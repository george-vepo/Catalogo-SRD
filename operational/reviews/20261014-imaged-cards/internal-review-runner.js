// Audit runner executed only through explicitly supplied connected GitHub tools.
// Pin this file's Git blob SHA before evaluating in the calling client.
const R="george-vepo/SRD-Card-Game-607-Supervisor",D="operational/reviews/20261014-imaged-cards",BR="chatgpt/srd607-audit-imaged-cards-20261014";
const context=JSON.parse((await tools.mcp__GitHub__fetch_file({repository_full_name:R,path:D+"/all-395-context.json",ref:BR})).result.content);
function check(r,j){
 const st=j.statistics||j.estatisticas||{}, ab=st.ability_scores||st.atributos||{}, sp=st.speeds||st.deslocamentos_ft||st.deslocamentos||{}, m=j.mechanics||j.mecanicas||j;
 const sections=r.group==="a"?["traits","actions","bonus_actions","reactions","legendary_actions","lair_actions","spellcasting"]:r.group==="b"?["habilidades_passivas","ataques","acoes","acoes_bonus","reacoes","acoes_lendarias","conjuracoes"]:["tracos","acoes","ataques","acoes_bonus","reacoes","acoes_lendarias","conjuracao"];
 const sec=Object.fromEntries(sections.map(k=>[k,Array.isArray(m[k])?m[k].length:m[k]&&typeof m[k]==="object"?Object.keys(m[k]).length:0]));
 const bad=[],ca=st.armor_class??st.ca,hp=st.hit_points??st.pv;
 if(!(Number(ca)>0))bad.push("CA_AUSENTE");
 if(!(Number(hp)>0))bad.push("PV_AUSENTE");
 if(Object.values(ab).filter(Number.isFinite).length<6)bad.push("ATRIBUTOS_INCOMPLETOS");
 if(typeof sp==="object"&&!Object.keys(sp).length)bad.push("DESLOCAMENTO_AUSENTE");
 if(!Object.values(sec).some(x=>x>0))bad.push("MECANICAS_AUSENTES");
 if(/PENDENTE_ESTRUTURACAO_INTEGRAL|previous_summary_for_context|PENDENTE_PESQUISA|RESUMO_HERDADO/.test(JSON.stringify(m)))bad.push("PLACEHOLDER_MECANICO");
 const unknown=Array.isArray(j.campos_nao_confirmados)?j.campos_nao_confirmados.filter(x=>typeof x==="string"&&x.trim()):[];
 if(unknown.length)bad.push("CAMPOS_NAO_CONFIRMADOS");
 if(j.conflito_editorial&&String(j.conflito_editorial).length>5||String(j.estado_auditoria||"").startsWith("BLOQUEADA")||Array.isArray(j.edition_conflicts)&&j.edition_conflicts.length)bad.push("CONFLITO_EDITORIAL");
 const src=r.group==="a"?(j.mechanics_source_statblock_full===true||j.statblock_verification?.source_level_structured===true||j.audit?.statblock_fully_structured_from_secondary===true):r.group==="b"?j.inventario_acoes_completo===true:j.pesquisa_detalhada_completa_na_fonte_individual===true;
 if(!src)bad.push("INVENTARIO_SEM_COMPROVACAO_COMPLETUDE");
 const direct=j.image?.file_path||j.imagem?.arquivo||j.imagem?.path||null,phy=r.image_candidates.find(x=>x.path===direct),side=r.image_candidates.find(x=>x.path===r.manifest_image_path),sha=j.image?.git_blob_sha||j.imagem?.blob_sha||j.imagem?.sha_git;
 if(direct&&!phy)bad.push("IMAGEM_LINK_QUEBRADO");
 if(phy&&sha&&sha!==phy.sha)bad.push("IMAGEM_SHA_DIVERGENTE");
 const imageLink=phy?"DIRETO":side?"MANIFESTO":r.image_candidates.length?"SOMENTE_ARQUIVO_ID":"AUSENTE";
 return {id:r.id,name:r.name,group:r.group,record:r.record,record_sha:r.record_sha,
 mechanics:bad.some(x=>!x.startsWith("IMAGEM_"))?"NAO_COMPROVADA":"ESTRUTURADA_SEM_LACUNAS_DETECTADAS",source_detail:src,
 stats:{ca,hp,ability_count:Object.values(ab).filter(Number.isFinite).length,speed:typeof sp==="object"?Object.keys(sp).length:1},sections:sec,issues:bad,unknown_fields:unknown.slice(0,8),
 image:{link:imageLink,path:phy?.path||side?.path||null,direct_reference:direct,manifest_reference:r.manifest_image_path,blob_sha:(phy||side)?.sha||null,available:r.image_candidates.length},
 status:j.status||j.estado||j.estado_auditoria||"",editorial_approved:j.mecanica_integral_validada===true||j.mecanica_completa===true,integrated:j.integrada===true,pending_count:(j.outstanding||j.pendencias||[]).length};
}
const data=await Promise.all(context.rows.slice(S,S+N).map(async r=>{
 try {return check(r,JSON.parse((await tools.mcp__GitHub__fetch_blob({repository_full_name:R,blob_sha:r.record_sha})).result.content))}
 catch(e){return {id:r.id,error:String(e)}}
}));
const p=D+"/individual/records-"+String(S).padStart(3,"0")+"-"+String(S+data.length-1).padStart(3,"0")+".json";
const w=await tools.mcp__GitHub__create_file({repository_full_name:R,path:p,content:JSON.stringify({range:[S,S+data.length],snapshot:context.main_snapshot,records:data}),branch:BR,message:"audit(srd607): inspect individual statblocks "+(S+1)+"-"+(S+data.length)+" of 395"});
return {range:[S,S+data.length],path:p,commit:w.result.commit_sha,errors:data.filter(x=>x.error).length,mech_ok:data.filter(x=>x.mechanics==="ESTRUTURADA_SEM_LACUNAS_DETECTADAS").length,link:data.reduce((a,x)=>(a[x.image?.link]=(a[x.image?.link]||0)+1,a),{})};
