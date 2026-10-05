![Agentic AIGC Detection: layered landscape image frames, a highlighted scan region, and a magnified detail connected by evidence lines.](assets/banner.svg)

**English** · [简体中文](README_CN.md)

[Intro](#intro) · [News](#news) · [Audio](#audio) · [Visual (images & videos)](#visual) · [Text](#text) · [Cross-modal](#cross-modal) · **[Technical comparison →](docs/COMPARISON.md)** · [Resources](#resources)

<a name="intro"></a>

## Intro

A collection of research on agentic detection of AI-generated content and related media manipulation. The focus is on methods that use tools, evidence-guided reasoning or multi-agent collaboration to investigate authenticity. Papers are grouped by input modality, with publication information and the availability of official implementations.

Models refer to forensic inference. Catalog labels omit the -Instruct suffix; exact variants, tool training, calibration and retrieval memory are detailed in [Inference setups](docs/COMPARISON.md#inference-setups).

Training describes forensic-agent adaptation: Training-free, SFT (supervised fine-tuning), or RL (reinforcement learning).

<a name="news"></a>

## News

- **2026‑10‑04**: Added the [technical comparison](docs/COMPARISON.md), covering five method-level dimensions.
- **2026‑10‑04**: Launched the Agentic AIGC Detection reading list.

<a name="audio"></a>

## Audio

No papers listed.

<a name="visual"></a>

## Visual (images & videos)

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

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

<a name="text"></a>

## Text

No papers listed.

<a name="cross-modal"></a>

## Cross-modal

Input: <code>I</code> Image · <code>V</code> Video · <code>A</code> Audio · <code>T</code> Text<br>Task: <code>D</code> Detection · <code>L</code> Localization · <code>E</code> Explanation

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
</tbody>
</table>

<a name="resources"></a>

## Resources

Selected platforms, model backbones and development tools for agentic media-forensics research. Check access requirements, model versions and data-handling terms before use.

### Agentic forensic platforms

- [Resemble Detect Agents](https://docs.resemble.ai/detect/agents) · **Managed API.** Media-authenticity investigations with streamed evidence and assessments; requires an account with Detect Agents access.
- [Clyravision](https://en.merantix-momentum.com/clyravision) · **Contact-based platform.** Agent-based image analysis combining forensic traces, metadata and source/context checks; the product page includes a recorded demonstration.

### Detection services for agent tools

- [Reality Defender RealAPI](https://www.realitydefender.com/product/realapi) · **Detection API.** Image, audio and video manipulation analysis with structured results for integration into an agent's evidence pipeline.
- [Sightengine](https://www.sightengine.com/docs/ai-generated-image-detection) · **Detection API.** AI-generated image scoring, with separate deepfake and AI-video detection models documented alongside it.

### Open-weight model backbones

- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) · Vision-language family with image/video reasoning and grounding; includes the 4B and 8B variants used by several listed methods.
- [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) · Image/video understanding backbone from the Qwen2.5-VL family used by ForenAgent and UniShield.
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) · Text reasoning model used in AgentFoX's agent-guided evidence fusion.
- [Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) · Text, image, audio and video understanding backbone used by FakeHunter.
- [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) · Omni-modal model supporting vision, audio and language; an alternative backbone evaluated by FakeHunter.

### Proprietary model services

- [OpenAI API models](https://developers.openai.com/api/docs/models) · Official model catalogue for the GPT-family services used in several listed methods; check the paper's exact model or snapshot when reproducing results.
- [Google Gemini API](https://ai.google.dev/gemini-api/docs/models) · Official multimodal model catalogue and API documentation, including the Gemini family used by SafeGuard.

### Agent frameworks and tool execution

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) · Stateful workflow orchestration with persistence and human review, suitable for multi-step evidence gathering and arbitration.
- [Pydantic AI](https://pydantic.dev/docs/ai/overview/) · Python agent framework with typed tools, structured outputs and dependency injection for explicit detector interfaces.
- [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) · Programmatic coding-agent sessions for code-based experiments and integration with research workflows.
- [OpenHands Software Agent SDK](https://docs.openhands.dev/sdk) · Custom agents with shell, file, browser and MCP tools, plus local and remote execution options.
- [Pi](https://pi.dev/docs/latest/sdk) · Embeddable coding-agent SDK with configurable sessions and extensible tools for custom execution workflows.



