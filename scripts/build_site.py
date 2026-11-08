#!/usr/bin/env python3
"""Build the public catalogue from the bilingual READMEs. Standard library only.

README tables are the source of titles, models, workflows, labels, and links.
The existing catalog-order.json supplies ordering only. No paper data is
hand-maintained in site/. The build fails rather than silently losing a row.
"""
import argparse
from collections import Counter
from datetime import date
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/liu33333/Awesome-Agentic-AIGC-Detection'
GROUPS = ('audio', 'visual', 'text', 'cross-modal')
LABELS = {
    'en': {
        'lang': 'en', 'other_lang': '简体中文', 'other_url': 'zh/',
        'kicker': 'Research library', 'title': 'Agentic AIGC Detection',
        'description': 'Research on detecting, localizing and explaining AI-generated content with agents, tools and multi-agent systems.',
        'browse': 'Explore papers', 'comparison': 'Technical comparison', 'repo': 'GitHub repository',
        'papers': 'Papers', 'modalities': 'Modalities', 'tasks': 'Tasks', 'collection': 'The research library',
        'subtitle': 'Browse papers', 'search': 'Search papers',
        'placeholder': 'Search titles, models, workflows…', 'filter': 'Filters', 'show_results': 'Show papers',
        'modality': 'Input modality', 'all': 'All modalities', 'audio': 'Audio', 'visual': 'Visual', 'text': 'Text', 'cross-modal': 'Cross-modal',
        'visual_hint': 'Images & videos', 'task': 'Task', 'training': 'Agent training',
        'all_tasks': 'All tasks', 'all_training': 'All training', 'D': 'Detection', 'L': 'Localization', 'E': 'Explanation',
        'training-free': 'Training-free', 'sft': 'SFT', 'rl': 'RL', 'other': 'Other / not stated',
        'training_note': 'Training refers to forensic-agent adaptation. Tool training, calibration and memory are shown separately in each paper.',
        'reset': 'Reset filters', 'sort': 'Sort papers', 'catalog': 'Catalogue order', 'newest': 'Newest first', 'az': 'Title A–Z',
        'results': 'papers', 'model': 'Model / training', 'workflow': 'Workflow', 'paper': 'Paper', 'source': 'README',
        'empty': 'No papers match these filters.', 'empty_hint': 'Try another keyword or reset the filters.',
        'notes': 'How to read this collection', 'scope_title': 'Scope, not a leaderboard',
        'scope': 'The collection includes agentic forensic methods and related tool-grounded or rule-orchestrated workflows. Inclusion does not imply equal autonomy or evaluation settings.',
        'order_title': 'A consistent reading order', 'order': 'Within each modality, papers follow conference opening dates, first arXiv releases or first online journal publication. Dates are used for sorting, not repeated beside venues.',
        'source_title': 'One source, always in sync', 'source_text': 'Every paper, model, workflow and resource link is generated from the repository README. Updating the source rebuilds this website automatically.',
        'resources': 'Keep exploring', 'survey': 'Related surveys', 'survey_hint': 'Agent foundations, detection and evaluation.',
        'resources_title': 'Models & benchmarks', 'resources_hint': 'Forensic models, datasets and evaluation resources.',
        'compare_hint': 'Compare inference setups, tool use and agent workflows.', 'contribute': 'Suggest a paper or correction',
        'footer': 'A community reading list for evidence-guided media forensics.', 'sync': 'Generated from README',
        'diagram': 'Conceptual illustration of media signals, forensic tools and an evidence trail. Not a detector result.',
        'legend': 'Input tags: I image · V video · A audio · T text', 'skip': 'Skip to papers',
        'nojs': 'All papers are readable below. Enable JavaScript to use search and filters.',
    },
    'zh': {
        'lang': 'zh-CN', 'other_lang': 'English', 'other_url': '../',
        'kicker': '开放论文库', 'title': 'Agentic AIGC Detection',
        'description': '汇集通过智能体、工具调用与多智能体协作，对 AI 生成内容进行检测、定位与解释的研究。',
        'browse': '浏览论文', 'comparison': '技术对比', 'repo': 'GitHub 仓库',
        'papers': '篇论文', 'modalities': '种输入模态', 'tasks': '类任务', 'collection': '论文目录',
        'subtitle': '浏览论文', 'search': '搜索论文',
        'placeholder': '搜索标题、模型、工作流程…', 'filter': '筛选论文', 'show_results': '查看论文',
        'modality': '输入模态', 'all': '全部模态', 'audio': '音频', 'visual': '视觉', 'text': '文本', 'cross-modal': '跨模态',
        'visual_hint': '图像与视频', 'task': '任务', 'training': '智能体训练',
        'all_tasks': '全部任务', 'all_training': '全部训练方式', 'D': '检测', 'L': '定位', 'E': '解释',
        'training-free': '免训练', 'sft': 'SFT · 监督微调', 'rl': 'RL · 强化学习', 'other': '其他 / 未注明',
        'training_note': '训练方式指鉴伪智能体的任务适配。工具训练、校准与记忆构建在各论文中单独说明。',
        'reset': '重置筛选', 'sort': '论文排序', 'catalog': '目录顺序', 'newest': '时间倒序', 'az': '标题 A–Z',
        'results': '篇论文', 'model': '模型 / 训练', 'workflow': '工作流程', 'paper': '论文', 'source': 'README 条目',
        'empty': '没有符合筛选条件的论文。', 'empty_hint': '试试其他关键词，或重置筛选。',
        'notes': '阅读说明', 'scope_title': '文献目录，而非排行榜',
        'scope': '收录智能体鉴伪方法，也包含相关的工具增强与规则编排流程。收录不代表各方法具有相同自主性或评测设置。',
        'order_title': '清晰一致的阅读顺序', 'order': '各模态内按会议开幕日、首次 arXiv 发布日或期刊首次在线发表日排序。日期仅用于排序，不在发表信息旁重复展示。',
        'source_title': '同一份来源，自动同步', 'source_text': '每篇论文、模型、工作流程与资源链接均由仓库 README 自动生成。更新来源后，网站会自动重新构建。',
        'resources': '继续探索', 'survey': '相关综述', 'survey_hint': '智能体基础、内容检测与评测综述。',
        'resources_title': '模型与基准', 'resources_hint': '专用取证模型、数据集及评测资源。',
        'compare_hint': '比较推理配置、工具使用与智能体工作流程。', 'contribute': '推荐论文或提交更正',
        'footer': '面向证据驱动媒体鉴伪的开放阅读清单。', 'sync': '由 README 自动生成',
        'diagram': '媒体信号、取证工具与证据链的概念示意图，并非实际检测结果。',
        'legend': '输入标签：I 图像 · V 视频 · A 音频 · T 文本', 'skip': '跳转到论文',
        'nojs': '以下全部论文无需 JavaScript 即可阅读。搜索与筛选需要启用 JavaScript。',
    },
}

