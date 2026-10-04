# Contributing

Thank you for helping make agentic AIGC detection easier to navigate. A useful contribution can be as small as one corrected link or a clearer explanation of one inference step.

## Propose a paper or correction

Open an issue or pull request with:

1. **Paper:** title, stable primary-source link, and the version you read.
2. **Task scope:** generated image/video detection, or a clearly identified related task such as local editing, face manipulation, audio manipulation, or factual verification.
3. **Inference mechanism:** what is observed, which decision follows, and what action can change. Note fixed tool calls and stopping conditions when relevant.
4. **Evidence:** the supporting section, figure, algorithm, or short source passage. Paraphrase in the README; do not copy abstracts.
5. **Suggested placement:** feedback-loop, related-forensics, or bounded-workflow group. Explain uncertainty rather than forcing a label.

Example submission:

- Paper and version: …
- Scope: …
- Observed evidence → next decision → possible action: …
- Evidence location: §… / Fig. … / Algorithm …
- What remains fixed or unclear: …
- Proposed one-sentence entry: …

## Editorial principles

- Describe the mechanism, not the marketing label. Tool use, multiple agents, and chain-of-thought do not by themselves prove adaptive evidence acquisition.
- Separate training-time search, reward computation, and data generation from test-time actions.
- Distinguish conditional verification and profile lookup from repeated tool selection after new observations.
- Treat categories as navigation aids, not quality tiers. Corrections can change placement without implying that a method is better or worse.
- Prefer primary papers and official project links. Check that code belongs to the listed paper before adding a repository link.
- Do not add unsupported “first,” “best,” or exhaustive-coverage claims. We do not require benchmarks, rankings, or experiment reruns.
- Keep entries short and neutral. If a claim is disputed, cite the relevant paper version and evidence; unresolved mechanisms can remain in Further reading.
- Keep README.md and README_CN.md aligned where practical. A contribution in either language is welcome; flag any translation still needed.

## Before submitting

- [ ] The paper is not already listed under another title or framework name.
- [ ] The primary link opens and the title/version match.
- [ ] Scope and inference behavior are supported by a specific source location.
- [ ] Training behavior is not presented as inference behavior.
- [ ] The change contains no unsupported performance claim.
- [ ] Both language versions are updated, or the missing translation is noted.

Please submit links and original summaries rather than uploading third-party papers or copyrighted figures. Paper and code licenses remain those of their respective owners.
