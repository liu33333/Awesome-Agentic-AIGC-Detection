"""The website must be a faithful, deterministic view of the README catalogue."""
import copy
import hashlib
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_site', ROOT / 'scripts/build_site.py')
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)

class Elements(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.articles = []
        self.scripts = []
    def handle_starttag(self, tag, pairs):
        a = dict(pairs)
        if 'id' in a: self.ids.append(a['id'])
        for key in ('href', 'src'):
            if key in a: self.links.append(a[key])
        if tag == 'article': self.articles.append(a)
        if tag == 'script': self.scripts.append(a)

class WebsiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = site.load_catalog()

    def test_all_papers_match_source_order_and_exact_titles(self):
        for lang in ('en', 'zh'):
            page = site.render(self.catalog, lang)
            parser = Elements(); parser.feed(page)
            source = self.catalog['papers'][lang]
            self.assertEqual([p['id'] for p in source], [a['id'] for a in parser.articles])
            self.assertEqual([p['title'] for p in source], [a['data-title'] for a in parser.articles])
            self.assertEqual(len(parser.ids), len(set(parser.ids)))
            for p in source:
                self.assertIn(site.escape(p['workflow']), page)
                for resource in p['resources']:
                    self.assertIn(site.escape(resource['url']), page)

    def test_paper_first_layout_and_accessible_mobile_controls(self):
        for lang in ('en', 'zh'):
            page = site.render(self.catalog, lang)
            self.assertNotIn('class="hero-art"', page)
            self.assertNotIn('Follow the evidence', page)
            self.assertIn('aria-controls="filter-controls"', page)
            self.assertIn('id="toggle-filters"', page)
            self.assertIn('aria-expanded="false"', page)
            self.assertIn('id="active-filter-count"', page)
            self.assertIn('id="apply-filters"', page)
            self.assertLess(page.index('id="search"'), page.index('id="filter-panel"'))
            self.assertIn('id="library-title"', page)
            for asset in ('style.css', 'app.js', 'favicon.svg'):
                digest = hashlib.sha256((ROOT/'site/assets'/asset).read_bytes()).hexdigest()[:12]
                self.assertIn(f'assets/{asset}?v={digest}', page)

    def test_source_training_classification_does_not_infer_tool_training(self):
        self.assertEqual(site.training_tags('Training-free · tools tuned'), ['training-free'])
        self.assertEqual(site.training_tags('SFT + RL'), ['sft', 'rl'])
        self.assertEqual(site.training_tags('RL (router) · tools tuned'), ['rl'])
        self.assertEqual(site.training_tags('Tools trained'), ['other'])
        self.assertEqual(site.training_tags(''), ['other'])
        self.assertEqual(site.training_tags('K-means memory'), ['other'])

    def test_models_keep_alternative_variants(self):
        paper = next(p for p in self.catalog['papers']['en'] if p['id'] == 'fakehunter')
        self.assertIn('MiniCPM-o-2_6', paper['model'])
        self.assertEqual(paper['training'], 'K-means memory')

    def test_bilingual_filter_identity(self):
        for en, zh in zip(self.catalog['papers']['en'], self.catalog['papers']['zh']):
            for key in ('id', 'title', 'url', 'modality', 'tasks', 'inputs', 'training_tags', 'sort_date', 'order'):
                self.assertEqual(en[key], zh[key], (en['id'], key))

    def test_expected_modality_counts_and_no_omissions(self):
        from collections import Counter
        counts = Counter(p['modality'] for p in self.catalog['papers']['en'])
        self.assertEqual(set(counts), set(site.GROUPS))
        self.assertTrue(all(count > 0 for count in counts.values()))
        expected = json.loads((ROOT / 'data/catalog-order.json').read_text())['papers']
        self.assertEqual(self.catalog['count'], len(expected))

    def test_build_is_deterministic_and_all_internal_links_exist(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            site.build(a); site.build(b)
            for rel in ('index.html', 'zh/index.html', 'catalog.json', 'assets/app.js', 'assets/style.css', 'assets/evidence.svg'):
                self.assertEqual((Path(a)/rel).read_bytes(), (Path(b)/rel).read_bytes())
            for rel in ('index.html', 'zh/index.html'):
                p = Path(a)/rel
                parser=Elements(); parser.feed(p.read_text())
                for link in parser.links:
                    parts=urlsplit(link)
                    if parts.scheme or parts.netloc: continue
                    target = (p.parent / unquote(parts.path)).resolve() if parts.path else p
                    if target.is_dir(): target /= 'index.html'
                    self.assertTrue(target.is_file(), (rel,link))
                    if parts.fragment:
                        dest=Elements(); dest.feed(target.read_text())
                        self.assertIn(parts.fragment, dest.ids, (rel,link))
                self.assertEqual(len(parser.scripts), 1)
                self.assertIn('defer', parser.scripts[0])

    def test_script_and_markup_are_escaped(self):
        catalog=copy.deepcopy(self.catalog)
        catalog['papers']['en'][0]['title']='<script>alert("x")</script>'
        page=site.render(catalog, 'en')
        self.assertNotIn('<script>alert', page)
        self.assertIn('&lt;script&gt;', page)
        for bad in ('javascript:alert(1)', '//example.com', 'data:text/html,test'):
            with self.assertRaises(ValueError): site.safe_url(bad)

    def test_source_changes_rebuild_content_and_fingerprint(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'data').mkdir()
            for name in ('README.md', 'README_CN.md', 'data/catalog-order.json'):
                (root/name).write_bytes((ROOT/name).read_bytes())
            original=site.load_catalog(root)
            readme=root/'README.md'
            readme.write_text(readme.read_text().replace(original['papers']['en'][0]['workflow'], 'Updated workflow from source.', 1))
            changed=site.load_catalog(root)
            self.assertNotEqual(original['source_sha256'], changed['source_sha256'])
            self.assertEqual(changed['papers']['en'][0]['workflow'], 'Updated workflow from source.')
            self.assertIn('Updated workflow from source.', site.render(changed, 'en'))

    def test_missing_ordering_record_fails_instead_of_silently_dropping_paper(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'data').mkdir()
            for name in ('README.md', 'README_CN.md'):
                (root/name).write_bytes((ROOT/name).read_bytes())
            order=json.loads((ROOT/'data/catalog-order.json').read_text())
            order['papers'].pop()
            (root/'data/catalog-order.json').write_text(json.dumps(order))
            with self.assertRaises(ValueError): site.load_catalog(root)

    def test_all_outbound_paper_resources_are_from_readme(self):
        for lang, file in [('en','README.md'), ('zh','README_CN.md')]:
            raw=(ROOT/file).read_text()
            for p in self.catalog['papers'][lang]:
                self.assertIn(p['url'], raw)
                for r in p['resources']: self.assertIn(r['url'],raw)

if __name__ == '__main__': unittest.main()
