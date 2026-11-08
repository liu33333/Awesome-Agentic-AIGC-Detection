"""Keep the bilingual paper catalog structurally consistent."""
from datetime import date
import html
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODALITIES = ('audio', 'visual', 'text', 'cross-modal')
SORT_DATA = json.loads((ROOT / 'data/catalog-order.json').read_text(encoding='utf-8'))
SORT_KEYS = {paper['id']: paper for paper in SORT_DATA['papers']}


def catalog(filename):
    text = (ROOT / filename).read_text(encoding='utf-8')
    groups = {}
    for modality, following in zip(MODALITIES, (*MODALITIES[1:], 'surveys')):
        section = text.split(f'<a name="{modality}"></a>', 1)[1].split(
            f'<a name="{following}"></a>', 1)[0]
        rows = []
        for row in re.findall(r'<tr>.*?</tr>', section, re.S):
            cells = re.findall(r'<td\b[^>]*>(.*?)</td>', row, re.S)
            if cells:
                key = re.search(r'<a name="([^"]+)"', cells[0])[1]
                rows.append((key, cells))
        groups[modality] = (section, rows)
    return text, groups


def visible(text):
    return html.unescape(re.sub(r'<[^>]+>', '', text)).strip()


class CatalogTests(unittest.TestCase):
    def test_four_modalities_one_table_each(self):
        for filename in ('README.md', 'README_CN.md'):
            _, groups = catalog(filename)
            all_keys = []
            for modality, (section, rows) in groups.items():
                with self.subTest(file=filename, modality=modality):
                    self.assertEqual(section.count('<table>'), 1)
                    self.assertFalse(re.search(r'^###\s', section, re.M))
                    self.assertEqual(section.count('<th '), 5)
                    self.assertEqual(section.count('<th width="34%"'), 1)
                    self.assertRegex(section, r'>Workflow</th>|>流程</th>')
                    self.assertTrue(rows)
                    dates = []
                    for key, cells in rows:
                        all_keys.append(key)
                        self.assertEqual(len(cells), 5, key)
                        self.assertRegex(cells[0], r'</strong>.*?<br><code>', key)
                        self.assertTrue(visible(cells[3]), key)
                        self.assertNotIn('<details', cells[3], key)
                        self.assertNotRegex(cells[1], r'<(?:sub|small|strong|b)[ >]', key)
                        self.assertNotRegex(' '.join(cells), r'\b\d{2}/\d{2}\b', key)
                        self.assertNotIn('&nbsp;', cells[1], key)
                        dates.append(date.fromisoformat(SORT_KEYS[key]['date']))
                    self.assertEqual(dates, sorted(dates, reverse=True))
            self.assertEqual(len(all_keys), len(set(all_keys)))
            self.assertEqual(set(all_keys), set(SORT_KEYS))

    def test_modality_legends_show_only_their_relevant_inputs(self):
        expected = {'audio': ['A'], 'visual': ['I', 'V'],
                    'text': ['T'], 'cross-modal': ['I', 'V', 'A', 'T']}
        for filename in ('README.md', 'README_CN.md'):
            _, groups = catalog(filename)
            for modality, (section, rows) in groups.items():
                with self.subTest(file=filename, modality=modality):
                    prefix = section.split('<table>', 1)[0]
                    input_legend = re.search(r'(?:Input:|输入：)(.*?)<br>', prefix)[1]
                    self.assertEqual(re.findall(r'<code>(.*?)</code>', input_legend),
                                     expected[modality])
                    # Actual paper tags remain explicit, not filled from the heading.
                    for key, cells in rows:
                        tags = re.findall(r'<code>(.*?)</code>', cells[0])
                        inputs = [tag for tag in tags if tag not in {'D', 'L', 'E'}]
                        self.assertTrue(inputs, key)
                        self.assertTrue(all(set(tag.split('+')) <= set(expected[modality])
                                            for tag in inputs), key)

    def test_bilingual_rows_dates_tags_and_resource_links(self):
        en_text, en = catalog('README.md')
        cn_text, cn = catalog('README_CN.md')
        for modality in MODALITIES:
            en_rows, cn_rows = en[modality][1], cn[modality][1]
            self.assertEqual([k for k, _ in en_rows], [k for k, _ in cn_rows])
            for (key, a), (_, b) in zip(en_rows, cn_rows):
                with self.subTest(paper=key):
                    self.assertEqual(visible(a[0]), visible(b[0]))
                    self.assertEqual(re.findall(r'<code>(.*?)</code>', a[0]),
                                     re.findall(r'<code>(.*?)</code>', b[0]))
                    self.assertEqual(re.findall(r'href="([^"]+)"', a[4]),
                                     re.findall(r'href="([^"]+)"', b[4]))
        external = lambda s: set(re.findall(r'https?://[^\s<>"\)]+', s))
        self.assertEqual(external(en_text), external(cn_text))

    def test_sort_metadata_is_complete_and_sourced(self):
        self.assertEqual(len(SORT_KEYS), len(SORT_DATA['papers']))
        for key, item in SORT_KEYS.items():
            with self.subTest(paper=key):
                date.fromisoformat(item['date'])
                self.assertIn(item['basis'], {'conference', 'preprint', 'journal'})
                self.assertTrue(item['source'].startswith('https://'))

    def test_resource_labels_are_standardized_and_bilingually_equivalent(self):
        translation = {'Code': '代码', 'Dataset': '数据集',
                       'Weights': '权重', 'Project Page': '项目主页'}
        _, en = catalog('README.md')
        _, cn = catalog('README_CN.md')
        for modality in MODALITIES:
            for (key, a), (_, b) in zip(en[modality][1], cn[modality][1]):
                with self.subTest(paper=key):
                    labels = lambda cell: [visible(label) for label in re.findall(
                        r'<a\b[^>]*href="[^"]+"[^>]*>(.*?)</a>', cell, re.S)]
                    en_labels, cn_labels = labels(a[4]), labels(b[4])
                    self.assertTrue(all(label in translation for label in en_labels))
                    self.assertEqual([translation[label] for label in en_labels], cn_labels)
                    # An announcement-only repository is not released source code.
                    if key in {'safeguard', 'omnivl-guard-pro'}:
                        self.assertEqual(en_labels, ['Project Page'])
                    # The paper's Data/Code availability sections cite the same folder.
                    if key == 'qwen-langgraph':
                        self.assertEqual(en_labels, ['Code', 'Dataset'])
                        urls = re.findall(r'href="([^"]+)"', a[4])
                        self.assertEqual(urls[0], urls[1])

    def test_comparisons_cover_catalog_in_the_same_order(self):
        for cn in (False, True):
            readme = 'README_CN.md' if cn else 'README.md'
            doc = 'docs/COMPARISON_CN.md' if cn else 'docs/COMPARISON.md'
            _, groups = catalog(readme)
            expected = [key for _, rows in groups.values() for key, _ in rows]
            text = (ROOT / doc).read_text(encoding='utf-8')
            sections = text.split('<a name="agent-workflows"></a>')
            self.assertEqual(len(sections), 2)
            for index, section in enumerate(sections):
                rows = [line for line in section.splitlines() if line.startswith('| **[')]
                keys = [re.search(r'README(?:_CN)?\.md#([^)]*)', line)[1] for line in rows]
                self.assertEqual(keys, expected)
                self.assertEqual(len(re.findall(r'^###\s', section, re.M)), 4)
                self.assertTrue(all(len(line.strip('|').split('|')) == 5 + index for line in rows))

    def test_unknowns_are_blank_and_parallel_resources_are_peers(self):
        prohibited = re.compile(r'not verified|not reported|not found|not located|unverified|unspecified|未核验|未报告|未找到|待发布', re.I)
        for filename in ('README.md', 'README_CN.md', 'docs/COMPARISON.md', 'docs/COMPARISON_CN.md'):
            text = (ROOT / filename).read_text(encoding='utf-8')
            self.assertIsNone(prohibited.search(visible(text)), filename)
        for filename in ('README.md', 'README_CN.md'):
            _, groups = catalog(filename)
            for _, rows in groups.values():
                for key, cells in rows:
                    resource = cells[4]
                    self.assertNotEqual(visible(resource), '—', key)
                    self.assertFalse(re.search(r'<(?:sub|small|strong|b)>\s*(?:\+\s*|＋)?(?:Weights|权重)', resource, re.I), key)
                    if re.search(r'>Weights</a>|>权重</a>', resource):
                        self.assertNotIn('style=', resource, key)


if __name__ == '__main__':
    unittest.main()
