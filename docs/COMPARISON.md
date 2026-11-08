# Technical comparison

[← Paper list](../README.md) · **English** · [简体中文](COMPARISON_CN.md)

Compare inference models, training requirements and agent workflows.

Both sections use only Audio, Visual, Text and Cross-modal groups, in the catalog’s date order. Fixed workflows, rule-based orchestration and tool-selection behavior are described within the tables.

These rows retain the model versions reported in the papers; newer candidate models appear in [Resources](../README.md#resources).

[Inference setups](#inference-setups) · [Agent workflows](#agent-workflows)

<a name="inference-setups"></a>

## Inference setups

Task tags describe explicit outputs: Detection (authenticity verdict), Localization (manipulated regions/spans/masks), and Explanation (reader-facing forensic rationale). Models reflect forensic inference. Training labels describe task-specific forensic-agent adaptation; tool training, calibration and memory construction are noted separately.

[Audio](#inference-audio) · [Visual (images & videos)](#inference-visual) · [Text](#inference-text) · [Cross-modal](#inference-cross-modal)

<a name="inference-audio"></a>

### Audio

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[ToolDF](../README.md#tooldf)**<br><sub>[Findings of EMNLP 2026](https://aclanthology.org/2026.findings-emnlp.842/)</sub> | Audio · deepfake detection<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen2.5-Omni-3B<br><sub>Tools: Demucs separation; XLSR-AASIST specialists</sub> | LoRA SFT | LoRA SFT on tool-use trajectories; final any-fake aggregation. Audio reconstruction scripts accompany the code. |
| **[SEAR / BAEA](../README.md#sear)**<br><sub>arXiv 2026 preprint</sub> | Audio · deepfake detection<br><sub>Outputs: Detection · Explanation</sub> | Frozen Qwen2.5-Omni-7B<br><sub>Tools: librosa, 35 acoustic measurements</sub> | Training-free | Acoustic features are compared with real-audio median/MAD statistics. Adaptive selects feature groups within a budget; Fixed uses deterministic evidence acquisition. |

<a name="inference-visual"></a>

### Visual (images & videos)

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[ATAR](../README.md#atar)**<br><sub>ACM Multimedia 2026 Oral · accepted</sub> | Image · generated-image detection; face/local/document manipulation<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen3-VL-8B-Instruct<br><sub>Tools: Grounded-SAM</sub> | SFT + RL | SFT + GRPO. Grounded-SAM converts region descriptions to localization masks. |
| **[Defake-o3](../README.md#defake-o3)**<br><sub>ACM Multimedia 2026 accepted</sub> | Image · generated-content detection<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen3-VL-8B-Instruct<br><sub>Tools: Zoom In crop tool</sub> | SFT + RL | LoRA SFT + GRPO. The training-time Evidence Verifier supplies rewards; inference can return local evidence boxes. |
| **[DVAR](../README.md#dvar)**<br><sub>ACM Multimedia 2026</sub> | Video · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | GPT-5.4<br><sub>Tools: GenVideoKB retrieval</sub> | Training-free | Generative/natural explanation agents and an arbiter use two debate rounds. The evaluation knowledge base is frozen. |
| **[ForgeryVCR](../README.md#forgeryvcr)**<br><sub>ACM Multimedia 2026 Oral · accepted</sub> | Image · manipulation detection/localization<br><sub>Outputs: Detection · Localization</sub> | Qwen3-VL-4B-Instruct<br><sub>Tools: NoisePrint++; SAM2; ELA / FFT / zoom</sub> | SFT + RL | SFT + GRPO. The policy uses visual intermediates; predicted boxes prompt SAM2 masks. |
| **[ForenAgent](../README.md#forenagent)**<br><sub>ECCV 2026 published</sub> | Image · generated-image detection; local tampering<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-VL-7B<br><sub>Tools: 12 forensic tools</sub> | SFT + RL | Full-parameter SFT + GRPO. Python operations and forensic-tool outputs guide iterative inspection. |
| **[SafeGuard](../README.md#safeguard)**<br><sub>ECCV 2026 published</sub> | Video · generated content with social risks<br><sub>Outputs: Detection · Explanation</sub> | GPT-4o + Gemini-2.5-Pro<br><sub>Tools: Grounding DINO; SAM 2; RAFT; Depth Anything V2; DINOv2; D3</sub> | Training-free | Prompted agents; D3 and Depth Anything V2 are task-tuned. Masks select regions for inspection. |
| **[Dissecting Agentic Forensics](../README.md#dissecting-agentic-forensics)**<br><sub>ECCV 2026 AI4MFDD workshop</sub> | Image · forgery detection<br><sub>Outputs: Detection · Explanation</sub> | Seven detectors → MLLM auditors + judge<br><sub>Strong hybrid: Gemma-4-26B-A4B-it auditors + GPT-5 judge</sub> | Training-free agents | Calibrated scores from seven detectors feed auditors and a judge. The listed hybrid uses Gemma auditors and a GPT-5 judge. |
| **[FACT](../README.md#fact)**<br><sub>arXiv 2026 preprint</sub> | Image · authenticity detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-VL-8B-Instruct<br><sub>Tools: five frozen experts; eight probes</sub> | SFT + RL | SFT followed by cost-aware GRPO. GPT-5.1 supports training-time skill evolution and trajectory synthesis. |
| **[PATE-Forensics](../README.md#pate-forensics)**<br><sub>arXiv 2026 · DDL-X challenge report</sub> | Image · facial forgery<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen3.5-Flash<br><sub>Tool: DINOv3-L/16 forensic detection/segmentation</sub> | Explanation model training-free | Prompted Qwen3.5-Flash explains forensic perception outputs. The DINOv3 tool uses LoRA and supervised detection/mask losses. Official implementation: CLASP. |
| **[ARGUS](../README.md#argus)**<br><sub>arXiv 2026 preprint</sub> | Video · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-VL-7B<br><sub>Four observers: texture / lighting / motion / physics; judge</sub> | SFT + RL | All roles use LoRA SFT; the judge then uses GRPO. Four observers report texture, lighting, motion and physics evidence. |
| **[Hermes](../README.md#hermes)**<br><sub>ICML 2026 published</sub> | Video · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-VL-8B + ChatGPT-5<br><sub>Tools: Off-the-shelf vision tools</sub> | Training-free | Training-free agent workflow. ChatGPT-5 plans at inference; Qwen3-VL-8B performs perception, initial reasoning and deliberation. |
| **[ForeAgent](../README.md#foreagent)**<br><sub>arXiv 2026 preprint</sub> | Image · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-VL-8B<br><sub>Original + frequency views; NPR expert</sub> | LoRA + iterative SFT | LoRA pretraining + iterative self-filtered SFT. Training-time self-refinement supports a perception → verdict inference pipeline. |
| **[UniShield](../README.md#unishield)**<br><sub>CVPR Findings 2026 published</sub> | Image · generated-image detection; face/local/document manipulation<br><sub>Outputs: Detection · Localization · Explanation</sub> | Qwen2.5-VL + GPT-4o<br><sub>Tools: IML-ViT; FakeShield; AscFormer; DMDL-R1 / GLaMM; CLIP; DFD-R1; AIDE; FakeVLM</sub> | RL (router) | GRPO trains the task router, DFD-R1 and DMDL-R1; GLaMM is fine-tuned. Natural-image and document branches provide localization. |
| **[VRAG-DFD](../README.md#vrag-dfd)**<br><sub>CVPR Findings 2026</sub> | Image · deepfake detection<br><sub>Outputs: Detection · Explanation</sub> | Multimodal reasoning model | SFT + RL | Retrieval-first evidence collection followed by cross-verification; SFT + GRPO. |
| **[AgentFoX](../README.md#agentfox)**<br><sub>arXiv 2026 preprint</sub> | Image · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen3-32B + GPT-4o<br><sub>Tools: DRCT; RINE; SPAI; PatchShuffle</sub> | Training-free | Frozen agent/expert weights; fitted score calibrators and reference-data priors. |
| **[EvoGuard](../README.md#evoguard)**<br><sub>arXiv 2026 preprint</sub> | Image · generated-content detection<br><sub>Outputs: Detection</sub> | Qwen3-VL-4B-Instruct<br><sub>Tools: Effort; FakeVLM; MIRROR; AIDE</sub> | RL | GRPO trains the policy while detector tools stay frozen. Additional tools can be integrated after policy training. |
| **[AIFo](../README.md#aifo)**<br><sub>arXiv 2025 preprint</sub> | Image · generated-content detection<br><sub>Outputs: Detection · Explanation</sub> | GPT-4o<br><sub>Tools: Five pretrained classifiers; optional CLIP-ViT-B/32 retrieval</sub> | Training-free | Prompted agents and frozen classifiers; optional case memory provides retrieved evidence. |

<a name="inference-text"></a>

### Text

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[AIGT-Agent](../README.md#aigt-agent)**<br><sub>Findings of EMNLP 2026</sub> | Text · AI-generated-text detection<br><sub>Outputs: Detection · Explanation</sub> | GPT-5-mini<br><sub>Tools: MPU / Binoculars; Google Search; webpage filter/analyzer</sub> |  | Independent detector/search modules; exact-then-fuzzy search and webpage-evidence aggregation. |
| **[Qwen–LangGraph](../README.md#qwen-langgraph)**<br><sub>Discover Computing 2026 published</sub> | Text · human/AI provenance and AI-written/AI-rewritten classification<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-1.5B-Instruct<br><sub>Tools: DeBERTa-v3-xsmall; ELECTRA-small; lexical SGD classifier; stylometrics</sub> |  | Specialist classifiers are trained/fine-tuned; fusion weights and routing thresholds are selected on validation data. |

<a name="inference-cross-modal"></a>

### Cross-modal

| Method | Input / task coverage | Forensic inference models / tools | Agent<br>training | Training / setup notes |
| --- | --- | --- | --- | --- |
| **[FALCON](../README.md#falcon)**<br><sub>Pattern Recognition 2026 · journal pre-proof</sub> | Audio–video · deepfake detection<br><sub>Outputs: Detection · Explanation</sub> |  | Three-stage human-in-the-loop training | Specialists extract symbolic evidence for LLM forensic reasoning. |
| **[ENF framework](../README.md#enf-framework)**<br><sub>arXiv 2026</sub> | Audio–video · physical-signal and deepfake analysis<br><sub>Outputs: Detection</sub> | Physical ENF audio / rolling-shutter video analysis<br><sub>Spatial / rPPG / lip-sync / metadata checks; trained detectors</sub> |  | A deterministic state machine combines physical ENF analysis and trained detectors. ENF authentication requires an independent trusted reference. |
| **[Adaptive multi-agent framework](../README.md#adaptive-multi-agent)**<br><sub>Informatics 2026 published</sub> | Audio–video · deepfake detection<br><sub>Outputs: Detection · Explanation</sub> | Llama-3-70B (report) + Gemini-1.5-Flash (context)<br><sub>Detectors: Xception; FreqNet; MobileNetV2 + BiLSTM; EfficientNet-B0; ECAPA-TDNN + MLP</sub> |  | Supervised/fine-tuned detectors; frozen ECAPA backbone. A disagreement gate activates phase two; fusion weights are selected on validation data. |
| **[MM-VeriAgent](../README.md#mm-veriagent)**<br><sub>arXiv 2026 preprint</sub> | Image–text · broader misinformation, including AIGC<br><sub>Outputs: Detection</sub> | Qwen2.5-VL-7B<br><sub>Nine tools: retrieval / fact-checking / DFFreq / DDA / MVSS-Net / captioning / consistency</sub> | SFT + RL | SFT + GRPO, with cached tool outputs for RL. The policy selects tool names or stops within three rounds; the current sample uses fixed tool parameters. |
| **[OmniVL-Guard Pro](../README.md#omnivl-guard-pro)**<br><sub>arXiv 2026 preprint</sub> | Text–image / text–video · forgery/localization/fact-checking; also standalone modes<br><sub>Outputs: Detection · Localization</sub> | Qwen3-VL-8B<br><sub>Tools: InsightFace; SAM3; search / crop / frame tools</sub> | SFT + RL | FSTR SFT + outcome/process RL. A training-time Checker guides process rewards; outputs include classes and grounding. |
| **[T²Agent](../README.md#t2agent)**<br><sub>AAAI 2026</sub> | Image–text · broader misinformation detection<br><sub>Outputs: Detection</sub> | GPT-4o<br><sub>Tools: PSCC-NET; LLaVA-34B; web / reverse-image search</sub> | Training-free | MCTS explores tool/evidence paths; v2 adds greedy tool-subset selection. The released implementation uses cached/precomputed tool results. |
| **[FakeHunter](../README.md#fakehunter)**<br><sub>arXiv 2025 preprint</sub> | Audio–video · manipulation detection<br><sub>Outputs: Detection · Explanation</sub> | Qwen2.5-Omni-7B<br><sub>Alternative evaluated: MiniCPM-o-2_6</sub><br><sub>Tools: CLIP + CLAP encoders; FAISS retrieval memory</sub> |  | K-means builds retrieval memory from training-set CLIP/CLAP embeddings. |


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

Organization refers to inference time; training describes agent adaptation. Tool training and code-generation interfaces are noted in the relevant rows.

[Audio](#audio) · [Visual (images & videos)](#visual) · [Text](#text) · [Cross-modal](#cross-modal)

<a name="audio"></a>

### Audio

| Method | Agent organization | Tool interface | What changes after feedback? | Training / setup | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[ToolDF](../README.md#tooldf)** | Single agent + final aggregator | Separation + specialist detectors | Dynamically choose separation and detector tools | LoRA SFT; label-constructed training observations | Verdict + temporal/source evidence + rationale |
| **[SEAR / BAEA](../README.md#sear)** | Adaptive agent / Fixed baseline | Whitelisted acoustic feature groups | Adaptive chooses groups within budget; Fixed is deterministic | Frozen model; real-audio reference statistics | Verdict + measured acoustic evidence + rationale |

<a name="visual"></a>
<a name="related-visual"></a>

### Visual (images & videos)

| Method | Agent organization | Tool interface | What changes after feedback? | Training / setup | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[ATAR](../README.md#atar)** | Single agent | Predefined crop + 22 forensic tools | Choose next crop/tool or stop | SFT + GRPO; tool-prior curriculum | Verdict + region descriptions; Grounded-SAM masks |
| **[Defake-o3](../README.md#defake-o3)** | Single agent | Predefined Zoom In | Choose another crop or final verdict | SFT + GRPO; verifier used for rewards | Verdict + global text; optional boxes/text |
| **[DVAR](../README.md#dvar)** | Generative / natural explanation agents + arbiter | GenVideoKB retrieval | Fixed two-round debate revises explanations | Training-free; frozen evaluation KB | Verdict + debated explanations |
| **[ForgeryVCR](../README.md#forgeryvcr)** | Single agent | ELA / NoisePrint++ / FFT / zoom | Use visual outputs for further tools/localization | SFT + GRPO | Verdict + boxes → SAM2 masks |
| **[ForenAgent](../README.md#forenagent)** | Single agent | Generated processing code + 12 fixed forensic tools | Revise operations/crops using tool outputs | SFT + GRPO | Verdict + reasoning + tool visualizations |
| **[SafeGuard](../README.md#safeguard)** | Perceptual solver + verifier | Predefined localization + four forensic tools | Revise hypotheses and reacquire evidence (≤3 cycles) | Training-free agents; forensic tools tuned | Verdict + confidence + localized cues |
| **[Dissecting Agentic Forensics](../README.md#dissecting-agentic-forensics)** | Seven detectors → auditors → judge | Fixed detector scores and visual evidence | Auditors inspect collected evidence; judge aggregates | Training-free agents; calibrated detector scores | Verdict + audit rationale |
| **[FACT](../README.md#fact)** | Single agent | Five frozen experts + eight probes | Dynamically choose a tool or stop | SFT + cost-aware GRPO; GPT-5.1 training teacher | Verdict + tool evidence |
| **[PATE-Forensics](../README.md#pate-forensics)** | Fixed perception tool → explanation model | Detection probability / mask / suspicious crops | Fixed perception-to-explanation pipeline | Training-free explanation model; trained perception tool | Verdict + mask + evidence-constrained explanation |
| **[ARGUS](../README.md#argus)** | Four observers → judge | Fixed texture / lighting / motion / physics observations | Judge aggregates four reports | LoRA SFT for all; judge GRPO | Verdict + observer reports |
| **[Hermes](../README.md#hermes)** | Planner + reasoner + three-role deliberation | RAG-selected Q&A checks + vision tools | Acquire tool evidence; revise graph (≤3 rounds) | Training-free | Verdict/score + temporal evidence graph |
| **[ForeAgent](../README.md#foreagent)** | Fixed perception → verdict | Original / frequency views + NPR expert | Perception outputs feed the verdict stage | LoRA pretraining + iterative self-filtered SFT | Verdict + forensic rationale |
| **[UniShield](../README.md#unishield)** | Perception → detection → report | Predefined eight-detector toolbox | One detector per image | GRPO task router; prompted scheduler | Verdict + report; task-dependent masks |
| **[VRAG-DFD](../README.md#vrag-dfd)** | Retrieval → cross-verification | Fixed RAG evidence retrieval | Cross-verifies retrieved evidence within a fixed workflow | SFT + GRPO | Verdict + retrieved evidence |
| **[AgentFoX](../README.md#agentfox)** | Single reasoning core + experts | Predefined experts + reliability profiles | Refine fusion/report on collected evidence | Frozen core; fitted calibration | Verdict + confidence + evidence report |
| **[EvoGuard](../README.md#evoguard)** | Single orchestrator | Detector APIs + capability profiles | Invoke complementary detectors or stop | GRPO; frozen detector tools | Verdict + multi-tool analysis |
| **[AIFo](../README.md#aifo)** | Gatherer / reasoner / debaters / judge | Search / metadata / classifiers / VLM | Debate existing evidence; judge stops | Prompted agents; frozen weights | Verdict + provenance/metadata + rationale |

<a name="text"></a>
<a name="related-text"></a>

### Text

| Method | Agent organization | Tool interface | What changes after feedback? | Training / setup | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[AIGT-Agent](../README.md#aigt-agent)** | Independent detector and search modules → aggregation | MPU / Binoculars + search + webpage filtering/analysis | Fixed exact-then-fuzzy search | Prompted roles | Verdict + detector and web evidence |
| **[Qwen–LangGraph](../README.md#qwen-langgraph)** | Local fusion + selective single controller | Predefined classifiers / stylometric diagnostics | Choose tools, stop or abstain using new evidence (≤2 steps; ≤1 specialist call) | Trained tools and calibrated routing | Provenance/subtype probabilities + lexical/linguistic diagnostics + route records; probabilities come from classifiers |

<a name="cross-modal"></a>
<a name="related-cross-modal"></a>

### Cross-modal

| Method | Agent organization | Tool interface | What changes after feedback? | Training / setup | Evidence output |
| --- | --- | --- | --- | --- | --- |
| **[FALCON](../README.md#falcon)** | Specialist experts + LLM reasoner | Expert-extracted symbolic evidence |  | Three-stage human-in-the-loop training | Verdict + forensic rationale |
| **[ENF framework](../README.md#enf-framework)** | Deterministic state machine | ENF + spatial / rPPG / lip-sync / metadata detectors | Rule-defined transitions | Trained detectors | Signal / detector evidence; authenticity needs independent trusted ENF reference |
| **[Adaptive multi-agent framework](../README.md#adaptive-multi-agent)** | Rule-orchestrated five-detector ensemble + report model | Fixed detectors / XAI / context and transcription | Disagreement activates two phase-two detectors | Trained/fine-tuned detectors | Fused score + saliency/SHAP/cross-modal diagnostics + forensic report |
| **[MM-VeriAgent](../README.md#mm-veriagent)** | Single agent | Nine predefined tools | Choose tool name or stop within ≤3 rounds; current sample fixes parameters | SFT + GRPO; cache-based RL | Verdict + tool evidence |
| **[OmniVL-Guard Pro](../README.md#omnivl-guard-pro)** | Single inference policy | Predefined search / crop / vision / SAM3 | Choose next tool from observations/errors | SFT + outcome RL + Checker-guided process RL | Verdict + trace + spatial/text/temporal grounding |
| **[T²Agent](../README.md#t2agent)** | MCTS-guided agent | Forensic / VLM / web-search tools | Explore tool/evidence paths; v2 greedily selects tool subset | Training-free | Verdict + searched evidence paths |
| **[FakeHunter](../README.md#fakehunter)** | Single prompted multimodal model | Memory retrieval / zoom / mel-spectrogram | Low confidence triggers visual/audio inspection | Training-set memory | Verdict + manipulation type + explanation |
