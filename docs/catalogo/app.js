'use strict';
const $ = id => document.getElementById(id);
const esc = value => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
const link = value => /^https:\/\/[^"'<> ]+/i.test(value||'') ? value : '';
// SRD_CATALOGO_ARTES_GERADAS_20261015: accept only whitelisted local assets.
const artSrc = value => (/^https:\/\/[^\"'<> ]+/i.test(value||'') || (/^assets\/(?:artes-geradas-20261015|drive-candidatas-20261021)\/[a-z0-9-]+\.webp$/i.test(value||''))) ? value : '';
const norm = value => String(value??'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().trim();
const $gallery = $('gallery');
const placeholder = () => $('missingImage').innerHTML.trim();
const classes = {'Comum':'common','Incomum':'uncommon','Rara':'rare','Lendária':'legendary','Mítica':'mythic'};
const stop = text => { $('status').textContent = text; };
const appState = {all:[], filtered:[], limit:60, active:null, lastFocus:null, zoom:1, x:0, y:0, drag:null};
function safeImage(url, label) {
  if (!artSrc(url)) return placeholder();
  return '<img loading="lazy" referrerpolicy="no-referrer" src="' + esc(url) + '" alt="' + esc(label) + '">';
}
function onImageError(img) {
  img.replaceWith($('missingImage').content.firstElementChild.cloneNode(true));
}
function makeLink(url, label) {
  return link(url) ? '<a class="ghost-btn" target="_blank" rel="noopener noreferrer" href="' + esc(url) + '">' + esc(label) + ' ↗</a>' : '';
}
function stat(value, label) {
  return '<div class="stat"><div class="value">' + esc(value === '' || value == null ? '—' : value) + '</div><div class="label">' + esc(label) + '</div></div>';
}
function section(title, body) {
  return '<section class="section"><h3>' + esc(title) + '</h3>' + body + '</section>';
}
function pair(label, value) {
  if (value == null || value === '' || (Array.isArray(value) && !value.length)) return '';
  const txt = typeof value === 'object' ? JSON.stringify(value) : String(value);
  return '<div class="pair"><dt>' + esc(label.replace(/_/g,' ')) + '</dt><dd>' + esc(txt) + '</dd></div>';
}
function rawData(title, value, isOpen) {
  const content = typeof value === 'string' ? value : JSON.stringify(value,null,2);
  return '<details ' + (isOpen ? 'open' : '') + '><summary>' + esc(title) + '</summary><pre>' + esc(content) + '</pre></details>';
}
function referenceDetails(extra) {
  if (!extra) return '';
  const p = extra.provenance || {};
  const external = extra.reference_scope === 'EXTERNAL_THIRD_PARTY_SOURCE_SUMMARY';
  const method = String(p.verification_method || '').toUpperCase();
  const partial = external && /INDICE|BLOQUEAD|PARCIAL|TEXTO_2023/.test(method);
  const title = external ? 'Ficha de terceiro resumida — não homologada' : 'Ficha de referência revisada — não homologada';
  const warning = external
    ? (partial ? 'A origem pode estar bloqueada e a conferência inclui índice ou espelho não oficial. Este resumo é de terceiros, não é SRD 5.2.1 e continua sem homologação para o jogo.' : 'Resumo próprio de referência externa consultada. Não equivale à transcrição integral nem à mecânica homologada do card game.')
    : 'Referência D&D 5e conferida em pesquisa anterior, com revisão independente ainda pendente. Não transforma os dados em mecânica oficial do card game.';
  const source = p.source_url || p.mechanical_source || '';
  const alternate = p.source_alt_url || p.crosscheck_url || '';
  const sourceLink = '<div class="linkrow">' + (source ? makeLink(source, 'Fonte original / portal de referência') : '') +
    (alternate && alternate !== source ? makeLink(alternate, 'Referência secundária (não oficial)') : '') + '</div>';
  return section(title, '<p class="notice">' + esc(warning) + '</p>' + sourceLink +
    rawData(external ? 'Resumo e proveniência' : 'Estatísticas, traços, ações e condições da fonte', extra, true));
}
function currentList() { return appState.filtered; }
function render(reset) {
  if (reset) appState.limit=60;
  const q=norm($('search').value), typ=$('type').value, rar=$('rarity').value, scope=$('scope').value;
  appState.filtered=appState.all.filter(c=>{
    if(typ!=='all'&&c.type!==typ)return false;
    if(rar!=='all'&&c.rarity!==rar)return false;
    if(scope==='607'&&!c.mechanics)return false;
    if(scope==='external'&&c.mechanics)return false;
    if(scope==='celestial'&&!c.celestial.length)return false;
    if(scope==='aberracao'&&!c.aberracao.length)return false;
    if(scope==='image'&&!c.art)return false;
    if(scope==='full'&&!c.mechanics?.ficha_integral_texto_local)return false;
    if(scope==='support'&&!c.celestial.length&&!c.aberracao.some(x=>x.support))return false;
    return !q||c.search.includes(q);
  });
  $('count').textContent=appState.filtered.length.toLocaleString('pt-BR');
  const subset=appState.filtered.slice(0,appState.limit);
  $gallery.replaceChildren();
  if(!subset.length){const n=document.createElement('div');n.className='empty';n.textContent='Nenhuma criatura encontrada com esses filtros.';$gallery.append(n);}
  const frag=document.createDocumentFragment();
  subset.forEach(c=>{
    const btn=document.createElement('button');
    btn.className='creature';btn.type='button';btn.dataset.rarity=classes[c.rarity]||'common';
    btn.setAttribute('aria-label','Abrir ficha da criatura '+c.name);
    const frame=document.createElement('div');frame.className='art-frame';frame.innerHTML=safeImage(c.art,'Ilustração de referência de '+c.name);
    const img=frame.querySelector('img');if(img)img.addEventListener('error',()=>onImageError(img),{once:true});
    const name=document.createElement('span');name.className='creature-name';name.textContent=c.name;
    btn.append(frame,name);
    if(c.artIsDrive){const label=document.createElement('span');label.className='drive-art-notice';label.textContent='Arte do autor · em revisão';btn.append(label);}
    btn.addEventListener('click',()=>openCard(c.index));
    frag.append(btn);
  });
  $gallery.append(frag);
  $('more').style.display=appState.filtered.length>appState.limit?'inline-flex':'none';
}
function mechanicsSummary(c){
  const f=c.mechanics;
  if(!f)return section('Ficha de combate','<p>Nenhuma ficha mecânica integrada no repositório para esta entrada. Use as fontes editoriais indicadas; não serão criados atributos ou habilidades inexistentes.</p>');
  let html='<div class="meta-pairs">'+
    pair('Iniciativa',f.iniciativa)+pair('Deslocamento',f.deslocamento)+
    pair('Atributos FOR/DES/CON/INT/SAB/CAR',f.atributos_FOR_DES_CON_INT_SAB_CAR)+
    pair('Status da ficha',f.status_ficha)+pair('Ficha mecânica completa (controle histórico)',f.ficha_mecanica_completa)+
    pair('Editora',f.editora)+pair('Publicação',f.publicacao)+
    '</div>';
  if(f.ficha_integral_texto_local)html+=rawData('Ficha integral registrada no repositório',f.ficha_integral_texto_local,true);
  if(f.mecanica_externa_integrada) {
    const m=f.mecanica_externa_integrada;
    html+='<p class="notice">Mecânica externa integrada em resumos estruturados próprios. A presença dos campos não substitui auditoria nem transcrição oficial da publicação.</p>';
    const fields=['atributos','salvaguardas','pericias','resistencias_dano','imunidades_dano','vulnerabilidades_dano','imunidades_condicao','sentidos','tracos','acoes','acoes_bonus','reacoes','acoes_lendarias','conjuracao'];
    const pairs=fields.filter(k=>m[k]!=null&&(!Array.isArray(m[k])||m[k].length));
    for(const key of pairs) {
      const val=m[key]; const header=key.replace(/_/g,' ');
      html+=rawData(header.charAt(0).toUpperCase()+header.slice(1),val, ['atributos','acoes','tracos'].includes(key));
    }
    html+=rawData('Todos os dados da mecânica estruturada',m,false);
  }
  if(f.habilidades_resumo_web)html+=rawData('Habilidades resumidas',f.habilidades_resumo_web,false);
  html+=rawData('Registro mecânico completo (JSON)',f,false);
  return section('Ficha de combate — registro do repositório',html);
}
function linksBlock(c) {
  const f=c.mechanics||{},m=c.meta,art=c.artRecord||{},c0=c.celestial[0]||{},curated=c.curated||{};
  const links=[
    [c0.sheet,'Ficha original / publicação de referência'],
    [f.url_ficha_individual_conhecida,'Ficha individual conhecida'],
    [f.url_referencia,'Referência do registro SRD'],
    [f.url_referencia_catalogo,'Catálogo editorial'],
    [curated.source_url,'Fonte da imagem revisada'],
    [art.URL_pagina_origem,'Fonte da ilustração'],
    [m['URL CATÁLOGO'],'Página do catálogo'],
    [m['URL ÍNDICE ESTRUTURADO'],'Índice estruturado da fonte']
  ];
  const visited=new Set(),parts=[];
  for(const [url,label] of links)if(link(url)&&!visited.has(url)){visited.add(url);parts.push(makeLink(url,label));}
  return section('Fontes e consulta',parts.length?'<div class="linkrow">'+parts.join('')+'</div>':'<p>Não há endereço público individual registrado para esta criatura.</p>');
}
function deckBlock(c) {
  let parts=[];
  if(c.celestial.length){
    const ids=c.celestial.map(x=>x.id).join(', '),x=c.celestial[0];
    parts.push(section('Baralho Celestial — 40 cartas','<p><strong>Cópias:</strong> '+esc(ids)+' · <strong>CA/PV do deck:</strong> '+esc(x.ac||'—')+' / '+esc(x.hp||'—')+'</p>'+
      '<p><strong>Suporte candidato ('+esc(x.abilityType||'')+'): '+esc(x.ability||'Não informado')+'</strong></p>'+
      '<p>'+esc(x.abilityDescription||'')+'</p>'+
      '<p><strong>Requisitos:</strong> '+esc(x.requirements||'Não informados')+'</p>'+
      '<p><strong>Homebrew:</strong> '+esc(x.homebrew||'Não informado')+'</p>'+
      '<p class="notice">'+esc(x.status||'Pendente de homologação')+'</p>'+
      '<div class="linkrow">'+makeLink(x.supportSource,'Fonte do suporte')+'</div>'));
  }
  if(c.aberracao.length) {
    const a=c.aberracao[0],ids=c.aberracao.map(x=>x.ORDEM).join(', ');
    let ab= '<p><strong>Posição(ões) no deck:</strong> '+esc(ids)+'</p><p><strong>Situação:</strong> '+esc(a.STATUS_REVISAO_20261014||a.CLASSIFICACAO_FICHA||'Não informada')+'</p>';
    if(a.support)ab+='<p><strong>Suporte candidato:</strong> '+esc(a.support.habilidade)+'</p><p>'+esc(a.support.efeito)+'</p><p><strong>Revisão:</strong> '+esc(a.support.revisao)+'</p>';
    parts.push(section('Baralho Aberração — proposta histórica',ab));
  }
  return parts.join('');
}
async function carregarFichaDrive(c) {
  const target = $('driveFichaConteudo');
  if (!target || !c.driveFicha) return;
  const id = c.meta['ID NO JOGO'] || '';
  try {
    const ficha = await getJSON(c.driveFicha.arquivo);
    if (appState.active !== c || !target.isConnected) return;
    const recebido = ficha.identificacao?.id_catalogo || ficha.ID_CATALOGO || '';
    if (!id || id !== c.driveFicha.id_catalogo || recebido !== id) {
      target.textContent = 'Identidade da ficha divergente: dados não exibidos.';
      return;
    }
    target.innerHTML = '<p class="notice">Arquivo de referência importado do Drive, com edição declarada ' +
      esc(c.driveFicha.edicao) + '. Não substitui ficha-base nem constitui homologação administrativa.</p>' +
      rawData('Ver JSON da ficha estruturada original', ficha, false);
  } catch (err) {
    if (appState.active === c && target.isConnected) target.textContent = 'Ficha complementar indisponível: ' + String(err.message||err);
  }
}
function openCard(index,fromLink) {
  const c=appState.all[index];if(!c)return;
  appState.lastFocus=appState.lastFocus||document.activeElement;
  appState.active=c;
  $('modal').classList.add('open');$('modal').setAttribute('aria-hidden','false');document.body.classList.add('lock');
  $('detailArt').innerHTML=safeImage(c.art,'Imagem inteira de '+c.name);
  const img=$('detailArt').querySelector('img');if(img)img.addEventListener('error',()=>onImageError(img),{once:true});
  $('imageActions').innerHTML=c.art?'<button type="button" id="showImage" class="ghost-btn">⤢ Ver imagem inteira</button>':'<span class="src-note">Imagem não confirmada. Sem substituição por outra criatura.</span>';
  if(c.art)$('showImage').addEventListener('click',openImage);
  const f=c.mechanics,m=c.meta;
  const id=m['ID NO JOGO']||'Sem ID canônico';
  const baseStatus=c.audit?.Estado||m.STATUS||'Não indicado';
  let status='<div class="notice"><strong>Estado documental:</strong> '+esc(baseStatus)+'. Fichas, imagens e suportes só são homologados conforme os registros de controle e decisões do administrador.</div>';
  if(f?.tipo_catalogo&&norm(f.tipo_catalogo)!==norm(c.type))status+='<div class="notice">Atenção: tipo divergente entre megalista ('+esc(c.type)+') e ficha dos 607 ('+esc(f.tipo_catalogo)+'). Identidade ou edição precisa de reconciliação.</div>';
  let top='<div class="tinycaps">BESTIÁRIO · REGISTRO '+esc(String(index+1))+' / 1320</div><h2>'+esc(c.name)+'</h2>'+
    '<div class="subid">'+esc(id)+' · '+esc(m['PUBLICAÇÃO']||m.FONTE||'Origem não informada')+'</div>'+
    '<div class="pills"><span class="pill">'+esc(c.rarity)+'</span><span class="pill">'+esc(c.type)+'</span>'+
    (c.celestial.length?'<span class="pill">Baralho Celestial</span>':'')+
    (c.aberracao.length?'<span class="pill">Deck Aberração</span>':'')+'</div>'+
    '<div class="stats">'+stat(c.nd,'NÍVEL DE DESAFIO')+stat(f?.CA??c.celestial[0]?.ac??'—','CLASSE DE ARMADURA')+stat(f?.PV??c.celestial[0]?.hp??'—','PV MÁXIMOS')+'</div>';
  let metaPairs=Object.entries(m).map(([k,v])=>pair(k,v)).join('');
  const imageNote=c.artIsDrive?'<p>Imagem criada pelo usuário e publicada com sua autorização em 21/10/2026. Identidade e estilo editorial ainda em revisão; não é ilustração oficial D&D nem altera a ficha da criatura.</p>':c.generated?'<p>Arte digital gerada em ChatGPT em revisão. Não é ilustração oficial da criatura, nem homologação da ficha ou dos direitos editoriais.</p>':c.art?
    '<p>Ilustração de referência (web), conforme arquivo de pesquisa. Fonte, edição e direitos de reprodução podem exigir revisão.</p>':
    '<p>Não há arte direta verificada e adequada para este registro. O catálogo não utiliza imagens de espécies parecidas como substituição.</p>';
  const candidataDrive = c.driveArt ?
    '<div class="notice"><strong>Arte adicional do Drive — ' + esc(c.driveArt.status) +
    ':</strong> imagem criada pelo usuário, com publicação autorizada no Catálogo SRD. A identidade visual permanece em revisão.</div>' +
    safeImage(c.driveArt.arquivo, 'Arte candidata do Drive de ' + c.name) +
    '<p class="src-note">' + esc(c.driveArt.revisao_visual) + ' · ' + esc(c.driveArt.direitos) + '</p>' : '';
  const imageBlock=section('Imagem e licença',imageNote+candidataDrive+(c.generated?'<p><strong>Proveniência da arte:</strong> '+esc(c.generated.origin)+'. '+esc(c.generated.review_note)+'</p>':'')+(c.curated?'<p><strong>Revisão visual manual:</strong> '+esc(c.curated.evidence)+' · '+esc(c.curated.source_name)+' · '+esc(c.curated.source_version)+' · '+esc(c.curated.rights)+'</p>':'')+(c.artRecord?.Status_verificacao?'<p>'+esc(c.artRecord.Status_verificacao)+'</p>':'')+
    (c.celestial[0]?.artNote?'<p>'+esc(c.celestial[0].artNote)+'</p>':''));
  $('detailInfo').innerHTML=top+status+deckBlock(c)+mechanicsSummary(c)+
    section('Identificação — todos os campos da megalista','<div class="meta-pairs">'+metaPairs+'</div>')+
    (c.audit?section('Controle de auditoria','<div class="meta-pairs">'+Object.entries(c.audit).map(([k,v])=>pair(k,v)).join('')+'</div>'):'')+
    imageBlock+(c.driveFicha?section('Ficha complementar do Drive — sem homologação',
       '<div id="driveFichaConteudo">Carregando ficha estruturada...</div>'):'')+referenceDetails(c.extra)+(c.alternates.length?section('Registro alternativo — identidade a conciliar','<p class="notice">O repositório contém KP-S007 (“Animated Instruments (Animated Symphony)”), enquanto a megalista utiliza TF-085. São mantidos como registros distintos, sem mesclar regras, aguardando reconciliação editorial.</p>'+c.alternates.map(x=>rawData(x.id+' · '+x.nome,x,true)).join('')):'')+(c.research.length?section('Pesquisas aprofundadas existentes','<div class="linkrow">'+c.research.map(x=>makeLink(x.url,'Pesquisa '+x.path.split('/')[3]+' · '+x.path.split('/').pop())).join('')+'</div><p>Arquivos de pesquisa do repositório; a existência não implica ficha homologada.</p>'):'')+linksBlock(c)+
    section('Rastreabilidade','<p>Os dados provêm dos arquivos versionados no GitHub e preservam as classificações originais. A megalista provisória é distinta da homologação mecânica e jurídica da coleção.</p>');
  $('detailInfo').scrollTop=0;$('close').focus();
  if (c.driveFicha) carregarFichaDrive(c);
  if(!fromLink)history.replaceState(null,'','#c/'+index);
}
function closeCard(){
  closeImage();
  $('modal').classList.remove('open');$('modal').setAttribute('aria-hidden','true');document.body.classList.remove('lock');appState.active=null;
  if(location.hash.startsWith('#c/'))history.replaceState(null,'',location.pathname+location.search);
  if(appState.lastFocus?.isConnected)appState.lastFocus.focus();
  appState.lastFocus=null;
}
function navigate(delta){
  if(!appState.active)return;
  const all=currentList();
  let i=all.findIndex(x=>x.index===appState.active.index);
  if(i<0)i=0;
  i=(i+delta+all.length)%all.length;
  if(all[i])openCard(all[i].index);
}
function applyZoom(){
 const img=$('lightContent').querySelector('img');
 if(img)img.style.transform='translate('+appState.x+'px,'+appState.y+'px) scale('+appState.zoom+')';
 $('zoomPct').textContent=Math.round(appState.zoom*100)+'%';
}
function openImage(){
 const c=appState.active;if(!c?.art)return;
 appState.zoom=1;appState.x=0;appState.y=0;
 $('lightTitle').textContent=c.name;
 $('lightContent').innerHTML=safeImage(c.art,c.name);
 const img=$('lightContent').querySelector('img');
 if(img){
   img.draggable=false;
   img.addEventListener('pointerdown',e=>{if(appState.zoom<=1)return;appState.drag={x:e.clientX-appState.x,y:e.clientY-appState.y};img.setPointerCapture(e.pointerId)});
   img.addEventListener('pointermove',e=>{if(!appState.drag)return;appState.x=e.clientX-appState.drag.x;appState.y=e.clientY-appState.drag.y;applyZoom()});
   img.addEventListener('pointerup',()=>{appState.drag=null});
   img.addEventListener('pointercancel',()=>{appState.drag=null});
 }
 $('lightbox').classList.add('open');$('lightbox').setAttribute('aria-hidden','false');applyZoom();$('lightClose').focus();
}
function closeImage(){ $('lightbox').classList.remove('open');$('lightbox').setAttribute('aria-hidden','true'); }
function zoomBy(step){appState.zoom=Math.min(4,Math.max(1,Math.round((appState.zoom+step)*100)/100));if(appState.zoom===1){appState.x=0;appState.y=0}applyZoom()}
$('close').addEventListener('click',closeCard);
$('prev').addEventListener('click',()=>navigate(-1));
$('next').addEventListener('click',()=>navigate(1));
$('modal').addEventListener('click',e=>{if(e.target===$('modal'))closeCard()});
$('lightClose').addEventListener('click',closeImage);
$('lightbox').addEventListener('click',e=>{if(e.target===$('lightbox'))closeImage()});
$('zoomIn').addEventListener('click',()=>zoomBy(.25));
$('zoomOut').addEventListener('click',()=>zoomBy(-.25));
$('zoomReset').addEventListener('click',()=>{appState.zoom=1;appState.x=0;appState.y=0;applyZoom()});
$('lightbox').addEventListener('wheel',e=>{if(!$('lightbox').classList.contains('open'))return;e.preventDefault();zoomBy(e.deltaY>0?-.15:.15)},{passive:false});
document.addEventListener('keydown',e=>{
 if($('lightbox').classList.contains('open')){if(e.key==='Escape')closeImage();else if(e.key==='+'||e.key==='=')zoomBy(.25);else if(e.key==='-')zoomBy(-.25);return}
 if(!$('modal').classList.contains('open'))return;
 if(e.key==='Escape')closeCard();
 else if(e.key==='ArrowRight')navigate(1);
 else if(e.key==='ArrowLeft')navigate(-1);
});
for(const name of ['search','type','rarity','scope'])$(name).addEventListener(name==='search'?'input':'change',()=>render(true));
$('more').addEventListener('click',()=>{appState.limit+=60;render(false)});
async function getJSON(path){
 const r=await fetch(path,{cache:'no-cache'});
 if(!r.ok)throw Error(path+' retornou HTTP '+r.status);
 return r.json();
}
async function init(){
 try{
   const [mega,srd,visuais,ledger,celestial,aberracao,aberrSupports,deepResearch,curadoria,extraSheets,generatedArts,driveImport]=await Promise.all([
     getJSON('data/megalista-1320.json'), getJSON('data/fichas-607.json'),
     getJSON('data/imagens-607.json'), getJSON('data/auditoria-607.json'),
     getJSON('data/deck-celestial-40.json'),getJSON('data/deck-aberracao-40.json'),
     getJSON('data/suportes-aberracao.json'),getJSON('data/pesquisas-aprofundadas.json'),getJSON('data/curadoria-artes-20261015.json'),getJSON('data/fichas-referencia-verificadas.json'),getJSON('data/artes-geradas-20261015.json'),getJSON('data/drive-import-20261021.json')
   ]);
   const fichas=new Map(srd.fichas.map(x=>[x.id,x]));
   const imagens=new Map(visuais.records.map(x=>[x.ID,x]));
   const auditoria=new Map(ledger.records.map(x=>[x.ID,x]));
   const approvedArts=new Map(curadoria.approved.filter(x=>x.rating==='REFERENCIA_VISUAL_ACEITA').map(x=>[x.id,x]));
   const extraRecords=new Map(extraSheets.records.map(x=>[x.id,x]));
   const generatedById=new Map(generatedArts.records.filter(x=>x.principal&&x.catalog_id).map(x=>[x.catalog_id,x]));
   const generatedByName=new Map(generatedArts.records.filter(x=>x.principal&&x.catalog_name).map(x=>[norm(x.catalog_name),x]));
   const driveArtById = new Map(driveImport.artes.filter(x=>x.id_catalogo).map(x=>[x.id_catalogo,x]));
   const driveArtByName = new Map(driveImport.artes.filter(x=>!x.id_catalogo).map(x=>[norm(x.nome),x]));
   const driveFichaById = new Map(driveImport.fichas.map(x=>[x.id_catalogo,x]));
   const cByName=new Map(),aByName=new Map();
   for(const x of celestial.records){const n=norm(x.name);if(!cByName.has(n))cByName.set(n,[]);cByName.get(n).push(x);}
   const sp=new Map(aberrSupports.records.map(x=>[norm(x.nome),x]));
   for(const x of aberracao.records){const n=norm(x.NOME);if(!aByName.has(n))aByName.set(n,[]);x.support=sp.get(n)||null;aByName.get(n).push(x);}
   const list=mega.records.map((m,i)=>{
     const name=m.NOME, id=m['ID NO JOGO']||'';
     const f=id?fichas.get(id):null,im=id?imagens.get(id):null,deep=id?(deepResearch.records[id]||[]):[];
     const curated=id?approvedArts.get(id):null,extra=id?extraRecords.get(id):null;
     const generated=(id&&generatedById.get(id))||generatedByName.get(norm(name))||null;
     const cel=cByName.get(norm(name))||[],abe=aByName.get(norm(name))||[];
     const verifiedSource=im?.URL_imagem_direta && im?.Status_verificacao?.includes('MIME, dimensões e correspondência visual confirmados');
     const web=generated?.image_url || curated?.image_url || (cel[0]&&cel[0].art) || (verifiedSource?im.URL_imagem_direta:'');
     const driveArt=driveArtById.get(id)||(!id&&driveArtByName.get(norm(name)))||null;
    // Apenas IDs exatos podem receber arte de prévia na grade. Referências sem
    // ID canônico continuam somente no painel de detalhes, sem inventar ID.
    const existingArt=artSrc(web)?web:'';
    const artIsDrive=Boolean(!existingArt && id && driveArt?.id_catalogo===id &&
      driveArt?.direitos==='CRIADA_PELO_USUARIO_PUBLICACAO_AUTORIZADA_20261021' &&
      artSrc(driveArt.arquivo));
    const art=existingArt || (artIsDrive?driveArt.arquivo:'');
     const alternates=id==='TF-085'?[...srd.fichas.filter(x=>x.id==='KP-S007')]:[];
     const keyfields=[name,id,...alternates.map(x=>x.id),m.TIPO,m.FONTE,m.PUBLICAÇÃO,m.EDITORA,...(m['ALIASES CONSOLIDADOS']?[m['ALIASES CONSOLIDADOS']]:[])];
     return {index:i,name,nd:m.ND,rarity:m.RARIDADE,type:m.TIPO,meta:m,mechanics:f||null,artRecord:im||null,
       audit:id?auditoria.get(id)||null:null,celestial:cel,aberracao:abe,research:deep,alternates,curated,generated,extra,art,artIsDrive,
       driveArt,
       driveFicha:driveFichaById.get(id)||null,
       search:norm(keyfields.join(' '))};
   });
   if(list.length!==1320)throw Error('Esperados 1320 registros, recebidos '+list.length);
   appState.all=list;
   for(const t of [...new Set(list.map(x=>x.type))].sort((a,b)=>a.localeCompare(b,'pt-BR'))) {
     const option=document.createElement('option');option.value=t;option.textContent=t;$('type').append(option);
   }
   const nImg=list.filter(x=>x.art).length;
   const nInt=list.filter(x=>x.mechanics?.ficha_integral_texto_local).length;
   const nSupport=list.filter(x=>x.celestial.length||x.aberracao.some(a=>a.support)).length;
   stop('1.320 criaturas · '+fichas.size+' fichas mecânicas · '+nInt+' textos integrais locais · '+nImg+' artes e referências visuais · '+nSupport+' criaturas com suporte candidato · '+driveImport.artes.length+' artes autorais (publicação autorizada, identidade em revisão) e '+driveImport.fichas.length+' fichas complementares do Drive');
   render(true);
   const hash=decodeURIComponent(location.hash.slice(1));
   if(hash.startsWith('c/')){const idx=Number(hash.slice(2));if(Number.isInteger(idx)&&idx>=0&&idx<list.length)openCard(idx,true)}
 }catch(e){
   console.error('Falha ao carregar o catálogo',e);
   stop('Não foi possível carregar todos os dados do repositório.');
   $gallery.innerHTML='<div class="empty">Abra o catálogo por um servidor HTTP (GitHub Pages ou localhost) e confirme os arquivos da pasta data/.<p>'+esc(e.message)+'</p></div>';
 }
}
init();
