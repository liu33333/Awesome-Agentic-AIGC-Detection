# Technical comparison

[← Paper list](../README.md) · **English** · [简体中文](COMPARISON_CN.md)

Compare the listed methods across agent organization, tools, feedback, training and evidence.

[Visual (images & videos)](#visual) · [Cross-modal](#cross-modal)

Organization refers to inference time; training describes agent adaptation, not whether underlying tools were pretrained. Tools are predefined unless code generation is specified.

<a name="visual"></a>

## Visual (images & videos)

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[ATAR](../README.md#atar)** | Single agent | Predefined crop + 22 forensic tools | Choose next crop/tool or stop | SFT + GRPO; tool-prior curriculum | Verdict + region descriptions; Grounded-SAM masks |
| **[ForenAgent](../README.md#forenagent)** | Single agent | Generated processing code + 12 fixed forensic tools | Revise operations/crops using tool outputs | SFT + GRPO | Verdict + reasoning + tool visualizations |
| **[SafeGuard](../README.md#safeguard)** | Perceptual solver + verifier | Predefined localization + four forensic tools | Revise hypotheses and reacquire evidence (≤3 cycles) | No agent fine-tuning; forensic tools tuned | Verdict + confidence + localized cues |
| **[Defake-o3](../README.md#defake-o3)** | Single agent | Predefined Zoom In | Choose another crop or final verdict | SFT + GRPO; verifier used for rewards | Verdict + global text; optional boxes/text |
| **[Hermes](../README.md#hermes)** | Planner + reasoner + three-role deliberation | RAG-selected Q&A checks + vision tools | Acquire tool evidence; revise graph (≤3 rounds) | No task-specific agent training | Verdict/score + temporal evidence graph |
| **[UniShield](../README.md#unishield)** | Perception → detection → report | Predefined eight-detector toolbox | One detector per image; no backtracking | GRPO task router; prompted scheduler | Verdict + report; task-dependent masks |
| **[AgentFoX](../README.md#agentfox)** | Single reasoning core + experts | Predefined experts + reliability profiles | Refine fusion/report on collected evidence | No core fine-tuning described; fitted calibration | Verdict + confidence + evidence report |
| **[EvoGuard](../README.md#evoguard)** | Single orchestrator | Detector APIs + capability profiles | Invoke complementary detectors or stop | GRPO; frozen detector tools | Verdict + multi-tool analysis |
| **[ForgeryVCR](../README.md#forgeryvcr)** | Single agent | ELA / NoisePrint++ / FFT / zoom | Use visual outputs for further tools/localization | SFT + GRPO | Verdict + boxes → SAM2 masks |
| **[AIFo](../README.md#aifo)** | Gatherer / reasoner / debaters / judge | Search / metadata / classifiers / VLM | Debate existing evidence; judge stops | Prompted agents; no weight training | Verdict + provenance/metadata + rationale |

<a name="cross-modal"></a>

## Cross-modal

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[OmniVL-Guard Pro](../README.md#omnivl-guard-pro)** | Single inference policy | Predefined search / crop / vision / SAM3 | Choose next tool from observations/errors | SFT + outcome RL + Checker-guided process RL | Verdict + trace + spatial/text/temporal grounding |
| **[FakeHunter](../README.md#fakehunter)** | Single prompted multimodal model | Memory retrieval / zoom / mel-spectrogram | Low confidence triggers visual/audio inspection | No agent fine-tuning; training-set memory | Verdict + manipulation type + explanation |
