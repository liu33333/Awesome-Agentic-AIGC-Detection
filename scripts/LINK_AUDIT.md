# Link audit

Run `python scripts/audit_links.py` with Python 3.12 (standard library only).
It checks `README.md`, `README_CN.md`, and every `docs/**/*.md`, including HTML
href/src, Markdown inline/image/reference-definition links and angle autolinks.
Code blocks and comments are excluded. Reference definitions are checked even
when unused; bare prose URLs are not links. This is a focused extractor, not a
complete CommonMark renderer. Prefer explicit HTML anchors for complex headings.
Use `--local-only` for an offline file/anchor check; use `--output DIR` to place
reports outside the default `link-audit` directory.

The workflow runs Mondays at 06:23 UTC, through Actions → Link audit → Run
workflow, and on pushes to `main` that change either README, `docs/**/*.md`,
`scripts/audit_links.py`, `tests/**`, or `.github/workflows/link-audit.yml`.
Scheduled runs require this workflow on the default branch. No issues,
PRs, edits, or messages are automatically created. Inspect the job summary and
30-day JSON/Markdown artifacts. A moved repository can still return 200, and a
redirect can lead to a login or unrelated landing page: review every redirect
chain and destination before changing links. External fragments and semantic
page identity are not validated. Local files and Markdown anchors are checked.

Classification:

- `ok`: HTTP 2xx, or an existing local target with its Markdown anchor.
- `redirected`: HTTP 2xx after redirects, with every hop preserved for review.
- `http_not_found`: GET returned 404/410. This is evidence for human review,
  not proof of permanent removal: GitHub/Hugging Face and other hosts may hide
  private or inaccessible resources behind these responses.
- `broken`: missing local file or missing local Markdown anchor only.
- `restricted`: 401/403/407/429/451. Never equated with a broken link.
- `unverified`: DNS/TLS/timeout/network failures, 5xx, other ambiguous statuses,
  redirect loops/limits, unsafe destinations, or unchecked non-Markdown anchors.
- `skipped`: non-HTTP schemes, or external links in local-only mode.

HEAD 400/404/405/410/501 responses are rechecked with GET. Access restrictions
and 429 responses do not trigger an immediate GET. GET bodies are not downloaded.
Transient failures retry up to twice with backoff. Numeric and HTTP-date
Retry-After headers are honored: up to 30 seconds is waited, and larger values
defer checking to another run. Active 429/503 cooldowns also defer other URLs
on the same hostname, rather than bypassing the requested wait. Redirects to
apparent login or homepage paths are flagged for review, without fetching bodies;
this heuristic cannot establish that other landing pages contain intended content. Four workers
operate with per-host serialized requests and a 0.5-second pause. Each request
has a 12-second socket timeout, redirects have a ten-hop bound, and the workflow
has a 30-minute deadline. Network/DNS timing can still exceed socket timeouts.
Only public HTTP(S) destinations without embedded credentials are requested;
private/reserved addresses and HTTPS downgrades are not followed. DNS checks
reduce accidental private requests, but are not a hardened DNS-rebinding sandbox.
Do not run this checker against untrusted inputs with privileged network access.

The audit is deliberately report-only: broken or uncertain findings do not fail
the job. Checker test failures and execution errors do fail it. A canceled or
timed-out run is incomplete, never a clean result. The JSON includes all results,
source file/line references, response status and redirect chains. Test locally
with `python -m unittest discover -s tests -v`; fixtures do not require Internet.