def text(value):
    value = re.sub(r'<br\s*/?>', ' ', value, flags=re.I)
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', '', value)).split())


def safe_url(value):
    value = html.unescape(value)
    parts = urlsplit(value)
    if parts.scheme not in ('https', 'http') or not parts.netloc:
        raise ValueError(f'Expected an external HTTP(S) URL: {value}')
    return value


def links(value):
    return [{'url': safe_url(url), 'label': text(label)} for url, label in
            re.findall(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', value, re.S)]


def parse_readme(content):
    result = []
    for group, following in zip(GROUPS, (*GROUPS[1:], 'surveys')):
        section = content.split(f'<a name="{group}"></a>', 1)[1].split(f'<a name="{following}"></a>', 1)[0]
        for row in re.findall(r'<tr>.*?</tr>', section, re.S):
            cells = re.findall(r'<td\b[^>]*>(.*?)</td>', row, re.S)
            if not cells:
                continue
            if len(cells) != 5:
                raise ValueError(f'{group}: expected five README columns, found {len(cells)}')
            key = re.search(r'<a name="([^"]+)"', cells[0])[1]
            title_part = re.split(r'<br\s*/?>', cells[0], maxsplit=1)[0]
            paper_link = links(title_part)
            if len(paper_link) != 1:
                raise ValueError(f'{key}: expected one paper link')
            tags = re.findall(r'<code>(.*?)</code>', cells[0])
            if not tags or any(t not in ('D', 'L', 'E') for t in tags[1:] if '+' not in t):
                raise ValueError(f'{key}: malformed input/task tags: {tags}')
            tasks = [t for t in tags if t in ('D', 'L', 'E')]
            inputs = [t for t in tags if t not in ('D', 'L', 'E')]
            if not tasks or not inputs:
                raise ValueError(f'{key}: missing input/task tags')
            subs = re.findall(r'<sub>(.*?)</sub>', cells[2], re.S)
            models = text(re.sub(r'<sub>.*?</sub>', '', cells[2], flags=re.S)).strip()
            alternatives = [text(s) for s in subs if text(s).startswith(('alt.', '备选'))]
            training = ' · '.join(text(s) for s in subs if not text(s).startswith(('alt.', '备选')))
            if alternatives:
                models += ' · ' + ' · '.join(alternatives)
            resource_links = links(cells[4])
            note = text(re.sub(r'<a\b[^>]*>.*?</a>', '', cells[4], flags=re.S))
            result.append({'id': key, 'modality': group, 'title': text(title_part),
                           'url': paper_link[0]['url'], 'inputs': inputs, 'tasks': tasks,
                           'venue': text(cells[1]), 'model': models, 'training': training,
                           'workflow': text(cells[3]), 'resources': resource_links, 'resource_note': note})
    if not result or len({p['id'] for p in result}) != len(result):
        raise ValueError('Empty catalogue or duplicate paper ids')
    return result


def training_tags(value):
    tags = []
    if 'training-free' in value.lower(): tags.append('training-free')
    if re.search(r'\bSFT\b', value): tags.append('sft')
    if re.search(r'\bRL\b', value): tags.append('rl')
    return tags or ['other']


def load_catalog(root=ROOT):
    sources = {lang: (root / filename).read_text(encoding='utf-8')
               for lang, filename in [('en', 'README.md'), ('zh', 'README_CN.md')]}
    parsed = {lang: parse_readme(value) for lang, value in sources.items()}
    keys = [p['id'] for p in parsed['en']]
    if keys != [p['id'] for p in parsed['zh']]:
        raise ValueError('Bilingual README paper order differs')
    order_source = (root / 'data/catalog-order.json').read_text(encoding='utf-8')
    ordering = json.loads(order_source)['papers']
    order = {p['id']: p for p in ordering}
    if len(order) != len(ordering) or set(keys) != set(order):
        raise ValueError('README and catalog-order.json paper ids differ')
    for index, (en, zh) in enumerate(zip(parsed['en'], parsed['zh'])):
        for field in ('title', 'url', 'inputs', 'tasks'):
            if en[field] != zh[field]:
                raise ValueError(f'{en["id"]}: bilingual {field} differs')
        if [r['url'] for r in en['resources']] != [r['url'] for r in zh['resources']]:
            raise ValueError(f'{en["id"]}: bilingual resource links differ')
        date.fromisoformat(order[en['id']]['date'])
        for paper in (en, zh):
            paper.update({'sort_date': order[en['id']]['date'], 'sort_basis': order[en['id']]['basis'],
                          'order': index, 'training_tags': training_tags(en['training'])})
    digest = hashlib.sha256(('\n'.join(sources.values()) + order_source).encode()).hexdigest()
    return {'papers': parsed, 'source_sha256': digest, 'count': len(keys)}


def escape(value):
    return html.escape(str(value), quote=True)


def card(paper, labels, readme):
    e = escape
    searchable = ' '.join([paper['id'], paper['title'], paper['venue'], paper['model'], paper['training'], paper['workflow'], paper['modality'], labels[paper['modality']], *paper['inputs'], *(labels[t] for t in paper['tasks'])])
    task_tags = ''.join(f'<span class="task-tag">{labels[t]}</span>' for t in paper['tasks'])
    input_tags = ' / '.join(paper['inputs'])
    model = f'<p class="model">{e(paper["model"])}</p>' if paper['model'] else ''
    training = f'<p class="training">{e(paper["training"])}</p>' if paper['training'] else ''
    modelblock = f'<div class="paper-model"><span class="field-label">{labels["model"]}</span>{model}{training}</div>' if model or training else ''
    resource_links = ''.join(f'<a href="{e(r["url"])}">{e(r["label"])}</a>' for r in paper['resources'])
    resource_note = f'<span class="resource-note">{e(paper["resource_note"])}</span>' if paper['resource_note'] else ''
    return f'''<article class="paper-card" id="{e(paper['id'])}" data-modality="{paper['modality']}" data-tasks="{' '.join(paper['tasks'])}" data-training="{' '.join(paper['training_tags'])}" data-order="{paper['order']}" data-date="{paper['sort_date']}" data-title="{e(paper['title'])}" data-search="{e(searchable)}">
      <div class="paper-topline"><span class="modality-mark {paper['modality']}">{labels[paper['modality']]}</span><span class="venue">{e(paper['venue'])}</span></div>
      <h3><a href="{e(paper['url'])}">{e(paper['title'])}</a></h3>
      <div class="paper-tags"><span class="input-tag" title="{e(labels['legend'])}">{e(input_tags)}</span><span class="tag-divider" aria-hidden="true"></span>{task_tags}</div>
      <div class="paper-details">{modelblock}<div class="paper-workflow"><span class="field-label">{labels['workflow']}</span><p>{e(paper['workflow'])}</p></div></div>
      <div class="paper-links"><a class="paper-link" href="{e(paper['url'])}">{labels['paper']} <span aria-hidden="true">↗</span></a>{resource_links}{resource_note}<a class="source-link" href="{REPO}/blob/main/{readme}#{paper['id']}" aria-label="{labels['source']}: {e(paper['title'])}">↗ <span>{labels['source']}</span></a></div>
    </article>'''


def render(catalog, lang):
    l = LABELS[lang]
    papers = catalog['papers'][lang]
    counts = Counter(p['modality'] for p in papers)
    prefix = '../' if lang == 'zh' else ''
    readme = 'README_CN.md' if lang == 'zh' else 'README.md'
    comparison = 'COMPARISON_CN.md' if lang == 'zh' else 'COMPARISON.md'
    readme_url = f'{REPO}/blob/main/{readme}'
    comparison_url = f'{REPO}/blob/main/docs/{comparison}'
    filters = ''.join(f'<button type="button" class="modality-button" data-modality="{g}" aria-pressed="false"><span>{l[g]}</span><span class="filter-count">{counts[g]}</span></button>' for g in GROUPS)
    cards = '\n'.join(card(p, l, readme) for p in papers)
    tasks = ''.join(f'<option value="{t}">{l[t]}</option>' for t in ('D', 'L', 'E'))
    training = ''.join(f'<option value="{t}">{l[t]}</option>' for t in ('training-free', 'sft', 'rl', 'other'))
    asset_version = lambda name: hashlib.sha256((ROOT / 'site/assets' / name).read_bytes()).hexdigest()[:12]
    page = f'''<!doctype html>
<html lang="{l['lang']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(l['description'])}">
<meta name="theme-color" content="#ffffff">
<title>Awesome Agentic AIGC Detection · {l['collection']}</title>
<link rel="icon" href="{prefix}assets/favicon.svg?v={asset_version("favicon.svg")}" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/style.css?v={asset_version("style.css")}">
<script src="{prefix}assets/app.js?v={asset_version("app.js")}" defer></script>
</head>
<body data-language="{lang}" data-result-label="{l['results']}">
<a class="skip-link" href="#papers">{l['skip']}</a>
<header class="site-header"><div class="header-inner"><a class="brand" href="{prefix or './'}" aria-label="Awesome Agentic AIGC Detection"><svg class="brand-symbol" aria-hidden="true" viewBox="0 0 28 28"><path d="M7 3h10l5 5v17H7zM16 3v6h6M11 14h7M11 18h7"/></svg><span>Agentic AIGC<span class="brand-sub">Detection</span></span></a><nav aria-label="Main"><a href="#papers" class="nav-papers">{l['collection']}</a><a href="#resources">{l['resources']}</a><a class="language-link" href="{l['other_url']}" lang="{'en' if lang == 'zh' else 'zh-CN'}">{l['other_lang']}</a><a class="github-link" href="{REPO}">GitHub <span aria-hidden="true">↗</span></a></nav></div></header>
<main>
<section class="intro shell" aria-labelledby="hero-title">
  <p class="eyebrow">{l['kicker']}</p>
  <h1 id="hero-title">{l['title']}</h1>
  <p class="intro-description">{l['description']}</p>
  <div class="collection-meta"><div class="collection-stats"><span><strong>{len(papers)}</strong> {l['papers']}</span><span><strong>4</strong> {l['modalities']}</span><span><strong>3</strong> {l['tasks']}</span></div><a href="{readme_url}" class="sync-link">{l['sync']} <span aria-hidden="true">↗</span></a></div>
</section>
<section id="papers" class="library shell" aria-labelledby="library-title">
  <h2 id="library-title" class="sr-only">{l['subtitle']}</h2>
  <noscript><p class="noscript-message">{l['nojs']}</p></noscript>
  <div class="library-layout">
    <div class="search-box"><label for="search" class="sr-only">{l['search']}</label><svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22"><circle cx="10.8" cy="10.8" r="6.8"/><path d="m16 16 5 5"/></svg><input id="search" type="search" placeholder="{l['placeholder']}" autocomplete="off"><kbd aria-hidden="true">/</kbd></div>
    <aside class="filter-panel" id="filter-panel" aria-label="{l['filter']}" data-open="false">
      <button type="button" id="toggle-filters" class="filter-toggle" aria-expanded="false" aria-controls="filter-controls"><svg aria-hidden="true" viewBox="0 0 20 20"><path d="M3 5h14M5 10h10M7 15h6"/></svg>{l['filter']}<span id="active-filter-count" hidden>0</span><span class="toggle-chevron" aria-hidden="true">⌄</span></button>
      <div class="filter-sticky" id="filter-controls">
      <div class="filter-heading"><h2>{l['filter']}</h2><button type="button" class="reset-button" id="reset-filters">{l['reset']}</button></div>
      <fieldset class="modality-fieldset"><legend>{l['modality']}</legend><button type="button" class="modality-button" data-modality="all" aria-pressed="true"><span>{l['all']}</span><span class="filter-count">{len(papers)}</span></button>{filters}</fieldset>
      <div class="select-filter"><label class="select-label" for="task-filter">{l['task']}</label><select id="task-filter"><option value="all">{l['all_tasks']}</option>{tasks}</select></div>
      <div class="select-filter"><label class="select-label" for="training-filter">{l['training']}</label><select id="training-filter"><option value="all">{l['all_training']}</option>{training}</select></div>
      <p class="filter-note">{l['training_note']}</p><p class="filter-legend">{l['legend']}</p>
      <a class="comparison-link" href="{comparison_url}">{l['comparison']} <span aria-hidden="true">↗</span></a>
      <a class="apply-filters" id="apply-filters" href="#paper-list">{l['show_results']} <span aria-hidden="true">↓</span></a>
    </div></aside>
    <div class="results-area">
      <div class="results-toolbar"><p id="result-count" role="status" aria-live="polite">{len(papers)} / {len(papers)} {l['results']}</p><label class="sr-only" for="sort">{l['sort']}</label><select id="sort"><option value="catalog">{l['catalog']}</option><option value="newest">{l['newest']}</option><option value="az">{l['az']}</option></select></div>
      <div class="paper-list" id="paper-list">{cards}</div>
      <div class="empty-state" id="empty-state" hidden><h3>{l['empty']}</h3><p>{l['empty_hint']}</p><button class="primary-button" type="button" id="empty-reset">{l['reset']}</button></div>
    </div>
  </div>
</section>
<section class="reading-notes shell" aria-labelledby="notes-title"><h2 id="notes-title">{l['notes']}</h2><div class="note-grid"><div><h3>{l['scope_title']}</h3><p>{l['scope']}</p></div><div><h3>{l['order_title']}</h3><p>{l['order']}</p></div><div><h3>{l['source_title']}</h3><p>{l['source_text']}</p></div></div></section>
<section id="resources" class="resources-section shell" aria-labelledby="resources-title"><h2 id="resources-title">{l['resources']}</h2><div class="resource-grid"><a href="{comparison_url}"><span>01 <span aria-hidden="true">↗</span></span><h3>{l['comparison']}</h3><p>{l['compare_hint']}</p></a><a href="{readme_url}#surveys"><span>02 <span aria-hidden="true">↗</span></span><h3>{l['survey']}</h3><p>{l['survey_hint']}</p></a><a href="{readme_url}#resources"><span>03 <span aria-hidden="true">↗</span></span><h3>{l['resources_title']}</h3><p>{l['resources_hint']}</p></a></div></section>
</main>
<footer class="site-footer"><div class="shell footer-inner"><div><strong>Awesome Agentic AIGC Detection</strong><p>{l['footer']}</p></div><div class="footer-links"><a href="{REPO}/issues">{l['contribute']} ↗</a><a href="{readme_url}">README ↗</a><a href="{prefix}catalog.json">JSON ↗</a></div></div></footer>
<!-- Catalogue source SHA-256: {catalog['source_sha256']} -->
</body></html>'''
    arrow = '<svg class="external-arrow" aria-hidden="true" viewBox="0 0 12 12"><path d="M3 9 9 3M3 3h6v6"/></svg>'
    return page.replace('↗', arrow)


def build(output, root=ROOT):
    catalog = load_catalog(root)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'zh').mkdir(exist_ok=True)
    shutil.copytree(root / 'site/assets', output / 'assets', dirs_exist_ok=True)
    (output / 'index.html').write_text(render(catalog, 'en'), encoding='utf-8')
    (output / 'zh/index.html').write_text(render(catalog, 'zh'), encoding='utf-8')
    (output / 'catalog.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (output / '.nojekyll').write_text('')
    print(f'Built {catalog["count"]} papers in English and Chinese at {output}')
    return catalog


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / '_site')
    args = parser.parse_args()
    build(args.output)
