![Agentic AIGC Detection: layered landscape image frames, a highlighted scan region, and a magnified detail connected by evidence lines.](assets/banner.svg)

**English** · [简体中文](README_CN.md)

[Intro](#intro) · [News](#news) · [Audio](#audio) · [Visual (images & videos)](#visual) · [Text](#text) · [Cross-modal](#cross-modal) · **[Technical comparison →](docs/COMPARISON.md)** · [Surveys](#surveys) · [Resources](#resources) · [Link checks](#link-checks)

<a name="intro"></a>

## Intro

A collection of research on agentic detection of AI-generated content and related media manipulation. The focus is on methods that use tools, evidence-guided reasoning or multi-agent collaboration to investigate authenticity. Papers are grouped by input modality, with publication information and the availability of official implementations. The catalog uses only four input-modality groups: Audio, Visual, Text and Cross-modal. Tool use and collaboration workflows are described within each table.

Models refer to forensic inference. Catalog labels omit the -Instruct suffix; exact variants, tool training, calibration and retrieval memory are detailed in [Inference setups](docs/COMPARISON.md#inference-setups).

Training describes forensic-agent adaptation: Training-free, SFT (supervised fine-tuning), or RL (reinforcement learning). Tool training, calibration and memory construction are recorded separately.

Each table is ordered newest first by the main date shown; revision dates are noted separately. Workflow notes describe individual implementations. Code, weights and data links are presented side by side.

<a name="news"></a>

## News

- **2026‑11‑08**: Added audio and cross-modal tool reasoning plus FACT; unified the modality tables with workflow notes, added forensic models/benchmarks, and updated d1/Jev. Synchronized bilingual comparisons and added automated link audits.
- **2026‑10‑23**: Added Qwen–LangGraph text detection and two related tool-grounded/rule-orchestrated methods; updated comparisons, added an agent-evaluation survey, refreshed Qwen/System-1 model resources.
- **2026‑10‑04**: Added the [technical comparison](docs/COMPARISON.md), covering five method-level dimensions.
- **2026‑10‑04**: Launched the Agentic AIGC Detection reading list.

<a name="audio"></a>

## Audio

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

**[View technical comparison →](docs/COMPARISON.md#audio)**

<table>
<thead>
<tr>
<th width="50%" align="left">Paper / Workflow</th>
<th width="12%" align="left">Venue / Date</th>
<th width="24%" align="left">Tags · Model · Training</th>
<th width="14%" align="left">Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top"><a name="tooldf"></a><strong><a href="https://aclanthology.org/2026.findings-emnlp.842/">ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection</a></strong><br><sub>Select separation / specialist tools, then aggregate verdicts.</sub></td>
<td width="12%" valign="top">Findings EMNLP<br>2026<br>26/10</td>
<td width="24%" valign="top"><code>A</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen2.5‑Omni‑3B<br><sub>LoRA SFT</sub></td>
<td width="14%" valign="top"><a href="https://github.com/rlataewoo/tooldf">Code</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="sear"></a><strong><a href="https://arxiv.org/abs/2609.39847">SEAR: Spoofing Evidence-Grounded Audio Reasoning Benchmark for Audio Language Models</a></strong> (BAEA)<br><sub>BAEA-Adaptive selects acoustic feature groups within a budget; deterministic BAEA-Fixed performs better in the paper.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/09</td>
<td width="24%" valign="top"><code>A</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑Omni‑7B<br><sub>Training-free</sub></td>
<td width="14%" valign="top"><a href="https://github.com/SEAR-benchmark/SEAR">Code</a><br><a href="https://huggingface.co/datasets/SEAR-benchmark/SEAR">Annotations</a><br><sub>Raw audio separate</sub></td>
</tr>
</tbody>
</table>

<a name="visual"></a>
<a name="related-fixed-tool-and-multi-agent-workflows"></a>

## Visual (images & videos)

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

**[View technical comparison →](docs/COMPARISON.md#visual)**

<table>
<thead>
<tr>
<th width="50%" align="left">Paper / Workflow</th>
<th width="12%" align="left">Venue / Date</th>
<th width="24%" align="left">Tags · Model · Training</th>
<th width="14%" align="left">Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top"><a name="atar"></a><strong><a href="https://arxiv.org/abs/2609.39066">Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection</a></strong> (ATAR)<br><sub>Choose the next crop / forensic tool or stop; Grounded-SAM produces masks.</sub></td>
<td width="12%" valign="top">ACM MM 2026<br><sub>Oral · accepted</sub><br>26/09</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="forenagent"></a><strong><a href="https://arxiv.org/abs/2512.16300">Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection</a></strong> (ForenAgent)<br><sub>Generate processing code and use 12 forensic tools; revise operations from feedback.</sub></td>
<td width="12%" valign="top">ECCV 2026<br>26/09</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/zfr00/ForenAgent">Toolkit</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="safeguard"></a><strong><a href="https://arxiv.org/abs/2607.03069">SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection</a></strong><br><sub>Perceptual solver + verifier revise hypotheses and reacquire evidence (≤3 cycles).</sub></td>
<td width="12%" valign="top">ECCV 2026<br>26/09</td>
<td width="24%" valign="top"><code>V</code> · <code>D</code>&nbsp;<code>E</code><br>GPT‑4o<br>+ Gemini‑2.5‑Pro<br><sub>Training-free · tools tuned</sub></td>
<td width="14%" valign="top"><a href="https://github.com/williamw99/SafeGuard">Project</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="fact"></a><strong><a href="https://arxiv.org/abs/2609.05876">FACT: A Forensic Agent with Compiled Tool-Use Trajectories for AI-Generated Image Detection</a></strong><br><sub>Select among five experts and eight probes, or stop; GPT-5.1 is a training-only teacher.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/09</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="dissecting-agentic-forensics"></a><strong><a href="https://arxiv.org/abs/2609.24359">Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection</a></strong><br><sub>Seven preset detectors → auditors → judge; the listed models are the hybrid configuration.</sub></td>
<td width="12%" valign="top">ECCV 2026<br><sub>AI4MFDD Workshop</sub><br>26/09</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Gemma‑4‑26B‑A4B‑it<br>+ GPT‑5<br><sub>Training-free · score calibration</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="defake-o3"></a><strong><a href="https://arxiv.org/abs/2608.16259">Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection</a></strong><br><sub>Inspect further crops or give a verdict; the evidence verifier is training-only.</sub></td>
<td width="12%" valign="top">ACM MM 2026<br><sub>accepted</sub><br>26/08</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="pate-forensics"></a><strong><a href="https://arxiv.org/abs/2608.18573">PATE-Forensics: Perception-as-Tool for Explainable Deepfake Forensics with General-Purpose MLLMs</a></strong><br><sub>Fixed perception → explanation pipeline.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>DDL-X challenge report</sub><br>26/08</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen3.5‑Flash<br><sub>Training-free · tool trained</sub></td>
<td width="14%" valign="top"><a href="https://github.com/yqli00000/CLASP">Code<br><sub>now CLASP</sub></a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="argus"></a><strong><a href="https://arxiv.org/abs/2608.06865">Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection</a></strong> (ARGUS)<br><sub>Four fixed observers (texture / lighting / motion / physics) → judge.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/08</td>
<td width="24%" valign="top"><code>V</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/XavierJiezou/ARGUS">Code</a><br><a href="https://huggingface.co/XavierJiezou/argus-models">Weights</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="hermes"></a><strong><a href="https://proceedings.mlr.press/v306/li26be.html">Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection</a></strong><br><sub>Planner, reasoner and deliberation roles update a temporal evidence graph (≤3 rounds).</sub></td>
<td width="12%" valign="top">ICML 2026<br>26/07</td>
<td width="24%" valign="top"><code>V</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br>+ ChatGPT‑5<br><sub>Training-free</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="unishield"></a><strong><a href="https://arxiv.org/abs/2510.03161">UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization</a></strong><br><sub>Route each image to one detector, then report.</sub></td>
<td width="12%" valign="top">CVPR Findings<br>2026<br>26/06</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen2.5‑VL<br>+ GPT‑4o<br><sub>RL (router) · tools tuned</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="foreagent"></a><strong><a href="https://arxiv.org/abs/2606.26552">Perception, Verdict, and Evolution: Hindsight-Driven Self-Refining Forensics Agent for AI-Generated Image Detection</a></strong> (ForeAgent)<br><sub>Perception → verdict at inference; self-refinement happens during training.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/06</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br><sub>SFT</sub></td>
<td width="14%" valign="top"><a href="https://huggingface.co/Shimin/qwen3_vl_8b_foreagent">Weights</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="vrag-dfd"></a><strong><a href="https://arxiv.org/abs/2604.13660">VRAG-DFD: Verifiable Retrieval-Augmentation for MLLM-based Deepfake Detection</a></strong><br><sub>Retrieve evidence, then cross-verify it.</sub></td>
<td width="12%" valign="top">CVPR Findings<br>2026<br>26/06</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>MLLM<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/abigcatcat/VRAG-DFD">Code</a><br><a href="https://huggingface.co/abigcatcat/VRAG-DFD">Weights</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="dvar"></a><strong><a href="https://arxiv.org/abs/2604.16987">DVAR: Adversarial Multi-Agent Debate for Video Authenticity Detection</a></strong><br><sub>GenVideoKB retrieval + a fixed two-round debate and arbiter; evaluation KB is frozen.</sub></td>
<td width="12%" valign="top">ACM MM 2026<br>26/04<br><sub>preprint</sub></td>
<td width="24%" valign="top"><code>V</code> · <code>D</code>&nbsp;<code>E</code><br>GPT‑5.4<br><sub>Training-free</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="agentfox"></a><strong><a href="https://arxiv.org/abs/2603.23115">AgentFoX: LLM-Driven Agentic Multi-Expert Fusion with Explainability for AI-Generated Image Detection</a></strong><br><sub>Fuse collected expert evidence using calibrated reliability profiles.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/03</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen3‑32B<br>+ GPT‑4o<br><sub>Training-free · calibration</sub></td>
<td width="14%" valign="top"><a href="https://github.com/suncore946/AgentFoX">Minimal</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="evoguard"></a><strong><a href="https://arxiv.org/abs/2603.17343">EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection</a></strong><br><sub>Select complementary detector APIs or stop; detector tools remain frozen.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/03</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code><br>Qwen3‑VL‑4B<br><sub>RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="forgeryvcr"></a><strong><a href="https://arxiv.org/abs/2602.14098">ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization</a></strong><br><sub>Use visual tool outputs for further inspection; boxes become SAM2 masks.</sub></td>
<td width="12%" valign="top">ACM MM 2026<br><sub>Oral · accepted</sub><br>26/02</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code><br>Qwen3‑VL‑4B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/youqiwong/ForgeryVCR">Code</a><br><a href="https://huggingface.co/youqiwong/ForgeryVCR">Weights</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="aifo"></a><strong><a href="https://arxiv.org/abs/2511.00181">From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection</a></strong> (AIFo)<br><sub>Gather evidence, reason and debate; a judge decides when to stop.</sub></td>
<td width="12%" valign="top">arXiv 2025<br><sub>preprint</sub><br>25/10</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>GPT‑4o<br><sub>Training-free</sub></td>
<td width="14%" valign="top"></td>
</tr>
</tbody>
</table>

<a name="text"></a>
<a name="related-tool-augmented-multi-role-workflow"></a>

## Text

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

**[View technical comparison →](docs/COMPARISON.md#text)**

<table>
<thead>
<tr>
<th width="50%" align="left">Paper / Workflow</th>
<th width="12%" align="left">Venue / Date</th>
<th width="24%" align="left">Tags · Model · Training</th>
<th width="14%" align="left">Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top"><a name="qwen-langgraph"></a><strong><a href="https://link.springer.com/article/10.1007/s10791-026-10710-z">Performance evaluation and interpretability of a Qwen LangGraph agent for AI written and AI rewritten text detection</a></strong><br><sub>Fusion + selective controller: choose tools, stop or abstain (≤2 steps; ≤1 specialist call).</sub></td>
<td width="12%" valign="top">Discover<br>Computing 2026<br>26/10</td>
<td width="24%" valign="top"><code>T</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑1.5B<br><sub>Tools trained</sub></td>
<td width="14%" valign="top"><a href="https://drive.google.com/drive/folders/14wU4r0-uRirkJ9aP3xI1lj2yHfWkj7DQ">Author resources</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="aigt-agent"></a><strong><a href="https://aclanthology.org/2026.findings-emnlp.272/">Beyond Text-Intrinsic Features: An Agentic Framework for Evidence-Based AI-Generated Text Detection</a></strong> (AIGT-Agent)<br><sub>Separate detection and search modules; fixed exact-then-fuzzy search and webpage-evidence aggregation.</sub></td>
<td width="12%" valign="top">Findings EMNLP<br>2026<br>26/10</td>
<td width="24%" valign="top"><code>T</code> · <code>D</code>&nbsp;<code>E</code><br>GPT‑5‑mini</td>
<td width="14%" valign="top"><a href="https://github.com/TrustAIRLab/AIGT-Agent">Code</a><br><a href="https://github.com/TrustAIRLab/AIGT-Agent/tree/main/data/benchmark_4k">Benchmark</a></td>
</tr>
</tbody>
</table>

<a name="cross-modal"></a>
<a name="related-rule-orchestrated-methods"></a>
<a name="pending-further-verification"></a>

## Cross-modal

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

**[View technical comparison →](docs/COMPARISON.md#cross-modal)**

<table>
<thead>
<tr>
<th width="50%" align="left">Paper / Workflow</th>
<th width="12%" align="left">Venue / Date</th>
<th width="24%" align="left">Tags · Model · Training</th>
<th width="14%" align="left">Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top"><a name="falcon"></a><strong><a href="https://doi.org/10.1016/j.patcog.2026.115240">LLM as a forensic reasoner: Expert-guided video deepfake detection across modalities</a></strong> (FALCON)<br><sub>Specialist experts extract symbolic evidence for LLM forensic reasoning.</sub></td>
<td width="12%" valign="top">Pattern Recognition<br>2026<br><sub>journal pre-proof</sub><br>26/10<br><sub>online 10-29</sub></td>
<td width="24%" valign="top"><code>A+V</code> · <code>D</code>&nbsp;<code>E</code><br><sub>Three-stage human-in-the-loop training</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="adaptive-multi-agent"></a><strong><a href="https://doi.org/10.3390/informatics13100163">A Multi-Agent Framework with Adaptive Orchestration for Explainable Multi-Modal Deepfake Detection</a></strong><br><sub>Fixed disagreement threshold activates extra detectors, then fusion and reporting.</sub></td>
<td width="12%" valign="top">Informatics 2026<br>26/10</td>
<td width="24%" valign="top"><code>A+V</code> · <code>D</code>&nbsp;<code>E</code><br>Llama‑3‑70B<br>+ Gemini‑1.5‑Flash<br><sub>Rule-based · detectors trained</sub></td>
<td width="14%" valign="top"><a href="https://github.com/saoirsebarry/multiagent-deepfake-detection">Code</a><br><a href="https://github.com/saoirsebarry/multiagent-deepfake-detection/tree/main/checkpoints">Weights</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="enf-framework"></a><strong><a href="https://arxiv.org/abs/2610.22440">An Agentic ENF Framework for Forensic Video Authentication Against Generative AI</a></strong><br><sub>Deterministic state transitions over ENF and detector evidence; ENF authentication needs an independent trusted reference.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/10</td>
<td width="24%" valign="top"><code>A+V</code> · <code>D</code><br>Deterministic state machine<br><sub>Rule-based · detectors trained</sub></td>
<td width="14%" valign="top"><a href="https://github.com/RyanSolent95/enf-video-forensics">Code</a><br><a href="https://github.com/RyanSolent95/enf-video-forensics/tree/main/outputs">Weights</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="mm-veriagent"></a><strong><a href="https://arxiv.org/abs/2609.30698">MM-VeriAgent: Learning to Use Extensive Tools to Verify Multimodal Misinformation with Reinforcement Learning</a></strong><br><sub>Choose among nine tools or stop (≤3 rounds); parameters fixed in current sample. Broader image–text misinformation, including AIGC.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/09<br><sub>v2 26/11</sub></td>
<td width="24%" valign="top"><code>T+I</code> · <code>D</code><br>Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="omnivl-guard-pro"></a><strong><a href="https://arxiv.org/abs/2605.16962">OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics</a></strong><br><sub>Select search / crop / vision tools from observations or errors.</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>preprint</sub><br>26/05</td>
<td width="24%" valign="top"><code>T+I</code>&nbsp;/&nbsp;<code>T+V</code> · <code>D</code>&nbsp;<code>L</code><br>Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/shen8424/OmniVL-Guard-Pro">Project</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="fakehunter"></a><strong><a href="https://arxiv.org/abs/2508.14581">Memory-Anchored Multimodal Reasoning for Explainable Video Forensics</a></strong> (FakeHunter)<br><sub>Retrieve memory; low confidence triggers visual / audio inspection.</sub></td>
<td width="12%" valign="top">arXiv 2025<br><sub>preprint</sub><br>25/08</td>
<td width="24%" valign="top"><code>A+V</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑Omni‑7B<br><sub>alt. MiniCPM‑o‑2_6</sub><br><sub>K-means memory</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="t2agent"></a><strong><a href="https://arxiv.org/abs/2505.19768">T²Agent: A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search</a></strong><br><sub>MCTS explores tool / evidence paths; v2 adds greedy tool-subset selection. Broader image–text misinformation, including AIGC.</sub></td>
<td width="12%" valign="top">AAAI 2026<br>25/05<br><sub>preprint</sub></td>
<td width="24%" valign="top"><code>T+I</code> · <code>D</code><br>GPT‑4o<br><sub>Training-free</sub></td>
<td width="14%" valign="top"><a href="https://github.com/cuixing100876/T2Agent">Code<br><sub>partly cached</sub></a></td>
</tr>
</tbody>
</table>

<a name="surveys"></a>

## Related surveys

[Agent surveys](#agent-surveys) · [Detection surveys](#detection-surveys)

<a name="agent-surveys"></a>

### Agent surveys

| Survey | Venue / status | Main contents |
| --- | --- | --- |
| **[Large language model agent evaluation and benchmarking: a systematic survey, meta-taxonomy, and critical research roadmap](https://doi.org/10.1007/s10462-026-11678-4)** | Artificial Intelligence Review, 2026 | Validity-centered agent evaluation; capability–scoring–environment taxonomy, contamination, nondeterminism, reproducibility and execution cost. |
| **[A Survey on the Optimization of Large Language Model-based Agents](https://doi.org/10.1145/3789261)** | ACM Computing Surveys, 2026 | Agent SFT, RL and hybrid optimization; trajectory construction, reward design, prompt optimization and knowledge retrieval. |
| **[A Survey on Agentic Multimodal Large Language Models](https://arxiv.org/abs/2510.10991)** | arXiv 2025 · preprint | Multimodal reasoning, reflection and memory; tool invocation and environment interaction; training frameworks and evaluation datasets. |
| **[Evaluation and Benchmarking of LLM Agents: A Survey](https://doi.org/10.1145/3711896.3736570)** | KDD 2025 | Evaluation objectives (behavior, capabilities, reliability and safety), interaction modes, benchmarks, metrics and tooling; long-horizon deployment challenges. |
| **[Large Language Model Based Multi-agents: A Survey of Progress and Challenges](https://www.ijcai.org/proceedings/2024/890)** | IJCAI 2024 · Survey Track | Environment interfaces, role profiling, communication and collaboration, capability acquisition, and datasets for collective problem-solving and simulation. |
| **[A survey on large language model based autonomous agents](https://doi.org/10.1007/s11704-024-40231-1)** | Frontiers of Computer Science, 2024 | Profiling, memory, planning and action as a unified architecture; tool use, capability acquisition, applications and evaluation. |

<a name="detection-surveys"></a>

### Detection surveys

| Survey | Venue / status | Main contents |
| --- | --- | --- |
| **[AI-Generated Content Detection: A Cross-Modal Survey of Methods, Challenges, and Future Directions](https://www.researchsquare.com/article/rs-10864156/v1)** | Research Square 2026 · preprint | Cross-modal AI-generated content detection methods, challenges and future directions. |
| **[Detecting AI-Generated Video: A Vision–Language Dual-View Survey](https://aclanthology.org/2026.findings-acl.1613/)** | Findings of ACL 2026 | Four-layer video-detection taxonomy: intrinsic cues, spatiotemporal consistency, cross-modal consistency and language-guided world-level reasoning, including tool-augmented agentic pipelines. |
| **[Explainable deepfake detection across different modalities: An overview of methods and challenges](https://doi.org/10.1016/j.imavis.2025.105738)** | Image and Vision Computing, 2025 | Explainable detection across image, video, audio and text; saliency methods, local surrogates and attribution; datasets and evaluation. |
| **[Survey on AI-Generated Media Detection: From Non-MLLM to MLLM](https://arxiv.org/abs/2502.05240)** | arXiv 2025‑02 · preprint | Specialized versus MLLM-based detectors across modalities; authenticity classification, explanation and forgery localization. |
| **[Detecting Multimedia Generated by Large AI Models: A Survey](https://arxiv.org/abs/2402.00045)** | arXiv 2024 · preprint; revised 2025‑07 | Text, image, video, audio and multimodal detection; performance, generalization, robustness and interpretability; datasets and metrics. |

<a name="resources"></a>

## Resources

Selected platforms, model backbones and development tools for agentic media-forensics research. Check access requirements, model versions and data-handling terms before use.

Current model candidates and paper-specific reproduction backbones are listed separately. Evaluate candidate models on task-specific forensic benchmarks.

### Agentic forensic platforms

- [Resemble Investigator](https://docs.resemble.ai/detect/agents) · **Managed API.** Media-authenticity investigations with streamed evidence and assessments; requires an account with Investigator access.
- [Clyravision](https://en.merantix-momentum.com/clyravision) · **Contact-based platform.** Agent-based image analysis combining forensic traces, metadata and source/context checks; the product page includes a recorded demonstration.

### Detection services for agent tools

- [Reality Defender RealAPI](https://www.realitydefender.com/product/realapi) · **Detection API.** Image, audio and video manipulation analysis with structured results for integration into an agent's evidence pipeline.
- [Sightengine](https://www.sightengine.com/docs/ai-generated-image-detection) · **Detection API.** AI-generated image scoring, with separate deepfake and AI-video detection models documented alongside it.

### Specialized forensic models

- [VeriSpoof](https://arxiv.org/abs/2611.04634) (2026‑11‑03) · Qwen3-ASR-1.7B encoder plus MiniCPM5-2B for audio detection, attribution, recording conditions, segment localization and source verification, with checkable explanations. [Inference code](https://github.com/swagshaw/verispoof) and [Plus weights](https://huggingface.co/AustinXiao/VeriSpoof-Plus) are available. Code and weights use CC BY-NC 4.0.
- [Venus-DefakerOne2](https://arxiv.org/abs/2610.37918) (2026‑10‑27; revised 11‑02) · Qwen3.5-2B image/video forensic expert with fixed real/fake question answering. [Weights](https://huggingface.co/qcf568/DefakerOne2) and [inference helper scripts](https://github.com/inclusionAI/DefakerOne2) are available. Use preview for paper reproduction; release uses more training data.

### Datasets and benchmarks

- [SEAR](https://huggingface.co/datasets/SEAR-benchmark/SEAR) · Audio QA annotations for verdicts, cues, numerical measurements and forensic rationales, with [BAEA/evaluation code](https://github.com/SEAR-benchmark/SEAR). Obtain ASVspoof raw audio separately.
- [VeriSpoof-Bench](https://huggingface.co/datasets/AustinXiao/VeriSpoof-Bench) · Labels, manifests, metadata and reconstruction materials for 54 subsets / 177,852 items. Obtain raw audio from the source corpora under their respective licenses.
- [RRVBench](https://www.modelscope.cn/models/DanceText/RRVBench) · DefakerOne2 video benchmark with 1,319 real and 11,000 synthetic videos from 11 generators. Authors specify noncommercial research use.
- [DeepfakeGenome](https://arxiv.org/abs/2611.06046) (2026‑11‑04) · About two million images from 100 facial forgery methods, including retrieval-based attribution evaluation. [Data](https://huggingface.co/datasets/DeepfakeGenome/DeepfakeGenome) and [training/testing code](https://huggingface.co/DeepfakeGenome/DeepfakeGenome_Codebase) are published; some source data must be obtained separately from FF++/DF40, with source-specific restrictions.
- [WildFakeToolBench](https://github.com/TrustAIRLab/WildFakeToolBench) ([paper](https://arxiv.org/abs/2610.31152) 10‑22; code released 10‑28) · 156 image-processing tools for robustness tests under real-world post-processing. Authors restrict use to academic purposes.
- [WildAIGC-Bench V3](https://github.com/YuZijian/WildAIGC-Bench) (updated 2026‑11‑03) · 600 AI-labeled images and 638 real-labeled photos with source/evidence records. Review the labels and evidence supplied with the [samples](https://huggingface.co/datasets/yuzj1997yzj/WildAIGC-Bench) before evaluation.

### Current multimodal backbones for new experiments

The following Qwen variants support visual inputs. Input modalities and licenses vary by checkpoint.

- [Qwen3.5](https://github.com/QwenLM/Qwen3.8#qwen35), especially [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) · Native image/video understanding; 9B is a compact open-weight candidate for local tool-using agents.
- [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) · Open-weight image/video-capable MoE with 35B total / 3B active parameters and preserved reasoning context for iterative agent workflows.
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) · Newer open-weight native VLM for image/video understanding and multi-step agent tasks; Apache-2.0.
- [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) ([weights](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)) · Open-weight multimodal MoE architecture preview with image/video support; Qwen Community 1.0 license.

### System-1 fast decision and perception models

“System-1” here covers direct structured decisions and candidate ranking. These general-purpose perception/decision resources need task-specific calibration and evaluation for forensic use.

- [Liquid d1](https://www.liquid.ai/blog/lfm3) · The 2026‑10‑27 release adds open-weight [d1-2B](https://huggingface.co/LiquidAI/d1-2B) (text/image/video) and [d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B) (adds audio), with weights and inference code. [d1-ultra](https://www.liquid.ai/blog/d1-ultra) provides text/image decisions via API; earlier [d1-3B](https://huggingface.co/LiquidAI/d1-3B) and experimental [d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) remain comparison options. Open weights use LFM Open License v1.0 with commercial-revenue restrictions.
- [Cloudflare Clef](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/) · [Clef](https://huggingface.co/Cloudflare/clef) / [Clef-flash](https://huggingface.co/Cloudflare/clef-flash) make structured decisions over text, images and video; [Clef-omni](https://huggingface.co/Cloudflare/clef-omni) adds audio. Apache-2.0 weights and hosted Workers AI access; multimodal release updated 2026‑10‑09.
- [pplx-decider-v1.2](https://huggingface.co/perplexity-ai/pplx-decider-v1.2) · Perplexity's Qwen3.8-27B-based text/image decision model with parallel question-marker readout. Questions can attend to one another. The model card lists Apache-2.0 weights and inference code and describes private access.
- [MetaEncoder-30B](https://huggingface.co/facebook/meta-encoder) · Cacheable text/image/video task and candidate embeddings for direct candidate ranking; [evaluation code](https://github.com/facebook/meta-encoder-eval) is available. Released weights require gated access and acceptance of model terms. Video uses the native implementation; the vLLM adapter supports text/image inputs. Calibrate similarity scores for the target task.
- [Intern-Decision](https://github.com/InternLM/Intern-Decision) · Text plus optional images → multiple typed JSON decisions in one forward pass; [4B weights](https://huggingface.co/internlm/Intern-Decision-4B), alongside 0.8B/2B variants. Code and weights use Apache-2.0.
- [Valen](https://github.com/Valen-Team/Valen) · Shared-state text/image/sampled-video decisions with 0.8B/2B/[4B weights](https://huggingface.co/Valen-Team/Valen-4B), Apache-2.0, and local ONNX/GGUF options. Local video uses 16 sampled frames; the free web chat uses one middle frame. The SystemOne and Decisions APIs support up to eight questions and one image per request.
- [TypeSafe Jev](https://docs.typesafe.ai/models) · Hosted structured-decision API: as of 2026‑11‑08, jev-latest and jev-preview both resolve to 1.14.0. [Image input](https://docs.typesafe.ai/images) and [Box localization](https://docs.typesafe.ai/primitives/box) remain experimental.

### Backbones used by listed papers

- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) · Vision-language family with image/video reasoning and grounding; includes the 4B and 8B variants used by several listed methods.
- [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) · Image/video understanding backbone used by ForenAgent, ARGUS and MM-VeriAgent. UniShield uses the Qwen2.5-VL family.
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) · Text reasoning model used in AgentFoX's agent-guided evidence fusion.
- [Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) · Text, image, audio and video understanding backbone used by FakeHunter and BAEA.
- [Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B) · ToolDF's audio tool-use backbone, adapted with LoRA SFT.
- [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) · Omni-modal model supporting vision, audio and language; an alternative backbone evaluated by FakeHunter.

### Proprietary model services

- [OpenAI API models](https://developers.openai.com/api/docs/models) · Official model catalogue for the GPT-family services used in several listed methods; check the paper's exact model or snapshot when reproducing results.
- [Google Gemini API](https://ai.google.dev/gemini-api/docs/models) · Official multimodal model catalogue and API documentation, including the Gemini family used by SafeGuard.
- [Qwen3.8-Omni-Flash](https://qwen.ai/blog?id=qwen3.8-omni-flash) · Hosted native omnimodal model with text, image, audio and video inputs, tool calling and long-context audio-visual reasoning.

### Agent frameworks and tool execution

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) · Stateful workflow orchestration with persistence and human review, suitable for multi-step evidence gathering and arbitration.
- [Pydantic AI](https://pydantic.dev/docs/ai/overview/) · Python agent framework with typed tools, structured outputs and dependency injection for explicit detector interfaces.
- [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) · Programmatic coding-agent sessions for code-based experiments and integration with research workflows.
- [OpenHands Software Agent SDK](https://docs.openhands.dev/sdk) · Custom agents with shell, file, browser and MCP tools, plus local and remote execution options.
- [Pi](https://pi.dev/docs/latest/sdk) · Embeddable coding-agent SDK with configurable sessions and extensible tools for custom execution workflows.
- [reflex](https://github.com/kshetrajna12/reflex) · Structured visual-judgment execution with shared-prefix caching and isolated batched questions, using frozen Qwen3.5-4B by default.

<a name="link-checks"></a>

## Link checks

The [link-audit workflow](.github/workflows/link-audit.yml) runs Mondays at 06:23 UTC, on relevant updates to main, and manually in GitHub Actions. Reports record redirect chains and destinations, with separate results for HTTP 404/410, access restrictions, transient errors and local file/anchor issues for human review. See the [link-audit guide](scripts/LINK_AUDIT.md) for usage and report details.
