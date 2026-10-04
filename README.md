# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

Papers on agentic AIGC detection, organized by audio, visual, text and cross-modal evidence, with comparisons of agent organization, tools, feedback, training and evidence outputs.

## Contents

- [Audio](#audio)
- [Visual (images & videos)](#visual)
- [Text](#text)
- [Cross-modal](#cross-modal)
- [Technical comparison](#technical-comparison)
- [Contributing](#contributing)

Tables run newest first: published papers use the conference opening date; preprints and accepted papers without verified proceedings publication use the first arXiv submission date. Status checked on 2026-10-04; “—” means no official repository verified.

<a id="audio"></a>

## Audio

No verified standalone entries yet.

<a id="visual"></a>

## Visual (images & videos)

| Paper | Venue / status | Date | Input / task | Official repository |
| --- | --- | --- | --- | --- |
| <a id="atar"></a>**[Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066)** (ATAR) | ACM Multimedia 2026 · Oral · accepted | 2026-09-30 | Image · generated-image detection; face/local/document manipulation | — |
| <a id="forenagent"></a>**[Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection](https://arxiv.org/abs/2512.16300)** (ForenAgent) | ECCV 2026 · published | 2026-09-08 | Image · generated-image detection; local tampering | [Toolkit only](https://github.com/zfr00/ForenAgent) |
| <a id="safeguard"></a>**[SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)** | ECCV 2026 · published | 2026-09-08 | Video · generated content with social risks | [Project; code pending](https://github.com/williamw99/SafeGuard) |
| <a id="defake-o3"></a>**[Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)** | ACM Multimedia 2026 · accepted | 2026-08-17 | Image · generated-content detection | — |
| <a id="hermes"></a>**[Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://proceedings.mlr.press/v306/li26be.html)** | ICML 2026 · published | 2026-07-06 | Video · generated-content detection | — |
| <a id="unishield"></a>**[UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization](https://arxiv.org/abs/2510.03161)** | CVPR Findings 2026 · published | 2026-06-03 | Image · generated-image detection; face/local/document manipulation | — |
| <a id="agentfox"></a>**[AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection](https://arxiv.org/abs/2603.23115)** | arXiv 2026 · preprint | 2026-03-24 | Image · generated-content detection | [Minimal inference](https://github.com/suncore946/AgentFoX) |
| <a id="evoguard"></a>**[EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection](https://arxiv.org/abs/2603.17343)** | arXiv 2026 · preprint | 2026-03-18 | Image · generated-content detection | — |
| <a id="forgeryvcr"></a>**[ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098)** | ACM Multimedia 2026 · Oral · accepted | 2026-02-15 | Image · manipulation detection/localization | [Inference + weights](https://github.com/youqiwong/ForgeryVCR) |
| <a id="aifo"></a>**[From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection](https://arxiv.org/abs/2511.00181)** (AIFo) | arXiv 2025 · preprint | 2025-10-31 | Image · generated-content detection | — |

<a id="text"></a>

## Text

No verified standalone entries yet.

<a id="cross-modal"></a>

## Cross-modal

Classified by jointly analyzed media evidence; text instructions alone do not make a method cross-modal.

| Paper | Venue / status | Date | Input / task | Official repository |
| --- | --- | --- | --- | --- |
| <a id="omnivl-guard-pro"></a>**[OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)** | arXiv 2026 · preprint | 2026-05-16 | Text–image / text–video · forgery/localization/fact-checking; also standalone modes | [Project; code pending](https://github.com/shen8424/OmniVL-Guard-Pro) |
| <a id="fakehunter"></a>**[Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581)** (FakeHunter) | arXiv 2025 · preprint | 2025-08-20 | Audio–video · manipulation detection | — |

<a id="technical-comparison"></a>

## Technical comparison

Organization refers to inference time; training describes agent adaptation, not whether underlying tools were pretrained. Tools are predefined unless code generation is specified.

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| ATAR | Single agent | Predefined crop + 22 forensic tools | Choose next crop/tool or stop | SFT + GRPO; tool-prior curriculum | Verdict + region descriptions; Grounded-SAM masks |
| ForenAgent | Single agent | Generated processing code + 12 fixed forensic tools | Revise operations/crops using tool outputs | SFT + GRPO | Verdict + reasoning + tool visualizations |
| SafeGuard | Perceptual solver + verifier | Predefined localization + four forensic tools | Revise hypotheses and reacquire evidence (≤3 cycles) | No agent fine-tuning; forensic tools tuned | Verdict + confidence + localized cues |
| Defake-o3 | Single agent | Predefined Zoom In | Choose another crop or final verdict | SFT + GRPO; verifier used for rewards | Verdict + global text; optional boxes/text |
| Hermes | Planner + reasoner + three-role deliberation | RAG-selected Q&A checks + vision tools | Acquire tool evidence; revise graph (≤3 rounds) | No task-specific agent training | Verdict/score + temporal evidence graph |
| UniShield | Perception → detection → report | Predefined eight-detector toolbox | One detector per image; no backtracking | GRPO task router; prompted scheduler | Verdict + report; task-dependent masks |
| AgentFoX | Single reasoning core + experts | Predefined experts + reliability profiles | Refine fusion/report on collected evidence | No core fine-tuning described; fitted calibration | Verdict + confidence + evidence report |
| EvoGuard | Single orchestrator | Detector APIs + capability profiles | Invoke complementary detectors or stop | GRPO; frozen detector tools | Verdict + multi-tool analysis |
| ForgeryVCR | Single agent | ELA / NoisePrint++ / FFT / zoom | Use visual outputs for further tools/localization | SFT + GRPO | Verdict + boxes → SAM2 masks |
| AIFo | Gatherer / reasoner / debaters / judge | Search / metadata / classifiers / VLM | Debate existing evidence; judge stops | Prompted agents; no weight training | Verdict + provenance/metadata + rationale |
| OmniVL-Guard Pro | Single inference policy | Predefined search / crop / vision / SAM3 | Choose next tool from observations/errors | SFT + outcome RL + Checker-guided process RL | Verdict + trace + spatial/text/temporal grounding |
| FakeHunter | Single prompted multimodal model | Memory retrieval / zoom / mel-spectrogram | Low confidence triggers visual/audio inspection | No agent fine-tuning; training-set memory | Verdict + manipulation type + explanation |

<a id="contributing"></a>

## Contributing

[Suggest a paper](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=paper_suggestion.md) or [report a correction](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=correction.md). Include publication/date evidence, the official repository and source locations for comparison fields. See [CONTRIBUTING.md](CONTRIBUTING.md).
