# Technical comparison

[← Paper list](../README.md) · **English** · [简体中文](COMPARISON_CN.md)

Compare inference models, training requirements and agent workflows.

[Inference setups](#inference-setups) · [Agent workflows](#agent-workflows)

<a name="inference-setups"></a>

## Inference setups

Task tags describe explicit outputs: Detection (authenticity verdict), Localization (manipulated regions/spans/masks), and Explanation (reader-facing forensic rationale). Models reflect forensic inference. Agent training-free concerns task-specific agent parameter updates; tool training, calibration and memory construction are noted separately.

### Visual (images & videos)

| Method | Input / task coverage | Forensic inference models / tools | Agent training-free | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[ATAR](../README.md#atar)** | Image · generated-image detection; face/local/document manipulation<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen3-VL-8B-Instruct<br><sub>Tools: Grounded-SAM</sub> | No | SFT + GRPO. Grounded-SAM converts region descriptions to localization masks. |
| **[ForenAgent](../README.md#forenagent)** | Image · generated-image detection; local tampering<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-VL-7B<br><sub>Tools: 12 forensic tools</sub> | No | Full-parameter SFT + GRPO. Artifact-based adjudication; crops guide inspection. |
| **[SafeGuard](../README.md#safeguard)** | Video · generated content with social risks<br><sub>Outputs: Detection · Explanation</sub> | GPT-4o + Gemini-2.5-Pro<br><sub>Tools: Grounding DINO; SAM 2; RAFT; Depth Anything V2; DINOv2; D3</sub> | Yes | Prompted agents; D3 and Depth Anything V2 are task-tuned. Masks select regions for inspection. |
| **[Defake-o3](../README.md#defake-o3)** | Image · generated-content detection<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen3-VL-8B-Instruct<br><sub>Tools: Zoom In crop tool</sub> | No | SFT + GRPO. Local evidence boxes are optional; Evidence Verifier is training-only. |
| **[Hermes](../README.md#hermes)** | Video · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-VL-8B + ChatGPT-5<br><sub>Tools: Off-the-shelf vision tools</sub> | Yes | No task-specific agent training. ChatGPT-5 plans at inference; ERG timestamps ground evidence. |
| **[UniShield](../README.md#unishield)** | Image · generated-image detection; face/local/document manipulation<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen2.5-VL + GPT-4o<br><sub>Tools: IML-ViT; FakeShield; AscFormer; DMDL-R1 / GLaMM; CLIP; DFD-R1; AIDE; FakeVLM</sub> | No | GRPO router / DFD-R1 / DMDL-R1; GLaMM fine-tuned. Localization applies to natural-image/document branches; Qwen size unspecified. |
| **[AgentFoX](../README.md#agentfox)** | Image · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-32B + GPT-4o<br><sub>Tools: DRCT; RINE; SPAI; PatchShuffle</sub> | Yes | Frozen agent/expert weights; fitted score calibrators and reference-data priors. |
| **[EvoGuard](../README.md#evoguard)** | Image · generated-content detection<br><sub>Outputs: Detection</sub> | Qwen3-VL-4B-Instruct<br><sub>Tools: Effort; FakeVLM; MIRROR; AIDE</sub> | No | GRPO-trained policy; frozen tools. Training-free extension applies to adding tools after policy training. |
| **[ForgeryVCR](../README.md#forgeryvcr)** | Image · manipulation detection/localization<br><sub>Outputs: Detection · Localization</sub> | Qwen3-VL-4B-Instruct<br><sub>Tools: NoisePrint++; SAM2; ELA / FFT / zoom</sub> | No | SFT + GRPO. Boxes become SAM2 masks; the main policy uses visual intermediates. |
| **[AIFo](../README.md#aifo)** | Image · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | GPT-4o<br><sub>Tools: Five pretrained classifiers; optional CLIP-ViT-B/32 retrieval</sub> | Yes | Prompted agents and frozen classifiers; optional case memory retrieves without parameter updates. |

### Cross-modal

| Method | Input / task coverage | Forensic inference models / tools | Agent training-free | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[OmniVL-Guard Pro](../README.md#omnivl-guard-pro)** | Text–image / text–video · forgery/localization/fact-checking; also standalone modes<br><sub>Outputs: Detection · Localization</sub> | Qwen3-VL-8B<br><sub>Tools: InsightFace; SAM3; search / crop / frame tools</sub> | No | FSTR SFT + outcome/process RL. Checker is training-only; reported task outputs include classes and grounding. |
| **[FakeHunter](../README.md#fakehunter)** | Audio–video · manipulation detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-Omni-7B<br><sub>Alternative evaluated: MiniCPM-o-2_6</sub><br><sub>Tools: CLIP + CLAP encoders; FAISS retrieval memory</sub> | Yes | No agent fine-tuning. K-means fits retrieval memory on training-set CLIP/CLAP embeddings. |

<details>
<summary>AIFo classifier identifiers</summary>

- haywoodsloan/ai-image-detector-deploy
- Organika/sdxl-detector
- legekka/AI-Anime-Image-Detector-ViT
- Smogy/SMOGY-Ai-images-detector
- NYUAD-ComNets/NYUAD_AI-generated_images_detector

</details>

<a name="agent-workflows"></a>

## Agent workflows

Organization refers to inference time; training describes agent adaptation, not whether underlying tools were pretrained. Tools are predefined unless code generation is specified.

<a name="visual"></a>

### Visual (images & videos)

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

### Cross-modal

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[OmniVL-Guard Pro](../README.md#omnivl-guard-pro)** | Single inference policy | Predefined search / crop / vision / SAM3 | Choose next tool from observations/errors | SFT + outcome RL + Checker-guided process RL | Verdict + trace + spatial/text/temporal grounding |
| **[FakeHunter](../README.md#fakehunter)** | Single prompted multimodal model | Memory retrieval / zoom / mel-spectrogram | Low confidence triggers visual/audio inspection | No agent fine-tuning; training-set memory | Verdict + manipulation type + explanation |

