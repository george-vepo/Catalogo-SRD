'use strict';
// Consulta preliminar isolada. Nunca modifica o catálogo geral, decks ou fichas.
const get = id => document.getElementById(id);
const norm = s => String(s ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase('pt-BR');
const state = { records:[], filtered:[], shown:0, chunk:80 };
function textNode(tag, value, className='') {
  const node=document.createElement(tag);
  node.textContent=String(value??'');
  if(className)node.className=className;
  return node;
}
function setStatus(message){get('load-status').textContent=message;}
function escValue(value){return value===''||value==null?'Não informado':String(value);}
function populateSelect(id,records,key,caption) {
  const list=[...new Set(records.map(x=>x[key]).filter(Boolean))].sort((a,b)=>a.localeCompare(b,'pt-BR'));
  for (const value of list) {
    const option=document.createElement('option');
    option.value=value; option.textContent=value;
    get(id).append(option);
  }
  get(id).firstElementChild.textContent=caption;
}
function buildRow(item) {
  const tr=document.createElement('tr');
  const id=textNode('td',item.id,'monospace');
  const title=document.createElement('td');
  title.append(textNode('strong',item.nome));
  title.append(textNode('small',item.editora+(item.publicacao?' · '+item.publicacao:''),'secondary'));
  const typ=textNode('td',item.tipo);
  const nd=textNode('td',escValue(item.nd),'monospace');
  const rar=textNode('td',item.raridade);
  const situ=textNode('td',item.situacao_catalogo,'smaller');
  const valid=document.createElement('td');
  valid.append(textNode('strong',item.status_ficha_origem||'Não informado'));
  valid.append(textNode('small','Booster (texto original): '+escValue(item.elegivel_booster_origem),'secondary'));
  const coverage=textNode('td',item.id_na_megalista_web?'ID presente':'ID ausente',
    item.id_na_megalista_web?'covered':'missing');
  tr.append(id,title,typ,nd,rar,situ,valid,coverage);
  return tr;
}
function drawRows(reset) {
  if(reset) {state.shown=0; get('rows').replaceChildren();}
  const remaining=state.filtered.slice(state.shown,state.shown+state.chunk);
  const frag=document.createDocumentFragment();
  for(const item of remaining) frag.append(buildRow(item));
  get('rows').append(frag);
  state.shown+=remaining.length;
  get('more').hidden=state.shown>=state.filtered.length;
  get('shown').textContent=state.shown+' de '+state.filtered.length+' resultados';
}
function applyFilters() {
  const q=norm(get('q').value.trim());
  const type=get('type').value,rar=get('rarity').value,
    status=get('situation').value,coverage=get('coverage').value,booster=get('booster').value;
  state.filtered=state.records.filter(r=>
     (!q||norm([r.id,r.nome,r.tipo,r.editora,r.publicacao].join(' ')).includes(q))
     &&(!type||r.tipo===type)
     &&(!rar||r.raridade===rar)
     &&(!status||r.situacao_catalogo===status)
     &&(!coverage||(coverage==='missing'?!r.id_na_megalista_web:r.id_na_megalista_web))
     &&(!booster||(booster==='sim'?r.elegivel_booster_origem==='SIM':r.elegivel_booster_origem!=='SIM'))
  );
  drawRows(true);
}
async function init() {
  try{
    const response=await fetch('data/catalogo-ativo-635-consulta-20261021.json',{cache:'no-cache'});
    if(!response.ok)throw Error('HTTP '+response.status);
    const data=await response.json();
    if(data.schema!=='SRD_CATALOGO_ATIVO_CONSULTA_PRELIMINAR_V1'
       ||data.registros?.length!==635
       ||data.resumo?.ids_ausentes_megalista_web!==29)throw Error('Dados inconsistentes com a auditoria.');
    const ids=new Set(data.registros.map(x=>x.id));
    if(ids.size!==635)throw Error('IDs duplicados.');
    const miss=data.registros.filter(x=>!x.id_na_megalista_web);
    if(miss.length!==29)throw Error('Ausências inconsistentes.');
    state.records=data.registros;
    get('total').textContent='635';
    get('common').textContent='606';
    get('missing').textContent='29';
    get('booster-yes').textContent=data.registros.filter(r=>r.elegivel_booster_origem==='SIM').length;
    get('source').textContent='Fonte: '+data.fonte+' · versão de referência '+data.data_referencia;
    populateSelect('type',data.registros,'tipo','Todos os tipos');
    populateSelect('rarity',data.registros,'raridade','Todas as raridades');
    populateSelect('situation',data.registros,'situacao_catalogo','Todas as situações');
    for(const id of ['q','type','rarity','situation','coverage','booster']){
      get(id).addEventListener(id==='q'?'input':'change',applyFilters);
    }
    get('more').addEventListener('click',()=>drawRows(false));
    get('show-missing').addEventListener('click',()=>{
      get('coverage').value='missing'; get('q').value='';applyFilters();
    });
    get('clear').addEventListener('click',()=>{
      get('q').value='';
      for(const id of ['type','rarity','situation','coverage','booster'])get(id).value='';
      applyFilters();
    });
    setStatus('Consulta de auditoria carregada. Nenhuma informação foi homologada por esta página.');
    applyFilters();
  }catch(err){
    setStatus('Não foi possível carregar a consulta: '+err.message);
    get('rows').replaceChildren();
    get('more').hidden=true;
  }
}
init();
