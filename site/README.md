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

The design uses a restrained paper-and-forest palette, an original media-evidence illustration, full-width paper titles, peer-level resource links and a compact filter rail that becomes a mobile filter panel. Actual reference pages inspected during design were [Nerfies](https://nerfies.github.io/) for research-page hierarchy and whitespace, and [AwesomeCUA](https://awesomecua.com/) for catalogue search and metadata organization. No template code or artwork was copied.

Before deployment, check English/Chinese pages, 320px and 390px phone layouts, keyboard focus, empty state/reset, every modality, task/training intersections, both sorts, URL restoration, language-switch state and primary source links. Source-link tests cover the built HTML paths and fragments. Existing repository link audits check the upstream paper/resource URLs separately.
