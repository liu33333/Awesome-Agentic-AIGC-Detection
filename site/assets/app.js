/* Progressive enhancement: all paper content is generated from README at build time. */
'use strict';
(() => {
  const $ = (id) => document.getElementById(id);
  const list = $('paper-list');
  const cards = Array.from(list.querySelectorAll('.paper-card'));
  const search = $('search');
  const task = $('task-filter');
  const training = $('training-filter');
  const sort = $('sort');
  const buttons = Array.from(document.querySelectorAll('.modality-button'));
  const filterPanel = $('filter-panel');
  const filterToggle = $('toggle-filters');
  document.body.dataset.enhanced = 'true';
  function setFiltersOpen(open) {
    filterPanel.dataset.open = String(open);
    filterToggle.setAttribute('aria-expanded', String(open));
  }
  filterToggle.addEventListener('click', () => setFiltersOpen(filterPanel.dataset.open !== 'true'));
  $('apply-filters').addEventListener('click', () => { setFiltersOpen(false); filterToggle.focus(); });
  const params = new URLSearchParams(window.location.search);
  let modality = params.get('modality') || 'all';
  if (!buttons.some(b => b.dataset.modality === modality)) modality = 'all';
  const normalize = (value) => value.normalize('NFKC').toLocaleLowerCase().replace(/[\u2010-\u2015]/g, '-');
  cards.forEach(card => { card.searchText = normalize(card.dataset.search); });
  function restore(select, key) {
    const value = params.get(key);
    if (Array.from(select.options).some(option => option.value === value)) select.value = value;
  }
  search.value = params.get('q') || '';
  restore(task, 'task'); restore(training, 'training'); restore(sort, 'sort');
  function update() {
    const terms = normalize(search.value).trim().split(/\s+/).filter(Boolean);
    let count = 0;
    const ordered = [...cards].sort((a, b) => {
      if (sort.value === 'newest') return b.dataset.date.localeCompare(a.dataset.date) || Number(a.dataset.order) - Number(b.dataset.order);
      if (sort.value === 'az') return a.dataset.title.localeCompare(b.dataset.title, 'en');
      return Number(a.dataset.order) - Number(b.dataset.order);
    });
    for (const card of ordered) {
      card.hidden = !((modality === 'all' || card.dataset.modality === modality)
        && (task.value === 'all' || card.dataset.tasks.split(' ').includes(task.value))
        && (training.value === 'all' || card.dataset.training.split(' ').includes(training.value))
        && terms.every(term => card.searchText.includes(term)));
      if (!card.hidden) count++;
      list.append(card);
    }
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.modality === modality)));
    $('result-count').textContent = `${count} / ${cards.length} ${document.body.dataset.resultLabel}`;
    $('empty-state').hidden = count !== 0;
    const filterCount = Number(modality !== 'all') + Number(task.value !== 'all') + Number(training.value !== 'all');
    $('active-filter-count').textContent = String(filterCount);
    $('active-filter-count').hidden = filterCount === 0;
    const query = new URLSearchParams();
    if (search.value.trim()) query.set('q', search.value.trim());
    if (modality !== 'all') query.set('modality', modality);
    if (task.value !== 'all') query.set('task', task.value);
    if (training.value !== 'all') query.set('training', training.value);
    if (sort.value !== 'catalog') query.set('sort', sort.value);
    const queryString = query.toString();
    const nextUrl = `${location.pathname}${queryString ? `?${queryString}` : ''}${location.hash}`;
    history.replaceState(null, '', nextUrl);
    const language = document.querySelector('.language-link');
    const target = new URL(language.getAttribute('href'), location.href);
    target.search = queryString;
    target.hash = location.hash;
    language.href = target.href;
  }
  function reset() {
    modality = 'all'; search.value = ''; task.value = 'all'; training.value = 'all'; sort.value = 'catalog'; update();
  }
  search.addEventListener('input', update);
  [task, training, sort].forEach(control => control.addEventListener('change', update));
  buttons.forEach(button => button.addEventListener('click', () => { modality = button.dataset.modality; update(); }));
  $('reset-filters').addEventListener('click', reset);
  $('empty-reset').addEventListener('click', () => {
    reset();
    search.focus();
    search.scrollIntoView({ block: 'center', behavior: 'auto' });
  });
  document.querySelector('.language-link').addEventListener('click', event => {
    const link = event.currentTarget;
    const target = new URL(link.href, location.href);
    target.search = location.search;
    target.hash = location.hash;
    link.href = target.href;
  });
  document.addEventListener('keydown', event => {
    const editing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName) || document.activeElement.isContentEditable;
    if (event.key === '/' && !editing && !event.metaKey && !event.ctrlKey && !event.altKey) { event.preventDefault(); search.focus(); }
    if (event.key === 'Escape' && document.activeElement === search) { search.value = ''; update(); }
  });
  update();
})();
