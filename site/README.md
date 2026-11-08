# Research website

A static, bilingual GitHub Pages catalogue with keyword search, modality/task/training filters, shareable filter URLs, and source-backed sorting. Full titles, model details, workflow notes and official resource links remain readable without JavaScript.

## One source of truth

- Edit paper content in the five-column modality tables in `README.md` and `README_CN.md`.
- Keep the existing `data/catalog-order.json` aligned with those rows. It contains only source-backed sorting dates and their basis, not a second paper catalogue.
- `scripts/build_site.py` parses those sources into static English and Chinese HTML plus a machine-readable `catalog.json`. No paper records are maintained by hand in `site/`.
- A changed source produces a changed SHA-256 fingerprint in the generated HTML and JSON. The builder checks bilingual identities, input/task tags, resource URLs, dates and completeness, and fails on mismatches rather than silently dropping papers.
- `Training-free`, `SFT` and `RL` filters come from the English agent-training labels. SFT + RL papers match both filters. Tool-only training and memory construction do not imply agent SFT/RL; other or empty labels use “Other / not stated.”

## Build and test

Python 3.12 and Node.js are sufficient. There are no production dependencies, external fonts, analytics or runtime API requests.

```sh
python -m unittest discover -s tests -v
python scripts/build_site.py
node --check site/assets/app.js
node tests/site_filter_test.js _site/catalog.json
python -m http.server 8000 --directory _site
```

Open `http://localhost:8000` for English and `/zh/` for Chinese. `_site/` is build output and is intentionally not committed.

## Deployment

In repository **Settings → Pages → Build and deployment**, set **Source** to **GitHub Actions**. The `pages.yml` workflow tests, builds and deploys on relevant pushes to `main`. Pull requests run tests without publishing. A failed build does not replace the previous deployment.

The English and Chinese READMEs link to the website near the top. GitHub Pages hosts the public site at `https://liu33333.github.io/Awesome-Agentic-AIGC-Detection/`.

## Design and browser checks

The design is a paper-first reading interface: a compact introduction, one sans-serif type family, readable 15px filter options, a quiet white/gray palette with a burgundy accent, and full-width paper titles. The large illustrated landing-page hero and ornamental statistics have been removed. Paper metadata, model/training details, workflow notes and resource links remain visible without expanding cards.

Actual reference pages visually inspected for this redesign were [alphaXiv](https://www.alphaxiv.org/) and [Semantic Scholar search](https://www.semanticscholar.org/search?q=agentic%20deepfake%20detection&sort=relevance). Their paper-first hierarchy, accessible search and restrained metadata informed the layout. No template code, branding or artwork was copied. On mobile, search remains above a collapsible filter panel; filter selections and result counts stay visible through the filter count and URL. Without JavaScript, all paper records and the expanded controls remain in the page.
Before deployment, check English/Chinese pages, 320px and 390px phone layouts, keyboard focus, empty state/reset, every modality, task/training intersections, both sorts, URL restoration, language-switch state and primary source links. Source-link tests cover the built HTML paths and fragments. Existing repository link audits check the upstream paper/resource URLs separately.
