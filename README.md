![Agentic AIGC Detection: layered landscape image frames, a highlighted scan region, and a magnified detail connected by evidence lines.](assets/banner.svg)

**English** · [简体中文](README_CN.md)

[Intro](#intro) · [News](#news) · [Audio](#audio) · [Visual (images & videos)](#visual) · [Text](#text) · [Cross-modal](#cross-modal) · **[Technical comparison →](docs/COMPARISON.md)** · [Surveys](#surveys) · [Resources](#resources)

<a name="intro"></a>

## Intro

A collection of research on agentic detection of AI-generated content and related media manipulation. The focus is on methods that use tools, evidence-guided reasoning or multi-agent collaboration to investigate authenticity. Papers are grouped by input modality, with publication information and the availability of official implementations. Related fixed-tool and rule-orchestrated methods are explicitly separated for comparison.

Models refer to forensic inference. Catalog labels omit the -Instruct suffix; exact variants, tool training, calibration and retrieval memory are detailed in [Inference setups](docs/COMPARISON.md#inference-setups).

Training describes forensic-agent adaptation: Training-free, SFT (supervised fine-tuning), or RL (reinforcement learning). “Not reported” means agent adaptation is unspecified, not that its tools are untrained.

<a name="news"></a>

## News

- **2026‑11‑08**: Added audio and cross-modal tool reasoning plus FACT; separated fixed multi-agent and rule-based workflows, added forensic models/benchmarks, and updated d1/Jev. Distinguished historical omissions, revisions and new releases; synchronized bilingual comparisons.
- **2026‑10‑23**: Added Qwen–LangGraph text detection and two explicitly separated related tool-grounded/rule-orchestrated methods; updated comparisons, added an agent-evaluation survey, refreshed Qwen/System-1 model resources and audited code status.
- **2026‑10‑04**: Added the [technical comparison](docs/COMPARISON.md), covering five method-level dimensions.
- **2026‑10‑04**: Launched the Agentic AIGC Detection reading list.

<a name="audio"></a>

## Audio

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

**[View technical comparison →](docs/COMPARISON.md#audio)**

<table>
<thead>
<tr>
<th width="400" align="left">Paper<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">Venue</th>
<th width="64" align="left">Date</th>
<th width="70" align="left">Tags</th>
<th width="180" align="left">Model / Training</th>
<th width="85" align="left">Code</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="tooldf"></a><strong><a href="https://aclanthology.org/2026.findings-emnlp.842/">ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection</a></strong></td>
<td width="115" valign="top">Findings&nbsp;EMNLP<br>2026</td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>A</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑Omni‑3B<br><sub>SFT</sub></td>
<td width="85" valign="top"><a href="https://github.com/rlataewoo/tooldf">Code</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="sear"></a><strong><a href="https://arxiv.org/abs/2609.39847">SEAR: Spoofing Evidence-Grounded Audio Reasoning Benchmark for Audio Language Models</a></strong> (BAEA)</td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>A</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑Omni‑7B<br><sub>Training-free</sub></td>
<td width="85" valign="top"><a href="https://github.com/SEAR-benchmark/SEAR">Code</a></td>
</tr>
</tbody>
</table>

BAEA-Adaptive selects acoustic feature groups within a budget; BAEA-Fixed is deterministic and performs better in the paper. [SEAR annotations](https://huggingface.co/datasets/SEAR-benchmark/SEAR) exclude raw audio. ToolDF provides code and audio-reconstruction scripts; files behind its author-provided weight link were not independently verified.

<a name="visual"></a>

## Visual (images & videos)

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

**[View technical comparison →](docs/COMPARISON.md#visual)**

<table>
<thead>
<tr>
<th width="400" align="left">Paper<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">Venue</th>
<th width="64" align="left">Date</th>
<th width="70" align="left">Tags</th>
<th width="180" align="left">Model / Training</th>
<th width="85" align="left">Code</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="atar"></a><strong><a href="https://arxiv.org/abs/2609.39066">Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection</a></strong> (ATAR)</td>
<td width="115" valign="top">ACM&nbsp;MM&nbsp;2026<br><sub>Oral · accepted</sub></td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="forenagent"></a><strong><a href="https://arxiv.org/abs/2512.16300">Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection</a></strong> (ForenAgent)</td>
<td width="115" valign="top">ECCV&nbsp;2026</td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top"><a href="https://github.com/zfr00/ForenAgent">Toolkit</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="safeguard"></a><strong><a href="https://arxiv.org/abs/2607.03069">SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection</a></strong></td>
<td width="115" valign="top">ECCV&nbsp;2026</td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">GPT‑4o<br>+ Gemini‑2.5‑Pro<br><sub>Training-free · tools tuned</sub></td>
<td width="85" valign="top"><a href="https://github.com/williamw99/SafeGuard">Pending</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="fact"></a><strong><a href="https://arxiv.org/abs/2609.05876">FACT: A Forensic Agent with Compiled Tool-Use Trajectories for AI-Generated Image Detection</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="defake-o3"></a><strong><a href="https://arxiv.org/abs/2608.16259">Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection</a></strong></td>
<td width="115" valign="top">ACM&nbsp;MM&nbsp;2026<br><sub>accepted</sub></td>
<td width="64" valign="top">26/08</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="hermes"></a><strong><a href="https://proceedings.mlr.press/v306/li26be.html">Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection</a></strong></td>
<td width="115" valign="top">ICML&nbsp;2026</td>
<td width="64" valign="top">26/07</td>
<td width="70" valign="top"><code>V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br>+ ChatGPT‑5<br><sub>Training-free</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="unishield"></a><strong><a href="https://arxiv.org/abs/2510.03161">UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization</a></strong></td>
<td width="115" valign="top">CVPR&nbsp;Findings<br>2026</td>
<td width="64" valign="top">26/06</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑VL<br>+ GPT‑4o<br><sub>RL (router) · tools tuned</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="agentfox"></a><strong><a href="https://arxiv.org/abs/2603.23115">AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/03</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑32B<br>+ GPT‑4o<br><sub>Training-free · calibration</sub></td>
<td width="85" valign="top"><a href="https://github.com/suncore946/AgentFoX">Minimal</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="evoguard"></a><strong><a href="https://arxiv.org/abs/2603.17343">EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/03</td>
<td width="70" valign="top"><code>I</code><br><code>D</code></td>
<td width="180" valign="top">Qwen3‑VL‑4B<br><sub>RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="forgeryvcr"></a><strong><a href="https://arxiv.org/abs/2602.14098">ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization</a></strong></td>
<td width="115" valign="top">ACM&nbsp;MM&nbsp;2026<br><sub>Oral · accepted</sub></td>
<td width="64" valign="top">26/02</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code></td>
<td width="180" valign="top">Qwen3‑VL‑4B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top"><a href="https://github.com/youqiwong/ForgeryVCR">Code<br><sub>+ weights</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="aifo"></a><strong><a href="https://arxiv.org/abs/2511.00181">From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection</a></strong> (AIFo)</td>
<td width="115" valign="top">arXiv&nbsp;2025<br><sub>preprint</sub></td>
<td width="64" valign="top">25/10</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">GPT‑4o<br><sub>Training-free</sub></td>
<td width="85" valign="top">—</td>
</tr>
</tbody>
</table>

### Related fixed-tool and multi-agent workflows

These use preset detector pools, fixed roles, debate rounds or retrieval pipelines. Evidence arbitration and training-time self-improvement do not imply autonomous tool selection at inference. ForeAgent is distinct from ForenAgent above.

**[View technical comparison →](docs/COMPARISON.md#related-visual)**

<table>
<thead>
<tr>
<th width="400" align="left">Paper<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">Venue</th>
<th width="64" align="left">Date</th>
<th width="70" align="left">Tags</th>
<th width="180" align="left">Model / Training</th>
<th width="85" align="left">Code</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="dissecting-agentic-forensics"></a><strong><a href="https://arxiv.org/abs/2609.24359">Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection</a></strong></td>
<td width="115" valign="top">ECCV&nbsp;2026<br><sub>AI4MFDD Workshop</sub></td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Gemma‑4‑26B‑A4B‑it<br>+ GPT‑5<br><sub>Training-free · score calibration</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="pate-forensics"></a><strong><a href="https://arxiv.org/abs/2608.18573">PATE-Forensics: Perception-as-Tool for Explainable Deepfake Forensics with General-Purpose MLLMs</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>DDL-X challenge report</sub></td>
<td width="64" valign="top">26/08</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3.5‑Flash<br><sub>Training-free · tool trained</sub></td>
<td width="85" valign="top"><a href="https://github.com/yqli00000/CLASP">Code<br><sub>now CLASP</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="argus"></a><strong><a href="https://arxiv.org/abs/2608.06865">Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection</a></strong> (ARGUS)</td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/08</td>
<td width="70" valign="top"><code>V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑VL‑7B<br><sub>SFT + RL · fixed 4+1 roles</sub></td>
<td width="85" valign="top"><a href="https://github.com/XavierJiezou/ARGUS">Code<br><sub>+ weights</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="foreagent"></a><strong><a href="https://arxiv.org/abs/2606.26552">Perception, Verdict, and Evolution: Hindsight-Driven Self-Refining Forensics Agent for AI-Generated Image Detection</a></strong> (ForeAgent)</td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/06</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT · training-time refinement</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="vrag-dfd"></a><strong><a href="https://arxiv.org/abs/2604.13660">VRAG-DFD: Verifiable Retrieval-Augmentation for MLLM-based Deepfake Detection</a></strong></td>
<td width="115" valign="top">CVPR&nbsp;Findings<br>2026</td>
<td width="64" valign="top">26/06</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">MLLM<br><sub>exact size unverified</sub><br><sub>SFT + RL · fixed RAG</sub></td>
<td width="85" valign="top"><a href="https://github.com/abigcatcat/VRAG-DFD">Code<br><sub>+ weights</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="dvar"></a><strong><a href="https://arxiv.org/abs/2604.16987">DVAR: Adversarial Multi-Agent Debate for Video Authenticity Detection</a></strong></td>
<td width="115" valign="top">ACM&nbsp;MM&nbsp;2026<br><sub>author-reported</sub></td>
<td width="64" valign="top">26/04<br><sub>preprint</sub></td>
<td width="70" valign="top"><code>V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">GPT‑5.4<br><sub>Training-free · fixed debate</sub></td>
<td width="85" valign="top">—</td>
</tr>
</tbody>
</table>

Dissecting's workshop acceptance is author-reported; the table shows its hybrid configuration. DVAR's venue is paper-reported and its DOI remains independently unverified; no official code or knowledge-base download was found. Files at ForeAgent's [author-provided weight link](https://huggingface.co/Shimin/qwen3_vl_8b_foreagent) were not verified.

<a name="text"></a>

## Text

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

**[View technical comparison →](docs/COMPARISON.md#text)**

<table>
<thead>
<tr>
<th width="400" align="left">Paper<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">Venue</th>
<th width="64" align="left">Date</th>
<th width="70" align="left">Tags</th>
<th width="180" align="left">Model / Training</th>
<th width="85" align="left">Code</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="qwen-langgraph"></a><strong><a href="https://link.springer.com/article/10.1007/s10791-026-10710-z">Performance evaluation and interpretability of a Qwen LangGraph agent for AI written and AI rewritten text detection</a></strong></td>
<td width="115" valign="top">Discover<br>Computing&nbsp;2026</td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>T</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑1.5B<br><sub>Not reported · tools trained</sub></td>
<td width="85" valign="top"><a href="https://drive.google.com/drive/folders/14wU4r0-uRirkJ9aP3xI1lj2yHfWkj7DQ">Author link<br><sub>not verified</sub></a></td>
</tr>
</tbody>
</table>

### Related tool-augmented multi-role workflow

Detection and search modules run separately, with fixed exact-to-fuzzy search fallback and webpage evidence aggregation; this is not an unconstrained tool planner.

**[View technical comparison →](docs/COMPARISON.md#related-text)**

<table>
<thead>
<tr>
<th width="400" align="left">Paper<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">Venue</th>
<th width="64" align="left">Date</th>
<th width="70" align="left">Tags</th>
<th width="180" align="left">Model / Training</th>
<th width="85" align="left">Code</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="aigt-agent"></a><strong><a href="https://aclanthology.org/2026.findings-emnlp.272/">Beyond Text-Intrinsic Features: An Agentic Framework for Evidence-Based AI-Generated Text Detection</a></strong> (AIGT-Agent)</td>
<td width="115" valign="top">Findings&nbsp;EMNLP<br>2026</td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>T</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">GPT‑5‑mini<br><sub>Training-free · prompt adaptation</sub></td>
<td width="85" valign="top"><a href="https://github.com/TrustAIRLab/AIGT-Agent">Code<br><sub>+ benchmark</sub></a></td>
</tr>
</tbody>
</table>

<a name="cross-modal"></a>

## Cross-modal

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

**[View technical comparison →](docs/COMPARISON.md#cross-modal)**

<table>
<thead>
<tr>
<th width="400" align="left">Paper<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">Venue</th>
<th width="64" align="left">Date</th>
<th width="70" align="left">Tags</th>
<th width="180" align="left">Model / Training</th>
<th width="85" align="left">Code</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="mm-veriagent"></a><strong><a href="https://arxiv.org/abs/2609.30698">MM-VeriAgent: Learning to Use Extensive Tools to Verify Multimodal Misinformation with Reinforcement Learning</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/09<br><sub>v2 26/11</sub></td>
<td width="70" valign="top"><code>T+I</code><br><code>D</code></td>
<td width="180" valign="top">Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="omnivl-guard-pro"></a><strong><a href="https://arxiv.org/abs/2605.16962">OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/05</td>
<td width="70" valign="top"><code>T+I</code>&nbsp;/&nbsp;<code>T+V</code><br><code>D</code>&nbsp;<code>L</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top"><a href="https://github.com/shen8424/OmniVL-Guard-Pro">Pending</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="fakehunter"></a><strong><a href="https://arxiv.org/abs/2508.14581">Memory-Anchored Multimodal Reasoning for Explainable Video Forensics</a></strong> (FakeHunter)</td>
<td width="115" valign="top">arXiv&nbsp;2025<br><sub>preprint</sub></td>
<td width="64" valign="top">25/08</td>
<td width="70" valign="top"><code>A+V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑Omni‑7B<br><sub>alt. MiniCPM‑o‑2_6</sub><br><sub>Training-free · fitted memory</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="t2agent"></a><strong><a href="https://arxiv.org/abs/2505.19768">T²Agent: A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search</a></strong></td>
<td width="115" valign="top">AAAI&nbsp;2026<br><sub>Oral</sub></td>
<td width="64" valign="top">25/05<br><sub>preprint</sub></td>
<td width="70" valign="top"><code>T+I</code><br><code>D</code></td>
<td width="180" valign="top">GPT‑4o<br><sub>Training-free</sub></td>
<td width="85" valign="top"><a href="https://github.com/cuixing100876/T2Agent">Code<br><sub>partly cached</sub></a></td>
</tr>
</tbody>
</table>

MM-VeriAgent and T²Agent address broader image–text misinformation, including generated/manipulated images, rather than only AIGC provenance. T²Agent's implementation partly reads precomputed tool results and its example backend differs from the main paper; end-to-end reproduction was not verified.

### Related rule-orchestrated methods

These escalate detection through fixed thresholds or deterministic state machines, without an autonomous LLM action policy. ENF presence alone does not prove authenticity; authentication requires consistency with trusted independent reference evidence.

**[View technical comparison →](docs/COMPARISON.md#related-cross-modal)**

<table>
<thead>
<tr>
<th width="400" align="left">Paper<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">Venue</th>
<th width="64" align="left">Date</th>
<th width="70" align="left">Tags</th>
<th width="180" align="left">Model / Training</th>
<th width="85" align="left">Code</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="adaptive-multi-agent"></a><strong><a href="https://doi.org/10.3390/informatics13100163">A Multi-Agent Framework with Adaptive Orchestration for Explainable Multi-Modal Deepfake Detection</a></strong></td>
<td width="115" valign="top">Informatics&nbsp;2026</td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>A+V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Llama‑3‑70B<br>+ Gemini‑1.5‑Flash<br><sub>Rule-based · detectors trained</sub></td>
<td width="85" valign="top"><a href="https://github.com/saoirsebarry/multiagent-deepfake-detection">Code<br><sub>+ weights</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="enf-framework"></a><strong><a href="https://arxiv.org/abs/2610.22440">An Agentic ENF Framework for Forensic Video Authentication Against Generative AI</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>preprint</sub></td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>A+V</code><br><code>D</code></td>
<td width="180" valign="top">Deterministic state machine<br><sub>Rule-based · detectors trained</sub></td>
<td width="85" valign="top"><a href="https://github.com/RyanSolent95/enf-video-forensics">Code<br><sub>+ weights</sub></a></td>
</tr>
</tbody>
</table>

### Pending further verification

- [FALCON: LLM as a forensic reasoner: Expert-guided video deepfake detection across modalities](https://doi.org/10.1016/j.patcog.2026.115240) · Pattern Recognition, online 2026‑10‑29. The abstract describes expert-extracted cross-modal evidence passed to an LLM; full-text access was restricted. Exact models, training, code and autonomy remain unverified, so no detailed comparison is included.

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

Current model candidates are separated from paper-specific reproduction backbones; inclusion is not evidence of validated forensic performance. New/updated entries checked: 2026‑11‑08; other entries retain the 2026‑10‑23 check. Visible public files do not imply full downloads or successful reproduction.

### Agentic forensic platforms

- [Resemble Investigator](https://docs.resemble.ai/detect/agents) · **Managed API.** Media-authenticity investigations with streamed evidence and assessments; requires an account with Investigator access.
- [Clyravision](https://en.merantix-momentum.com/clyravision) · **Contact-based platform.** Agent-based image analysis combining forensic traces, metadata and source/context checks; the product page includes a recorded demonstration.

### Detection services for agent tools

- [Reality Defender RealAPI](https://www.realitydefender.com/product/realapi) · **Detection API.** Image, audio and video manipulation analysis with structured results for integration into an agent's evidence pipeline.
- [Sightengine](https://www.sightengine.com/docs/ai-generated-image-detection) · **Detection API.** AI-generated image scoring, with separate deepfake and AI-video detection models documented alongside it.

### Specialized forensic models

- [VeriSpoof](https://arxiv.org/abs/2611.04634) (2026‑11‑03) · Qwen3-ASR-1.7B encoder plus MiniCPM5-2B for audio detection, attribution, recording conditions, segment localization and source verification, with checkable explanations. [Inference code](https://github.com/swagshaw/verispoof) and [Plus weights](https://huggingface.co/AustinXiao/VeriSpoof-Plus) are available; training code is pending. Code/weights use CC BY-NC 4.0. This is a specialized model, not an autonomous tool-selection loop.
- [Venus-DefakerOne2](https://arxiv.org/abs/2610.37918) (2026‑10‑27; revised 11‑02) · Qwen3.5-2B image/video forensic expert with fixed real/fake question answering. [Weights](https://huggingface.co/qcf568/DefakerOne2) and [inference helper scripts](https://github.com/inclusionAI/DefakerOne2) are available, not a complete training release. Use preview for paper reproduction; release uses more training data. Weight/data licensing details still need confirmation.

### Datasets and benchmarks

- [SEAR](https://huggingface.co/datasets/SEAR-benchmark/SEAR) · Audio QA annotations for verdicts, cues, numerical measurements and forensic rationales, with [BAEA/evaluation code](https://github.com/SEAR-benchmark/SEAR). Obtain ASVspoof raw audio separately.
- [VeriSpoof-Bench](https://huggingface.co/datasets/AustinXiao/VeriSpoof-Bench) · Labels, manifests, metadata and reconstruction materials for 54 subsets / 177,852 items; not all raw audio. Source-corpus licenses still apply.
- [RRVBench](https://www.modelscope.cn/models/DanceText/RRVBench) · DefakerOne2 video benchmark with 1,319 real and 11,000 synthetic videos from 11 generators. Authors specify noncommercial research use; full download access and license terms were not independently verified.
- [DeepfakeGenome](https://arxiv.org/abs/2611.06046) (2026‑11‑04) · About two million images from 100 facial forgery methods, including retrieval-based attribution evaluation. [Data](https://huggingface.co/datasets/DeepfakeGenome/DeepfakeGenome) and [training/testing code](https://huggingface.co/DeepfakeGenome/DeepfakeGenome_Codebase) are published; some source data must be obtained separately from FF++/DF40, with source-specific restrictions.
- [WildFakeToolBench](https://github.com/TrustAIRLab/WildFakeToolBench) ([paper](https://arxiv.org/abs/2610.31152) 10‑22; code released 10‑28) · 156 image-processing tools for robustness tests under real-world post-processing. Not a detection agent; excludes complete test images, detector weights and intermediate collection artifacts. Authors restrict use to academic purposes.
- [WildAIGC-Bench V3](https://github.com/YuZijian/WildAIGC-Bench) (updated 2026‑11‑03) · 600 AI images and 638 real photos with source/evidence records. **Challenge set requiring review, not an unquestioned gold standard:** some AI-labeled [samples](https://huggingface.co/datasets/yuzj1997yzj/WildAIGC-Bench) retain evidence notes that ground truth awaits manual verification, including img_00e970e187abfbf5, img_024f0544ed6ff0f5 and img_02760ab536eb47cc. Review labels/evidence before evaluation.

### Current multimodal backbones for new experiments

These Qwen variants support vision without a separate “-VL” suffix. Input modalities and licenses still vary by checkpoint; do not assume every later Qwen release is multimodal.

- [Qwen3.5](https://github.com/QwenLM/Qwen3.8#qwen35), especially [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) · Native image/video understanding; 9B is a compact open-weight candidate for local tool-using agents.
- [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) · Open-weight image/video-capable MoE with 35B total / 3B active parameters and preserved reasoning context for iterative agent workflows.
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) · Newer open-weight native VLM for image/video understanding and multi-step agent tasks; Apache-2.0.
- [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) ([weights](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)) · Open-weight multimodal MoE architecture preview with image/video support; Qwen Community 1.0 license, not Apache-2.0.

### System-1 fast decision and perception models

“System-1” here covers direct structured decisions and candidate ranking, not a single architecture or only the Jev ecosystem. These are general-purpose perception/decision resources, not validated forensic detectors; scores need task-specific calibration, and parallel questions do not imply constant latency.

- [Liquid d1](https://www.liquid.ai/blog/lfm3) · The 2026‑10‑27 release adds open-weight [d1-2B](https://huggingface.co/LiquidAI/d1-2B) (text/image/video) and [d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B) (adds audio), with visible weight/inference files; long speech and some languages remain limitations. [d1-ultra](https://www.liquid.ai/blog/d1-ultra) provides text/image decisions via API; earlier [d1-3B](https://huggingface.co/LiquidAI/d1-3B) and experimental [d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) remain comparison options. Open weights use LFM Open License v1.0 with commercial-revenue restrictions; these are not forensic-specialist models.
- [Cloudflare Clef](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/) · [Clef](https://huggingface.co/Cloudflare/clef) / [Clef-flash](https://huggingface.co/Cloudflare/clef-flash) make structured decisions over text, images and video; [Clef-omni](https://huggingface.co/Cloudflare/clef-omni) adds audio. Apache-2.0 weights and hosted Workers AI access; multimodal release updated 2026‑10‑09.
- [pplx-decider-v1.2](https://huggingface.co/perplexity-ai/pplx-decider-v1.2) · Perplexity's Qwen3.8-27B-based text/image decision model with parallel question-marker readout. Questions can attend to one another, rather than operating independently. Apache-2.0 weight files and inference code are listed, but download access was not verified because the model card retains private-access instructions.
- [MetaEncoder-30B](https://huggingface.co/facebook/meta-encoder) · Cacheable text/image/video task and candidate embeddings for direct candidate ranking; [evaluation code](https://github.com/facebook/meta-encoder-eval) is available. Released weights require gated access and acceptance of model terms. Video uses the native implementation, not the text/image-only vLLM adapter; similarities are not automatically calibrated probabilities.
- [Intern-Decision](https://github.com/InternLM/Intern-Decision) · Text plus optional images → multiple typed JSON decisions in one forward pass; [4B weights](https://huggingface.co/internlm/Intern-Decision-4B), alongside 0.8B/2B variants. Apache-2.0 code/weights are released; training data and private calibration records are not fully public.
- [Valen](https://github.com/Valen-Team/Valen) · Shared-state text/image/sampled-video decisions with 0.8B/2B/[4B weights](https://huggingface.co/Valen-Team/Valen-4B), Apache-2.0, and local ONNX/GGUF options. Local video uses 16 sampled frames; the free web chat uses one middle frame and the free API is single-question, so demo capabilities differ from local models.
- [TypeSafe Jev](https://docs.typesafe.ai/models) · Hosted structured-decision API: as of 2026‑11‑08, jev-latest and jev-preview both resolve to 1.14.0, with no separate preview version. [Image input](https://docs.typesafe.ai/images) and [Box localization](https://docs.typesafe.ai/primitives/box) remain experimental. No open weights or validated forensic performance are claimed.

### Backbones used by listed papers

- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) · Vision-language family with image/video reasoning and grounding; includes the 4B and 8B variants used by several listed methods.
- [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) · Image/video understanding backbone used by ForenAgent, ARGUS and MM-VeriAgent; UniShield uses the Qwen2.5-VL family without a reported parameter size.
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) · Text reasoning model used in AgentFoX's agent-guided evidence fusion.
- [Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) · Text, image, audio and video understanding backbone used by FakeHunter and BAEA.
- [Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B) · ToolDF's audio tool-use backbone, adapted with LoRA SFT.
- [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) · Omni-modal model supporting vision, audio and language; an alternative backbone evaluated by FakeHunter.

### Proprietary model services

- [OpenAI API models](https://developers.openai.com/api/docs/models) · Official model catalogue for the GPT-family services used in several listed methods; check the paper's exact model or snapshot when reproducing results.
- [Google Gemini API](https://ai.google.dev/gemini-api/docs/models) · Official multimodal model catalogue and API documentation, including the Gemini family used by SafeGuard.
- [Qwen3.8-Omni-Flash](https://qwen.ai/blog?id=qwen3.8-omni-flash) · Hosted native omnimodal model with text, image, audio and video inputs, tool calling and long-context audio-visual reasoning; not listed as open weights.

### Agent frameworks and tool execution

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) · Stateful workflow orchestration with persistence and human review, suitable for multi-step evidence gathering and arbitration.
- [Pydantic AI](https://pydantic.dev/docs/ai/overview/) · Python agent framework with typed tools, structured outputs and dependency injection for explicit detector interfaces.
- [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) · Programmatic coding-agent sessions for code-based experiments and integration with research workflows.
- [OpenHands Software Agent SDK](https://docs.openhands.dev/sdk) · Custom agents with shell, file, browser and MCP tools, plus local and remote execution options.
- [Pi](https://pi.dev/docs/latest/sdk) · Embeddable coding-agent SDK with configurable sessions and extensible tools for custom execution workflows.
- [reflex](https://github.com/kshetrajna12/reflex) · Structured visual-judgment execution with shared-prefix caching and isolated batched questions, using frozen Qwen3.5-4B by default. The current stable release is a framework, not a newly fine-tuned checkpoint.
