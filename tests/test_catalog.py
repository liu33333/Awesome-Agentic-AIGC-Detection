"""Keep the bilingual paper catalog structurally consistent."""
import html
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODALITIES = ('audio', 'visual', 'text', 'cross-modal')


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
                    self.assertEqual(section.count('<th '), 4)
                    self.assertEqual(section.count('<th width="50%"'), 1)
                    self.assertTrue(rows)
                    dates = []
                    for key, cells in rows:
                        all_keys.append(key)
                        self.assertEqual(len(cells), 4, key)
                        self.assertRegex(cells[0], r'</strong>.*?<br><sub>.+</sub>$', key)
                        self.assertNotIn('&nbsp;', cells[1], key)
                        dates.append(re.search(r'\d{2}/\d{2}', cells[1])[0])
                    self.assertEqual(dates, sorted(dates, reverse=True))
            self.assertEqual(len(all_keys), len(set(all_keys)))

    def test_bilingual_rows_dates_tags_and_resource_links(self):
        en_text, en = catalog('README.md')
        cn_text, cn = catalog('README_CN.md')
        for modality in MODALITIES:
            en_rows, cn_rows = en[modality][1], cn[modality][1]
            self.assertEqual([k for k, _ in en_rows], [k for k, _ in cn_rows])
            for (key, a), (_, b) in zip(en_rows, cn_rows):
                with self.subTest(paper=key):
                    self.assertEqual(visible(a[0].split('<br><sub>', 1)[0]),
                                     visible(b[0].split('<br><sub>', 1)[0]))
                    self.assertEqual(re.findall(r'\d{2}/\d{2}', a[1]),
                                     re.findall(r'\d{2}/\d{2}', b[1]))
                    self.assertEqual(re.findall(r'<code>(.*?)</code>', a[2]),
                                     re.findall(r'<code>(.*?)</code>', b[2]))
                    self.assertEqual(re.findall(r'href="([^"]+)"', a[3]),
                                     re.findall(r'href="([^"]+)"', b[3]))
        external = lambda s: set(re.findall(r'https?://[^\s<>"\)]+', s))
        self.assertEqual(external(en_text), external(cn_text))

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
                    resource = cells[3]
                    self.assertNotEqual(visible(resource), '—', key)
                    self.assertFalse(re.search(r'<(?:sub|small|strong|b)>\s*(?:\+\s*|＋)?(?:Weights|权重)', resource, re.I), key)
                    if re.search(r'>Weights</a>|>权重</a>', resource):
                        self.assertNotIn('style=', resource, key)


if __name__ == '__main__':
    unittest.main()
