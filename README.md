![Awesome Agentic AIGC Detection. Forensic illustration connecting image, audio and text signals with an agent, a magnified region and an evidence report.](assets/banner.svg)

**English** · [简体中文](README_CN.md)

[Intro](#intro) · [News](#news) · [Audio](#audio) · [Visual (images & videos)](#visual) · [Text](#text) · [Cross-modal](#cross-modal) · **[Technical comparison →](docs/COMPARISON.md)**

<a name="intro"></a>

## Intro

A collection of research on agentic detection of AI-generated content and related media manipulation. The focus is on methods that use tools, evidence-guided reasoning or multi-agent collaboration to investigate authenticity. Papers are grouped by input modality, with publication information and the availability of official implementations.

Models refer to forensic inference; agent training-free means no task-specific agent parameter updates. Tool training, calibration and retrieval memory are detailed in [Inference setups](docs/COMPARISON.md#inference-setups).

<a name="news"></a>

## News

- **2026‑10‑04**: Added the [technical comparison](docs/COMPARISON.md), covering five method-level dimensions.
- **2026‑10‑04**: Launched the Agentic AIGC Detection reading list.

<a name="audio"></a>

## Audio

No papers listed.

<a name="visual"></a>

## Visual (images & videos)

| Paper / task / model | Venue / status | Date | Official repository |
| --- | --- | --- | --- |
| <a name="atar"></a>**[Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066)** (ATAR)<br><sub>Image · <b>Detection · Localization · Explanation</b></sub><br><sub>Model: Qwen3-VL-8B-Instruct<br>Agent training-free: No</sub> | ACM&nbsp;Multimedia<br>2026<br><sub>Oral · accepted</sub> | 2026‑09‑30 | — |
| <a name="forenagent"></a>**[Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection](https://arxiv.org/abs/2512.16300)** (ForenAgent)<br><sub>Image · <b>Detection · Explanation</b></sub><br><sub>Model: Qwen2.5-VL-7B<br>Agent training-free: No</sub> | ECCV&nbsp;2026<br><sub>published</sub> | 2026‑09‑08 | [Toolkit&nbsp;only](https://github.com/zfr00/ForenAgent) |
| <a name="safeguard"></a>**[SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)**<br><sub>Video · <b>Detection · Explanation</b></sub><br><sub>Model: GPT-4o + Gemini-2.5-Pro<br>Agent training-free: Yes (tools tuned)</sub> | ECCV&nbsp;2026<br><sub>published</sub> | 2026‑09‑08 | [Project;<br>code&nbsp;pending](https://github.com/williamw99/SafeGuard) |
| <a name="defake-o3"></a>**[Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)**<br><sub>Image · <b>Detection · Localization · Explanation</b></sub><br><sub>Model: Qwen3-VL-8B-Instruct<br>Agent training-free: No</sub> | ACM&nbsp;Multimedia<br>2026<br><sub>accepted</sub> | 2026‑08‑17 | — |
| <a name="hermes"></a>**[Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://proceedings.mlr.press/v306/li26be.html)**<br><sub>Video · <b>Detection · Explanation</b></sub><br><sub>Model: Qwen3-VL-8B + ChatGPT-5<br>Agent training-free: Yes</sub> | ICML&nbsp;2026<br><sub>published</sub> | 2026‑07‑06 | — |
| <a name="unishield"></a>**[UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization](https://arxiv.org/abs/2510.03161)**<br><sub>Image · <b>Detection · Localization · Explanation</b></sub><br><sub>Model: Qwen2.5-VL + GPT-4o<br>Agent training-free: No</sub> | CVPR&nbsp;Findings<br>2026<br><sub>published</sub> | 2026‑06‑03 | — |
| <a name="agentfox"></a>**[AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection](https://arxiv.org/abs/2603.23115)**<br><sub>Image · <b>Detection · Explanation</b></sub><br><sub>Model: Qwen3-32B + GPT-4o<br>Agent training-free: Yes (calibration)</sub> | arXiv&nbsp;2026<br><sub>preprint</sub> | 2026‑03‑24 | [Minimal inference](https://github.com/suncore946/AgentFoX) |
| <a name="evoguard"></a>**[EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection](https://arxiv.org/abs/2603.17343)**<br><sub>Image · <b>Detection</b></sub><br><sub>Model: Qwen3-VL-4B-Instruct<br>Agent training-free: No</sub> | arXiv&nbsp;2026<br><sub>preprint</sub> | 2026‑03‑18 | — |
| <a name="forgeryvcr"></a>**[ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098)**<br><sub>Image · <b>Detection · Localization</b></sub><br><sub>Model: Qwen3-VL-4B-Instruct<br>Agent training-free: No</sub> | ACM&nbsp;Multimedia<br>2026<br><sub>Oral · accepted</sub> | 2026‑02‑15 | [Inference + weights](https://github.com/youqiwong/ForgeryVCR) |
| <a name="aifo"></a>**[From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection](https://arxiv.org/abs/2511.00181)** (AIFo)<br><sub>Image · <b>Detection · Explanation</b></sub><br><sub>Model: GPT-4o<br>Agent training-free: Yes</sub> | arXiv&nbsp;2025<br><sub>preprint</sub> | 2025‑10‑31 | — |

<a name="text"></a>

## Text

No papers listed.

<a name="cross-modal"></a>

## Cross-modal

| Paper / task / model | Venue / status | Date | Official repository |
| --- | --- | --- | --- |
| <a name="omnivl-guard-pro"></a>**[OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)**<br><sub>Text–image / text–video · <b>Detection · Localization</b></sub><br><sub>Model: Qwen3-VL-8B<br>Agent training-free: No</sub> | arXiv&nbsp;2026<br><sub>preprint</sub> | 2026‑05‑16 | [Project;<br>code&nbsp;pending](https://github.com/shen8424/OmniVL-Guard-Pro) |
| <a name="fakehunter"></a>**[Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581)** (FakeHunter)<br><sub>Audio–video · <b>Detection · Explanation</b></sub><br><sub>Model: Qwen2.5-Omni-7B; alt. MiniCPM-o-2_6<br>Agent training-free: Yes (fitted memory)</sub> | arXiv&nbsp;2025<br><sub>preprint</sub> | 2025‑08‑20 | — |


