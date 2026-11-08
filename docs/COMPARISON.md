# Technical comparison

[← Paper list](../README.md) · **English** · [简体中文](COMPARISON_CN.md)

Compare inference models, training requirements and agent workflows.

These rows retain the model versions reported in the papers; newer candidate models appear in [Resources](../README.md#resources).

[Inference setups](#inference-setups) · [Agent workflows](#agent-workflows)

<a name="inference-setups"></a>

## Inference setups

Task tags describe explicit outputs: Detection (authenticity verdict), Localization (manipulated regions/spans/masks), and Explanation (reader-facing forensic rationale). Models reflect forensic inference. Training labels describe task-specific forensic-agent adaptation; tool training, calibration and memory construction are noted separately.

### Audio

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[ToolDF](../README.md#tooldf)**<br><sub>[Findings of EMNLP 2026](https://aclanthology.org/2026.findings-emnlp.842/)</sub> | Audio · deepfake detection<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen2.5-Omni-3B<br><sub>Tools: Demucs separation; XLSR-AASIST specialists</sub> | LoRA SFT | Training tool observations are label-constructed. Final any-fake aggregation. [Code](https://github.com/rlataewoo/tooldf); raw audio requires reconstruction; weight link not independently verified. |
| **[SEAR / BAEA](../README.md#sear)**<br><sub>arXiv 2026 preprint</sub> | Audio · deepfake detection<br><sub>Outputs: Detection · Explanation</sub> | Frozen Qwen2.5-Omni-7B<br><sub>Tools: librosa, 35 acoustic measurements</sub> | Training-free | Features compared with real-audio median/MAD. Budgeted Adaptive selects whitelisted groups with ≤1 follow-up; deterministic Fixed performs better in the paper. [Code](https://github.com/SEAR-benchmark/SEAR) + HF AQA labels; raw audio separate. |

### Visual (images & videos)

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[ATAR](../README.md#atar)**<br><sub>ACM Multimedia 2026 Oral · accepted</sub> | Image · generated-image detection; face/local/document manipulation<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen3-VL-8B-Instruct<br><sub>Tools: Grounded-SAM</sub> | SFT + RL | SFT + GRPO. Grounded-SAM converts region descriptions to localization masks. |
| **[ForenAgent](../README.md#forenagent)**<br><sub>ECCV 2026 published</sub> | Image · generated-image detection; local tampering<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-VL-7B<br><sub>Tools: 12 forensic tools</sub> | SFT + RL | Full-parameter SFT + GRPO. Artifact-based adjudication; crops guide inspection. Repository: Toolkit only. |
| **[SafeGuard](../README.md#safeguard)**<br><sub>ECCV 2026 published</sub> | Video · generated content with social risks<br><sub>Outputs: Detection · Explanation</sub> | GPT-4o + Gemini-2.5-Pro<br><sub>Tools: Grounding DINO; SAM 2; RAFT; Depth Anything V2; DINOv2; D3</sub> | Training-free | Prompted agents; D3 and Depth Anything V2 are task-tuned. Masks select regions for inspection. Repository: Project; code pending. |
| **[FACT](../README.md#fact)**<br><sub>arXiv 2026 preprint</sub> | Image · authenticity detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-VL-8B-Instruct<br><sub>Tools: five frozen experts; eight probes</sub> | SFT + RL | Cost-aware GRPO after SFT. GPT-5.1 is a training teacher, not an inference model. Code not located. |
| **[Defake-o3](../README.md#defake-o3)**<br><sub>ACM Multimedia 2026 accepted</sub> | Image · generated-content detection<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen3-VL-8B-Instruct<br><sub>Tools: Zoom In crop tool</sub> | SFT + RL | SFT + GRPO. Local evidence boxes are optional; Evidence Verifier is training-only. |
| **[Hermes](../README.md#hermes)**<br><sub>ICML 2026 published</sub> | Video · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-VL-8B + ChatGPT-5<br><sub>Tools: Off-the-shelf vision tools</sub> | Training-free | No task-specific agent training. ChatGPT-5 plans at inference; ERG timestamps ground evidence. |
| **[UniShield](../README.md#unishield)**<br><sub>CVPR Findings 2026 published</sub> | Image · generated-image detection; face/local/document manipulation<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen2.5-VL + GPT-4o<br><sub>Tools: IML-ViT; FakeShield; AscFormer; DMDL-R1 / GLaMM; CLIP; DFD-R1; AIDE; FakeVLM</sub> | RL (router) | GRPO router / DFD-R1 / DMDL-R1; GLaMM fine-tuned. Localization applies to natural-image/document branches; Qwen size unspecified. |
| **[AgentFoX](../README.md#agentfox)**<br><sub>arXiv 2026 preprint</sub> | Image · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-32B + GPT-4o<br><sub>Tools: DRCT; RINE; SPAI; PatchShuffle</sub> | Training-free | Frozen agent/expert weights; fitted score calibrators and reference-data priors. Repository: Minimal inference. |
| **[EvoGuard](../README.md#evoguard)**<br><sub>arXiv 2026 preprint</sub> | Image · generated-content detection<br><sub>Outputs: Detection</sub> | Qwen3-VL-4B-Instruct<br><sub>Tools: Effort; FakeVLM; MIRROR; AIDE</sub> | RL | GRPO-trained policy; frozen tools. Training-free extension applies to adding tools after policy training. |
| **[ForgeryVCR](../README.md#forgeryvcr)**<br><sub>ACM Multimedia 2026 Oral · accepted</sub> | Image · manipulation detection/localization<br><sub>Outputs: Detection · Localization</sub> | Qwen3-VL-4B-Instruct<br><sub>Tools: NoisePrint++; SAM2; ELA / FFT / zoom</sub> | SFT + RL | SFT + GRPO. Boxes become SAM2 masks; the main policy uses visual intermediates. Repository: Inference + weights. |
| **[AIFo](../README.md#aifo)**<br><sub>arXiv 2025 preprint</sub> | Image · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | GPT-4o<br><sub>Tools: Five pretrained classifiers; optional CLIP-ViT-B/32 retrieval</sub> | Training-free | Prompted agents and frozen classifiers; optional case memory retrieves without parameter updates. |

### Related visual methods: fixed workflows

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[Dissecting Agentic Forensics](../README.md#dissecting-agentic-forensics)**<br><sub>ECCV 2026 AI4MFDD workshop · author-reported</sub> | Image · forgery detection<br><sub>Outputs: Detection · Explanation</sub> | Seven detectors → MLLM auditors + judge<br><sub>Strong hybrid: Gemma-4-26B-A4B-it auditors + GPT-5 judge</sub> | Training-free agents | Detector scores calibrated; detectors run first in a fixed workflow. Workshop status author-reported; code not found. |
| **[PATE-Forensics](../README.md#pate-forensics)**<br><sub>arXiv 2026 · DDL-X challenge report</sub> | Image · facial forgery<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen3.5-Flash<br><sub>Tool: DINOv3-L/16 forensic detection/segmentation</sub> | Explanation model training-free | Fixed perception → explanation, no autonomous tool selection. Forensic tool uses LoRA and supervised detection/mask losses. Paper's code URL redirects to CLASP, whose naming differs. |
| **[ARGUS](../README.md#argus)**<br><sub>arXiv 2026 preprint</sub> | Video · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-VL-7B<br><sub>Four observers: texture / lighting / motion / physics; judge</sub> | SFT + RL | All roles use LoRA SFT; judge then uses GRPO. Fixed four-observer + judge workflow, no learned tool policy. [Code, datasets and LoRAs](https://github.com/XavierJiezou/ARGUS). |
| **[ForeAgent](../README.md#foreagent)**<br><sub>arXiv 2026 preprint</sub> | Image · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-VL-8B<br><sub>Original + frequency views; NPR expert</sub> | LoRA + iterative SFT | LoRA pretraining + iterative self-filtered SFT; self-refinement is training-time. Fixed perception → verdict at inference. Code not found; author-linked HF weights Shimin/qwen3_vl_8b_foreagent not verified. Distinct from ForenAgent. |
| **[VRAG-DFD](../README.md#vrag-dfd)**<br><sub>CVPR Findings 2026</sub> | Image · deepfake detection<br><sub>Outputs: Detection · Explanation</sub> | Multimodal reasoning model<br><sub>Exact model size not independently verified</sub> | SFT + RL | Fixed RAG-first retrieval + cross-verification; SFT + GRPO. [Code and weights](https://github.com/abigcatcat/VRAG-DFD). |
| **[DVAR](../README.md#dvar)**<br><sub>ACM Multimedia 2026 · author-reported</sub> | Video · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | GPT-5.4<br><sub>Tools: GenVideoKB retrieval</sub> | Training-free | Generative/natural explanation agents and arbiter use a fixed two-round debate. Evaluation KB frozen. Venue author-reported; DOI not independently verified; code/KB not found. |

### Text

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[Qwen–LangGraph](../README.md#qwen-langgraph)**<br><sub>Discover Computing 2026 published</sub> | Text · human/AI provenance and AI-written/AI-rewritten classification<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-1.5B-Instruct<br><sub>Tools: DeBERTa-v3-xsmall; ELECTRA-small; lexical SGD classifier; stylometrics</sub> | Not reported | Qwen adaptation unspecified; specialist classifiers trained/fine-tuned, fusion weights and route thresholds validation-selected. Author-linked analysis code/data not independently inspected. |

### Related text method: fixed evidence workflow

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[AIGT-Agent](../README.md#aigt-agent)**<br><sub>Findings of EMNLP 2026</sub> | Text · AI-generated-text detection<br><sub>Outputs: Detection · Explanation</sub> | GPT-5-mini<br><sub>Tools: MPU / Binoculars; Google Search; webpage filter/analyzer</sub> | Prompt adaptation | No parameter fine-tuning reported. Independent detector/search modules; fixed exact-then-fuzzy search and evidence aggregation. [Code + 4K benchmark](https://github.com/TrustAIRLab/AIGT-Agent); no third-party weights. |

### Cross-modal

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[MM-VeriAgent](../README.md#mm-veriagent)**<br><sub>arXiv 2026 preprint</sub> | Image–text · broader misinformation, including AIGC<br><sub>Outputs: Detection</sub> | Qwen2.5-VL-7B<br><sub>Nine tools: retrieval / fact-checking / DFFreq / DDA / MVSS-Net / captioning / consistency</sub> | SFT + RL | SFT + GRPO with cached tool outputs for RL. ≤3 tool rounds; policy chooses tool name or stop, current sample fixes parameters. Code not found. |
| **[OmniVL-Guard Pro](../README.md#omnivl-guard-pro)**<br><sub>arXiv 2026 preprint</sub> | Text–image / text–video · forgery/localization/fact-checking; also standalone modes<br><sub>Outputs: Detection · Localization</sub> | Qwen3-VL-8B<br><sub>Tools: InsightFace; SAM3; search / crop / frame tools</sub> | SFT + RL | FSTR SFT + outcome/process RL. Checker is training-only; reported task outputs include classes and grounding. Repository: Project; code pending. |
| **[FakeHunter](../README.md#fakehunter)**<br><sub>arXiv 2025 preprint</sub> | Audio–video · manipulation detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-Omni-7B<br><sub>Alternative evaluated: MiniCPM-o-2_6</sub><br><sub>Tools: CLIP + CLAP encoders; FAISS retrieval memory</sub> | Training-free | No agent fine-tuning. K-means fits retrieval memory on training-set CLIP/CLAP embeddings. |
| **[T²Agent](../README.md#t2agent)**<br><sub>AAAI 2026</sub> | Image–text · broader misinformation detection<br><sub>Outputs: Detection</sub> | GPT-4o<br><sub>Tools: PSCC-NET; LLaVA-34B; web / reverse-image search</sub> | Training-free | MCTS explores dynamic tool/evidence paths; v2 adds greedy tool subset selection. [Code](https://github.com/cuixing100876/T2Agent) partly uses cached/precomputed results and example backend differs; no end-to-end reproduction claim. |

### Related cross-modal methods: rule-based orchestration

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[Adaptive multi-agent framework](../README.md#adaptive-multi-agent)**<br><sub>Informatics 2026 published</sub> | Audio–video · deepfake detection<br><sub>Outputs: Detection · Explanation</sub> | Llama-3-70B (report) + Gemini-1.5-Flash (context)<br><sub>Detectors: Xception; FreqNet; MobileNetV2 + BiLSTM; EfficientNet-B0; ECAPA-TDNN + MLP</sub> | Rule-based orchestration | Supervised/fine-tuned detectors; frozen ECAPA backbone. Fixed disagreement gate enables phase two; validation-selected fusion weights, not an LLM action policy. Repository: Code + five detector checkpoints. |
| **[ENF framework](../README.md#enf-framework)**<br><sub>arXiv 2026 · submitted to IEEE TIFS</sub> | Audio–video · physical-signal and deepfake analysis<br><sub>Outputs: Detection</sub> | Physical ENF audio / rolling-shutter video analysis<br><sub>Spatial / rPPG / lip-sync / metadata checks; trained detectors</sub> | Rule-based orchestration | Deterministic state machine, no LLM planner. [Code + two weights](https://github.com/RyanSolent95/enf-video-forensics). TIFS submission is not acceptance. ENF presence alone does not authenticate without an independent trusted reference. |

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

<a name="audio"></a>

### Audio

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[ToolDF](../README.md#tooldf)** | Single agent + final aggregator | Separation + specialist detectors | Dynamically choose separation and detector tools | LoRA SFT; label-constructed training observations | Verdict + temporal/source evidence + rationale |
| **[SEAR / BAEA](../README.md#sear)** | Adaptive agent / Fixed baseline | Whitelisted acoustic feature groups | Adaptive chooses groups within budget and ≤1 follow-up; Fixed is deterministic | Frozen model; real-audio reference statistics | Verdict + measured acoustic evidence + rationale |

<a name="visual"></a>

### Visual (images & videos)

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[ATAR](../README.md#atar)** | Single agent | Predefined crop + 22 forensic tools | Choose next crop/tool or stop | SFT + GRPO; tool-prior curriculum | Verdict + region descriptions; Grounded-SAM masks |
| **[ForenAgent](../README.md#forenagent)** | Single agent | Generated processing code + 12 fixed forensic tools | Revise operations/crops using tool outputs | SFT + GRPO | Verdict + reasoning + tool visualizations |
| **[SafeGuard](../README.md#safeguard)** | Perceptual solver + verifier | Predefined localization + four forensic tools | Revise hypotheses and reacquire evidence (≤3 cycles) | No agent fine-tuning; forensic tools tuned | Verdict + confidence + localized cues |
| **[FACT](../README.md#fact)** | Single agent | Five frozen experts + eight probes | Dynamically choose a tool or stop | SFT + cost-aware GRPO; GPT-5.1 training teacher | Verdict + tool evidence |
| **[Defake-o3](../README.md#defake-o3)** | Single agent | Predefined Zoom In | Choose another crop or final verdict | SFT + GRPO; verifier used for rewards | Verdict + global text; optional boxes/text |
| **[Hermes](../README.md#hermes)** | Planner + reasoner + three-role deliberation | RAG-selected Q&A checks + vision tools | Acquire tool evidence; revise graph (≤3 rounds) | No task-specific agent training | Verdict/score + temporal evidence graph |
| **[UniShield](../README.md#unishield)** | Perception → detection → report | Predefined eight-detector toolbox | One detector per image; no backtracking | GRPO task router; prompted scheduler | Verdict + report; task-dependent masks |
| **[AgentFoX](../README.md#agentfox)** | Single reasoning core + experts | Predefined experts + reliability profiles | Refine fusion/report on collected evidence | No core fine-tuning described; fitted calibration | Verdict + confidence + evidence report |
| **[EvoGuard](../README.md#evoguard)** | Single orchestrator | Detector APIs + capability profiles | Invoke complementary detectors or stop | GRPO; frozen detector tools | Verdict + multi-tool analysis |
| **[ForgeryVCR](../README.md#forgeryvcr)** | Single agent | ELA / NoisePrint++ / FFT / zoom | Use visual outputs for further tools/localization | SFT + GRPO | Verdict + boxes → SAM2 masks |
| **[AIFo](../README.md#aifo)** | Gatherer / reasoner / debaters / judge | Search / metadata / classifiers / VLM | Debate existing evidence; judge stops | Prompted agents; no weight training | Verdict + provenance/metadata + rationale |

<a name="related-visual"></a>

### Related visual methods: fixed workflows

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[Dissecting Agentic Forensics](../README.md#dissecting-agentic-forensics)** | Seven detectors → auditors → judge | Fixed detector scores and visual evidence | Auditors inspect collected evidence; judge aggregates | Training-free agents; calibrated detector scores | Verdict + audit rationale |
| **[PATE-Forensics](../README.md#pate-forensics)** | Fixed perception tool → explanation model | Detection probability / mask / suspicious crops | No tool selection or feedback loop | No explanation-model fine-tuning; trained perception tool | Verdict + mask + evidence-constrained explanation |
| **[ARGUS](../README.md#argus)** | Four observers → judge | Fixed texture / lighting / motion / physics observations | Judge aggregates four reports; no learned tool selection | LoRA SFT for all; judge GRPO | Verdict + observer reports |
| **[ForeAgent](../README.md#foreagent)** | Fixed perception → verdict | Original / frequency views + NPR expert | No inference-time iterative self-refinement | LoRA pretraining + iterative self-filtered SFT | Verdict + forensic rationale |
| **[VRAG-DFD](../README.md#vrag-dfd)** | Retrieval → cross-verification | Fixed RAG evidence retrieval | Cross-verifies retrieved evidence within a fixed workflow | SFT + GRPO | Verdict + retrieved evidence |
| **[DVAR](../README.md#dvar)** | Generative / natural explanation agents + arbiter | GenVideoKB retrieval | Fixed two-round debate revises explanations, not an unconstrained tool policy | Training-free; frozen evaluation KB | Verdict + debated explanations |

<a name="text"></a>

### Text

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[Qwen–LangGraph](../README.md#qwen-langgraph)** | Local fusion + selective single controller | Predefined classifiers / stylometric diagnostics | Choose tools, stop or abstain using new evidence (≤2 steps; ≤1 specialist call) | Controller adaptation unspecified; trained tools and calibrated routing | Provenance/subtype probabilities + lexical/linguistic diagnostics + route records; classifiers, not controller, estimate probabilities |

<a name="related-text"></a>

### Related text method: fixed evidence workflow

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[AIGT-Agent](../README.md#aigt-agent)** | Independent detector and search modules → aggregation | MPU / Binoculars + search + webpage filtering/analysis | Fixed exact-then-fuzzy search; not unconstrained planning | Prompt adaptation; no parameter fine-tuning reported | Verdict + detector and web evidence |

<a name="cross-modal"></a>

### Cross-modal

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[MM-VeriAgent](../README.md#mm-veriagent)** | Single agent | Nine predefined tools | Choose tool name or stop within ≤3 rounds; current sample fixes parameters | SFT + GRPO; cache-based RL | Verdict + tool evidence |
| **[OmniVL-Guard Pro](../README.md#omnivl-guard-pro)** | Single inference policy | Predefined search / crop / vision / SAM3 | Choose next tool from observations/errors | SFT + outcome RL + Checker-guided process RL | Verdict + trace + spatial/text/temporal grounding |
| **[FakeHunter](../README.md#fakehunter)** | Single prompted multimodal model | Memory retrieval / zoom / mel-spectrogram | Low confidence triggers visual/audio inspection | No agent fine-tuning; training-set memory | Verdict + manipulation type + explanation |
| **[T²Agent](../README.md#t2agent)** | MCTS-guided agent | Forensic / VLM / web-search tools | Explore tool/evidence paths; v2 greedily selects tool subset | Training-free | Verdict + searched evidence paths |

<a name="related-cross-modal"></a>

### Related cross-modal methods: rule-based orchestration

| Method | Agent organization | Tool interface | What changes after feedback? | Agent training | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[Adaptive multi-agent framework](../README.md#adaptive-multi-agent)** | Rule-orchestrated five-detector ensemble + report model | Fixed detectors / XAI / context and transcription | Disagreement activates two phase-two detectors; no LLM tool planning | No learned orchestration policy; trained/fine-tuned detectors | Fused score + saliency/SHAP/cross-modal diagnostics + forensic report |
| **[ENF framework](../README.md#enf-framework)** | Deterministic state machine | ENF + spatial / rPPG / lip-sync / metadata detectors | Rule-defined transitions; no learned tool planner | Trained detectors; no LLM orchestration | Signal / detector evidence; authenticity needs independent trusted ENF reference |
