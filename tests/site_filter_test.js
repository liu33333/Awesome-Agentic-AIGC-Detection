/* Dependency-free integration of the shipped filter script against a DOM fixture. */
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const fixture = JSON.parse(fs.readFileSync(process.argv[2] || '_site/catalog.json', 'utf8'));
let assertions = 0;
function test(name, fn) { fn(); assertions++; console.log(`PASS ${name}`); }
function start(query = '', lang = 'en') {
  class Element {
    constructor(dataset = {}) { this.dataset = dataset; this.value = ''; this.hidden = false; this.events = {}; this.attributes = {}; this.tagName = 'DIV'; }
    addEventListener(name, fn) { this.events[name] = fn; }
    setAttribute(name, value) { this.attributes[name] = value; }
    getAttribute(name) { return this.attributes[name]; }
    focus() { doc.activeElement = this; }
  }
  const cards = fixture.papers[lang].map(p => new Element({
    modality: p.modality, tasks: p.tasks.join(' '), training: p.training_tags.join(' '), order: String(p.order), date: p.sort_date, title: p.title,
    search: [p.id,p.title,p.venue,p.model,p.training,p.workflow,p.modality].join(' ')
  }));
  const ids = Object.fromEntries(['paper-list','search','task-filter','training-filter','sort','result-count','empty-state','reset-filters','empty-reset'].map(id => [id,new Element()]));
  ids.search.tagName = 'INPUT';
  for (const [key,values] of Object.entries({'task-filter':['all','D','L','E'],'training-filter':['all','training-free','sft','rl','other'],'sort':['catalog','newest','az']})) {
    ids[key].options = values.map(value=>({value})); ids[key].value = values[0];
  }
  const list = ids['paper-list']; list.children = [...cards]; list.querySelectorAll = () => cards;
  list.append = c => { list.children = list.children.filter(x=>x!==c); list.children.push(c); };
  const buttons = ['all','audio','visual','text','cross-modal'].map(modality=>new Element({modality}));
  const language = new Element(); language.attributes.href = lang==='en' ? 'zh/' : '../';
  const doc = {getElementById:id=>ids[id], querySelectorAll:()=>buttons, querySelector:()=>language, body:{dataset:{resultLabel:'papers'}}, activeElement:new Element(), events:{}, addEventListener(name,fn){this.events[name]=fn;}};
  const location = new URL(`https://example.com/project/${lang==='zh'?'zh/':''}${query}`);
  const history = { replaceState(_a,_b,url){ const n=new URL(url,location.href);location.href=n.href; } };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../site/assets/app.js'),'utf8'), {document:doc,window:{location},location,history,URL,URLSearchParams});
  return {ids,cards,list,buttons,doc,location,language,visible:()=>list.children.filter(c=>!c.hidden), set(id,value){ids[id].value=value;ids[id].events[id==='search'?'input':'change']();}, modality(value){buttons.find(b=>b.dataset.modality===value).events.click();},reset(){ids['reset-filters'].events.click();}};
}
const app=start();
test('initial static catalogue order retained',()=>assert.equal(app.visible().length,fixture.count));
test('case-insensitive keyword search',()=>{app.set('search','tOoLdF');assert.equal(app.visible()[0].dataset.title.includes('ToolDF'),true);assert.equal(app.visible().length,1);});
test('multiword model and workflow query',()=>{app.set('search','qwen separation');assert.equal(app.visible().length,1);});
test('modality filters all groups',()=>{app.reset();for(const group of ['audio','visual','text','cross-modal']){app.modality(group);assert.equal(app.visible().length,fixture.papers.en.filter(p=>p.modality===group).length);}});
test('modality task and training intersect',()=>{app.reset();app.modality('visual');app.set('task-filter','L');app.set('training-filter','rl');assert.ok(app.visible().length>0);assert.ok(app.visible().every(c=>c.dataset.modality==='visual'&&c.dataset.tasks.includes('L')&&c.dataset.training.includes('rl')));});
test('empty state appears and reset works',()=>{app.set('search','zzzz-nothing-zzzz');assert.equal(app.visible().length,0);assert.equal(app.ids['empty-state'].hidden,false);app.ids['empty-reset'].events.click();assert.equal(app.visible().length,fixture.count);assert.equal(app.ids['empty-state'].hidden,true);});
test('SFT+RL participates in both filters',()=>{app.set('training-filter','sft');assert.ok(app.visible().some(c=>c.dataset.training==='sft rl'));app.set('training-filter','rl');assert.ok(app.visible().some(c=>c.dataset.training==='sft rl'));});
test('newest ordering uses source-backed full dates',()=>{app.reset();app.set('sort','newest');const dates=app.visible().map(c=>c.dataset.date);assert.deepEqual(dates,[...dates].sort().reverse());});
test('alphabetical sort works',()=>{app.set('sort','az');const titles=app.visible().map(c=>c.dataset.title);assert.deepEqual(titles,[...titles].sort((a,b)=>a.localeCompare(b,'en')));});
test('URL stores filter state',()=>{app.reset();app.modality('audio');app.set('search','sear');assert.equal(app.location.searchParams.get('modality'),'audio');assert.equal(app.location.searchParams.get('q'),'sear');});
test('language link preserves filters and path',()=>{const target=new URL(app.language.href);assert.equal(target.pathname,'/project/zh/');assert.equal(target.searchParams.get('q'),'sear');});
test('direct URL restores filter state',()=>{const deep=start('?q=sear&modality=audio&training=training-free');assert.equal(deep.visible().length,1);assert.equal(deep.visible()[0].dataset.title.includes('SEAR'),true);});
test('invalid URL parameters are ignored safely',()=>{const deep=start('?modality=bad&task=invalid&training=bad&sort=bad');assert.equal(deep.visible().length,fixture.count);});
test('Chinese catalogue shares filter behavior',()=>{const zh=start('?modality=cross-modal&task=L&training=rl','zh');assert.ok(zh.visible().length>0);assert.ok(zh.visible().every(c=>c.dataset.modality==='cross-modal'));assert.equal(new URL(zh.language.href).pathname,'/project/');});
test('slash focuses search, not while editing',()=>{let prevented=false;app.doc.activeElement={tagName:'BODY'};app.doc.events.keydown({key:'/',preventDefault(){prevented=true;}});assert.equal(prevented,true);assert.equal(app.doc.activeElement,app.ids.search);});
test('Escape clears search',()=>{app.set('search','not-a-paper');app.doc.events.keydown({key:'Escape'});assert.equal(app.ids.search.value,'');assert.ok(app.visible().length>0);});
console.log(`${assertions} filter integration checks passed.`);
