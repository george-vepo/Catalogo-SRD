from pathlib import Path
import json, csv, math, zipfile, re
from datetime import date
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'outputs'
OUT.mkdir(parents=True, exist_ok=True)
DATE = '2026-10-10'
IMAGE_VERIFY_DATE = '2026-10-09'
VERSION = '2.1.0'
LOT = '16-20'
BASE_JSON = ROOT / 'SRD_Card_Game_Fichas_607_Indice_e_Textos_Extraidos.json'
BASE_CSV = ROOT / 'SRD_Worker_Base_Pendencias_607.csv'
SOURCES_CSV = ROOT / 'SRD_Card_Game_Fichas_607_Fontes_Web_Lote2.csv'
IMAGES_CSV = ROOT / 'SRD_Card_Game_Referencia_URL_Imagens_607_v3.csv'


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))

def mod(v): return math.floor((v - 10) / 2)
def signed(n): return f'{n:+d}'
def ab_scores(scores):
    keys = ['FOR','DES','CON','INT','SAB','CAR']
    return {k:{'valor':v,'modificador':mod(v)} for k,v in zip(keys,scores)}
def tr(name, summary, **kw): return {'nome':name,'resumo_mecanico':summary,**kw}
def act(name, summary, **kw): return {'nome':name,'resumo_mecanico':summary,**kw}
def strip_internal_citations(value):
    if isinstance(value, dict):
        return {k:strip_internal_citations(v) for k,v in value.items() if k != 'citation'}
    if isinstance(value, list):
        return [strip_internal_citations(v) for v in value]
    return value

# Facts were transcribed as mechanics and paraphrased from the linked source pages.
# No source prose is copied into these external records.
EXTERNAL = {
'KP-S001': {
 'fonte_publicacao':'Tome of Beasts 1', 'editora_fonte':'Kobold Press / Open Design LLC', 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Gargantuan', 'tipo_fonte':'aberration', 'alinhamento':'chaotic evil', 'nd_fonte':'15', 'ca':18, 'ca_base':'natural armor', 'pv':248, 'formula_pv':'16d20 + 80',
 'deslocamento':{'walk_ft':10,'burrow_ft':30}, 'scores':[23,16,21,15,14,6],
 'salvaguardas':{}, 'pericias':{'Deception':8}, 'resistencias_dano':['bludgeoning de ataques não mágicos'], 'imunidades_dano':['acid'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['prone'],
 'sentidos':['darkvision 60 ft.','tremorsense 60 ft.'], 'percepcao_passiva':12, 'idiomas':['Common','Primordial','telepathy 60 ft.'], 'bonus_proficiencia':5,
 'tracos':[tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e outros efeitos mágicos.'), tr('Mordant Puppets','Pode gastar 8 horas para transformar um humanoide morto em fantoche controlado, com estatísticas de zombie; alcance máximo de 30 ft. e até 12 fantoches. Quando um fantoche é destruído, criaturas a até 5 ft. fazem salvaguarda de Destreza CD 18 ou sofrem 2d8 acid. Se a criatura morrer, os fantoches colapsam.')],
 'acoes':[act('Multiattack','Faz uma mordida e quatro tentáculos, ou quatro espinhos ácidos.'), act('Bite','Ataque corpo a corpo +11, alcance 5 ft.; 2d10+6 piercing e 4d8 acid.',ataque='+11',alcance='5 ft.',dano=[{'dados':'2d10+6','tipo':'piercing'},{'dados':'4d8','tipo':'acid'}]), act('Tentacle','Ataque corpo a corpo +11, alcance 20 ft.; 2d8+6 bludgeoning e agarra alvo Large ou menor (fuga CD 18). Cada tentáculo agarra um alvo.',ataque='+11',alcance='20 ft.',dano=[{'dados':'2d8+6','tipo':'bludgeoning'}],salvaguarda='escape DC 18'), act('Acid Spike','Ataque à distância +8, alcance 30/120 ft.; 2d6+3 piercing e 3d8 acid.',ataque='+8',alcance='30/120 ft.',dano=[{'dados':'2d6+3','tipo':'piercing'},{'dados':'3d8','tipo':'acid'}])],
 'acoes_bonus':[], 'reacoes':[act('Hidden Trap','Enquanto enterrado e imóvel coberto por terra, é indistinguível do terreno. Quando uma criatura entra no espaço que ocupa, pode usar a reação para fazer um ataque de Tentacle e remover a cobertura.')],
 'conjuracao':None, 'nota_tatica':'Emboscada subterrânea; pode usar a reação Hidden Trap.',
 'secoes_nao_listadas':['ações bônus','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.5esrd.com/database/creature/mordant-snare-3pp/', 'citation':'turn0view2'
},
'KP-S005': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC', 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Medium', 'tipo_fonte':'celestial', 'alinhamento':'neutral good', 'nd_fonte':'15', 'ca':15, 'ca_base':'', 'pv':202, 'formula_pv':'27d8 + 81',
 'deslocamento':{'walk_ft':40}, 'scores':[14,21,16,16,18,21],
 'salvaguardas':{'DEX':10,'WIS':9,'CHA':10}, 'pericias':{'Insight':9,'Perception':9}, 'resistencias_dano':['radiant','bludgeoning, piercing e slashing de ataques não mágicos'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','deafened','exhaustion','frightened'],
 'sentidos':['truesight 60 ft.'], 'percepcao_passiva':19, 'idiomas':['all','telepathy 120 ft.'], 'bonus_proficiencia':5,
 'tracos':[tr('Charlatan’s Bane','Percebe quando ouve uma mentira e tem vantagem em testes de Insight para detectar tentativa de engano.'), tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e outros efeitos mágicos.'), tr('Magic Weapons','Seus ataques com armas são mágicos.'), tr('Motion Blur','Depois de se mover pelo menos 10 ft. no turno, ataques contra ela têm desvantagem até o início do próximo turno.'), tr('Innate Spellcasting','Atributo de conjuração Carisma; CD 18; sem componentes verbais ou materiais.')],
 'acoes':[act('Multiattack','Usa Blasphemer’s Bane e depois faz três ataques.'), act('Sacred Fist','Ataque corpo a corpo +10, alcance 5 ft.; 2d8+5 bludgeoning e 3d8 radiant.',ataque='+10',alcance='5 ft.',dano=[{'dados':'2d8+5','tipo':'bludgeoning'},{'dados':'3d8','tipo':'radiant'}]), act('Sacred Bolt','Ataque mágico à distância +10, alcance 60 ft.; 5d8 radiant.',ataque='+10',alcance='60 ft.',dano=[{'dados':'5d8','tipo':'radiant'}]), act('Blasphemer’s Bane','Uma criatura visível a até 30 ft. faz salvaguarda de Sabedoria CD 18; em falha, não pode conjurar nem manter concentração até o início do próximo turno da yaojing.',salvaguarda='Wisdom DC 18'), act('Radiant Spin','Recarga 5–6. Criaturas a até 10 ft. fazem salvaguarda de Destreza CD 18; falha causa 5d8 bludgeoning + 5d8 radiant e empurra até 10 ft.; sucesso reduz o dano pela metade e evita o empurrão.',uso='Recharge 5–6',salvaguarda='Dexterity DC 18')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':{'atributo':'CHA','cd':18,'ataque_magia':None,'sem_componentes':['verbal','material'],'at_will':['detect evil and good','silence'],'3/day':['beacon of hope','bestow curse'],'1/day':['death ward','dispel evil and good']}, 'nota_tatica':'Pode bloquear conjuração/concentração com Blasphemer’s Bane antes de atacar.',
 'secoes_nao_listadas':['ações bônus','reações','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.5esrd.com/database/creature/yaojing/', 'citation':'turn2view2'
},
'TF-002': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC', 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Medium', 'tipo_fonte':'aberration', 'alinhamento':'neutral evil', 'nd_fonte':'1/2', 'ca':13, 'ca_base':'clockwork armor', 'pv':26, 'formula_pv':'4d8 + 8',
 'deslocamento':{'walk_ft':30,'fly_ft':30,'fly_hover':True,'swim_ft':30}, 'scores':[15,12,14,12,10,10],
 'salvaguardas':{}, 'pericias':{'Perception':2}, 'resistencias_dano':[], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','exhaustion','frightened','paralyzed','petrified','poisoned','prone'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':11, 'idiomas':['Deep Speech','Void Speech'], 'bonus_proficiencia':2,
 'tracos':[tr('Clockwork Encasement','O ser precisa permanecer na armadura mecânica e morre quando ela chega a 0 PV.'), tr('Immutable Form','A criatura e a armadura são imunes a efeitos que alterem a forma enquanto ela permanecer dentro da armadura.'), tr('Innate Spellcasting','Atributo Inteligência, CD 11, +3 para ataques mágicos; sem componentes materiais.')],
 'acoes':[act('Whirring Blades','Ataque corpo a corpo +4, alcance 5 ft.; 2d4+2 slashing.',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d4+2','tipo':'slashing'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':{'atributo':'INT','cd':11,'ataque_magia':'+3','sem_componentes':['material'],'at_will':['firebolt (1d10)'],'1/day':['fear']}, 'nota_tatica':'A ficha não informa multiataque; usa um ataque Whirring Blades.',
 'secoes_nao_listadas':['salvaguardas','ações bônus','reações','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.5esrd.com/database/creature/ahu-nixta-drudge/', 'citation':'turn2view3'
},
'TF-005': {
 'fonte_publicacao':'Tome of Beasts 3', 'editora_fonte':'Kobold Press / Open Design LLC', 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Medium', 'tipo_fonte':'aberration', 'alinhamento':'unaligned', 'nd_fonte':'2', 'ca':12, 'ca_base':'', 'pv':60, 'formula_pv':'8d8 + 24',
 'deslocamento':{'walk_ft':20,'swim_ft':60}, 'scores':[12,15,16,4,12,9],
 'salvaguardas':{}, 'pericias':{'Perception':3,'Stealth':4}, 'resistencias_dano':['acid','cold'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':13, 'idiomas':[], 'bonus_proficiencia':2,
 'tracos':[tr('Frozen to the Spot','Enquanto está sobre neve ou gelo, não pode ser movido contra a vontade.'), tr('Hold Breath','Pode prender a respiração por 90 minutos.')],
 'acoes':[act('Multiattack','Faz uma mordida, uma Toothy Maw e três ataques de tentáculo; pode substituir os três tentáculos por Reel.'), act('Bite','Ataque corpo a corpo +4, alcance 5 ft.; 2d4+2 piercing.',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d4+2','tipo':'piercing'}]), act('Toothy Maw','Ataque corpo a corpo +4, alcance 5 ft.; 2d6+2 piercing.',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d6+2','tipo':'piercing'}]), act('Tendril','Ataque corpo a corpo +4, alcance 15 ft.; agarra criatura Medium ou menor (escape CD 13). Cada tentáculo só pode manter uma criatura; dois ou mais tentáculos na mesma criatura também a deixam Restrained.',ataque='+4',alcance='15 ft.',salvaguarda='escape DC 13'), act('Reel','Puxa até 10 ft. cada criatura que esteja agarrada.')],
 'acoes_bonus':[act('Ice Slide','Se se mover pelo menos 10 ft. em linha reta sobre neve ou gelo no turno, pode deslizar até 40 ft.')], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Pode prender várias criaturas com tentáculos e aproximá-las com Reel.',
 'secoes_nao_listadas':['salvaguardas','imunidades a condições','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.5esrd.com/database/creature/birgemon-seal/', 'citation':'turn2view4'
},
'TF-447': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'construct', 'alinhamento':'', 'nd_fonte':'1', 'ca':15, 'ca_base':'natural armor', 'pv':32, 'formula_pv':'5d8 + 10; bloodied 16',
 'deslocamento':{'walk_ft':50}, 'scores':[16,10,14,2,12,6],
 'salvaguardas':{}, 'pericias':{'Perception':3}, 'resistencias_dano':[], 'imunidades_dano':['poison','damage from nonmagical, non-adamantine weapons'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','fatigue','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':13, 'idiomas':['understands its creator’s languages; cannot speak'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Immutable Form','Imune a efeitos que alterariam sua forma.'), tr('Keen Hearing and Smell','Vantagem em testes de Perception baseados em audição ou olfato.'), tr('Magic Resistance','Vantagem em salvaguardas contra magias e efeitos mágicos.'), tr('Constructed Nature','Não precisa respirar, alimentar-se ou dormir.')],
 'acoes':[act('Bite','Ataque corpo a corpo +5, alcance 5 ft.; 2d4+3 piercing; a criatura alvo faz salvaguarda de Força CD 13 ou cai Prone.',ataque='+5',alcance='5 ft.',dano=[{'dados':'2d4+3','tipo':'piercing'}],salvaguarda='Strength DC 13')],
 'acoes_bonus':[], 'reacoes':[act('Protective Bite','Quando uma criatura a até 5 ft. acerta o dono do guardião com ataque corpo a corpo, o guardião morde o atacante.')], 'conjuracao':None, 'nota_tatica':'Segue ordens do dono; sem ordens, permanece perto e ataca ameaças ao dono ou a si.',
 'secoes_nao_listadas':['salvaguardas','ações bônus','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.a5e.tools/node/1670', 'citation':'turn0view0'
},
'TF-311': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Small', 'tipo_fonte':'construct', 'alinhamento':'', 'nd_fonte':'2', 'ca':14, 'ca_base':'natural armor', 'pv':44, 'formula_pv':'8d6 + 16; bloodied 22',
 'deslocamento':{'walk_ft':15,'climb_ft':15}, 'scores':[6,16,14,1,6,1],
 'salvaguardas':{}, 'pericias':{'Perception':0}, 'pericias_bonus_dado':{'Perception':'1d8'}, 'resistencias_dano':[], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','deafened','exhaustion','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['blindsight 120 ft. (blind beyond range)'], 'percepcao_passiva':14, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Clockwork Nature','Não precisa de ar, alimento ou descanso e é imune a doença.'), tr('Immutable Form','Imune a efeitos que alterariam sua forma.'), tr('Clockwork Sights','Não sofre desvantagem por atacar à distância a até 5 ft. de um inimigo.'), tr('Rooted','Pode usar ação bônus para ancorar-se ou soltar-se de uma superfície. Ancorado, deslocamento 0; CD 20 Força para removê-lo. A heavy crossbow só pode ser usada quando ancorado.')],
 'acoes':[act('Multiattack','Faz um ataque com cada besta.'), act('Light Crossbow','Ataque à distância +5, alcance 80/320 ft.; 1d8+3 piercing.',ataque='+5',alcance='80/320 ft.',dano=[{'dados':'1d8+3','tipo':'piercing'}]), act('Heavy Crossbow','Ataque à distância +5, alcance 100/400 ft.; 1d10+3 piercing.',ataque='+5',alcance='100/400 ft.',dano=[{'dados':'1d10+3','tipo':'piercing'}])],
 'acoes_bonus':[act('Rooted','Ancorar ou soltar-se de uma superfície; ver traço.')], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'A Heavy Crossbow exige que esteja ancorado; a Light Crossbow não.',
 'secoes_nao_listadas':['salvaguardas','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1452', 'citation':'turn0view1'
},
'TF-429': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'construct', 'alinhamento':'', 'nd_fonte':'4', 'ca':18, 'ca_base':'natural armor', 'pv':60, 'formula_pv':'8d8 + 24; bloodied 30',
 'deslocamento':{'walk_ft':35}, 'scores':[16,12,16,1,6,1],
 'salvaguardas':{}, 'pericias':{'Athletics':5,'Perception':0,'Survival':0}, 'pericias_bonus_dado':{'Perception':'1d4','Survival':'1d4'}, 'resistencias_dano':[], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','deafened','exhaustion','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['blindsight 120 ft. (blind beyond range)'], 'percepcao_passiva':12, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('False Appearance','Enquanto imóvel, parece uma armadura comum.'), tr('Clockwork Nature','Não precisa de ar, alimento ou descanso e é imune a doença.'), tr('Immutable Form','Imune a efeitos que alterariam sua forma.')],
 'acoes':[act('Multiattack','Faz três ataques.'), act('Halberd','Ataque corpo a corpo +5, alcance 10 ft.; 1d10+3 slashing.',ataque='+5',alcance='10 ft.',dano=[{'dados':'1d10+3','tipo':'slashing'}]), act('Calculated Sweep','Faz um ataque corpo a corpo contra cada criatura escolhida a até 10 ft.; em acerto crítico, alvo faz salvaguarda de Força CD 13 ou cai Prone.',salvaguarda='Strength DC 13')],
 'acoes_bonus':[act('Overclock','Recarga 5–6; usa a ação Dash.',uso='Recharge 5–6')], 'reacoes':[act('Parry','Soma 2 à CA contra um ataque corpo a corpo que o acertaria.')], 'conjuracao':None, 'nota_tatica':'Persegue intrusos por até uma milha da área que guarda.',
 'secoes_nao_listadas':['salvaguardas','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1453', 'citation':'turn3view0'
},
'TF-442': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'construct', 'alinhamento':'', 'nd_fonte':'4', 'ca':16, 'ca_base':'natural armor', 'pv':66, 'formula_pv':'7d10 + 28; bloodied 33',
 'deslocamento':{'walk_ft':30}, 'scores':[18,8,18,1,10,1],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','deafened','exhaustion','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['blindsight 60 ft. (blind beyond range)'], 'percepcao_passiva':10, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':14,
 'tracos':[tr('Bludgeoning Weakness','Quando recebe mais de 10 de dano bludgeoning de um único ataque, cai Prone.'), tr('False Appearance','Enquanto imóvel, parece uma estátua normal.'), tr('Spell-created','CD 19 para destruir com dispel magic.')],
 'acoes':[act('Smash','Ataque corpo a corpo +6, alcance 5 ft.; 2d10+4 bludgeoning.',ataque='+6',alcance='5 ft.',dano=[{'dados':'2d10+4','tipo':'bludgeoning'}]), act('Spit Flame','Ataque mágico à distância +2, alcance 60 ft.; 1d10 fire; objeto inflamável não usado ou carregado também pega fogo.',ataque='+2',alcance='60 ft.',dano=[{'dados':'1d10','tipo':'fire'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Objetos animados costumam permanecer imóveis até alguém aproximar-se ou tocá-los.',
 'secoes_nao_listadas':['salvaguardas','ações bônus','reações','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/2266', 'citation':'turn3view1'
},
'TF-456': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'construct', 'alinhamento':'', 'nd_fonte':'4', 'ca':14, 'ca_base':'', 'pv':67, 'formula_pv':'9d8 + 27; bloodied 33',
 'deslocamento':{'walk_ft':40}, 'scores':[16,18,16,12,14,16],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['bludgeoning','piercing'], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','fatigue','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':12, 'idiomas':['understands its creator’s languages; cannot speak'], 'bonus_proficiencia':2, 'maneuver_dc':14,
 'tracos':[tr('Flammable','Depois de receber dano de fogo, sofre 1d10 de dano de fogo contínuo; uma criatura pode gastar uma ação para apagar as chamas.'), tr('Spell-created','CD 19 em dispel magic para desativar. Fica inanimado por uma hora, salvo se o corpo for destruído.')],
 'acoes':[act('Multiattack','Usa Scare e faz dois ataques de Claw.'), act('Claw','Ataque corpo a corpo +6, alcance 5 ft.; 1d8+4 slashing e 1d6 necrotic.',ataque='+6',alcance='5 ft.',dano=[{'dados':'1d8+4','tipo':'slashing'},{'dados':'1d6','tipo':'necrotic'}]), act('Scare','Criaturas escolhidas que veem o espantalho a até 30 ft. fazem salvaguarda de Sabedoria CD 13; falha causa frightened por 1 minuto, com novo teste ao fim de cada turno. Sucesso ou término concede imunidade por 24 horas.',salvaguarda='Wisdom DC 13'), act('Fire Breath','Recarga 4–6; cone de 30 ft.; salvaguarda de Destreza CD 13, 4d6 fire em falha, metade em sucesso.',uso='Recharge 4–6',salvaguarda='Dexterity DC 13'), act('Pumpkin Head','1/dia; arremessa a cabeça a até 60 ft.; criaturas a até 20 ft. fazem salvaguarda de Destreza CD 13 ou sofrem 6d6 fire, metade em sucesso. Perde a cabeça e Fire Breath até completar descanso longo.',uso='1/day',salvaguarda='Dexterity DC 13'), act('Invisibility','1/dia; fica invisível por 1 hora ou até atacar ou usar Scare, Fire Breath ou Pumpkin Head.',uso='1/day')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'A página recomenda Scare primeiro, Fire Breath quando disponível e Pumpkin Head quando bloodied.',
 'secoes_nao_listadas':['salvaguardas','ações bônus','reações','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1783', 'citation':'turn3view2'
},
'TF-444': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'construct', 'alinhamento':'', 'nd_fonte':'5', 'ca':9, 'ca_base':'', 'pv':93, 'formula_pv':'11d8 + 44; bloodied 46',
 'deslocamento':{'walk_ft':30}, 'scores':[18,8,18,6,10,5],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['lightning','poison','damage from nonmagical, non-adamantine weapons'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','fatigue','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':10, 'idiomas':['understands its creator’s languages; cannot speak'], 'bonus_proficiencia':3, 'maneuver_dc':15,
 'tracos':[tr('Berserk','Quando começa o turno bloodied, rola d6; em 6 torna-se berserk e ataca a criatura mais próxima visível (ou objeto se não alcança ninguém). Continua assim até destruído ou curado ao máximo; o criador pode usar uma ação e teste de Persuasion CD 15 para acalmá-lo.'), tr('Fire Fear','Ao receber dano de fogo, fica rattled até o fim do turno seguinte.'), tr('Immutable Form','Imune a efeitos que alterariam sua forma.'), tr('Lightning Absorption','Dano de lightning recebido restaura PV em vez de causar dano.'), tr('Magic Resistance','Vantagem em salvaguardas contra magias e efeitos mágicos.'), tr('Constructed Nature','Não precisa respirar, alimentar-se ou dormir.')],
 'acoes':[act('Multiattack','Faz dois ataques de Slam.'), act('Slam','Ataque corpo a corpo +7, alcance 5 ft.; 2d8+4 bludgeoning.',ataque='+7',alcance='5 ft.',dano=[{'dados':'2d8+4','tipo':'bludgeoning'}]), act('Hurl Object','Ataque à distância +7, alcance 20/60 ft.; 4d6+4 bludgeoning.',ataque='+7',alcance='20/60 ft.',dano=[{'dados':'4d6+4','tipo':'bludgeoning'}]), act('Lightning Bolt','1/dia quando bloodied; linha de 80 ft. por 5 ft.; criaturas fazem salvaguarda de Destreza CD 15, 8d6 lightning em falha, metade em sucesso.',uso='1/day; while bloodied',salvaguarda='Dexterity DC 15')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Prefere Slam; usa Lightning Bolt quando disponível e lança objetos apenas se não alcança inimigos.',
 'secoes_nao_listadas':['salvaguardas','ações bônus','reações','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1669', 'citation':'turn3view3'
},
'TF-514': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'elemental', 'alinhamento':'', 'nd_fonte':'2', 'ca':15, 'ca_base':'natural armor', 'pv':45, 'formula_pv':'6d8 + 18; bloodied 22',
 'deslocamento':{'walk_ft':30,'fly_ft':60}, 'scores':[14,10,16,8,14,8],
 'salvaguardas':{'STR':4,'CON':5}, 'pericias':{'Perception':4}, 'resistencias_dano':['piercing e slashing de armas não mágicas e não adamantinas'], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue','petrified','poisoned','unconscious'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Terran'], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[tr('False Appearance','Imóvel, parece uma estátua comum.'), tr('Elemental Nature','Não precisa respirar, alimentar-se ou dormir.')],
 'acoes':[act('Multiattack','Faz um ataque de Bite e um de Claws.'), act('Bite','Ataque corpo a corpo +4, alcance 5 ft.; 1d6+2 piercing.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d6+2','tipo':'piercing'}]), act('Claws','Ataque corpo a corpo +4, alcance 5 ft.; 1d6+2 slashing, ou 2d6+2 se começou o turno a pelo menos 20 ft. acima do alvo.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d6+2 (ou 2d6+2)','tipo':'slashing'}]), act('Rock','Ataque à distância +4, alcance 20/60 ft.; 2d6+2 bludgeoning.',ataque='+4',alcance='20/60 ft.',dano=[{'dados':'2d6+2','tipo':'bludgeoning'}]), act('Spit','Recarga 5–6; linha de água de 5 por 30 ft.; salvaguarda de Força CD 12, 3d6 bludgeoning e empurrão de até 15 ft. em falha, metade do dano em sucesso.',uso='Recharge 5–6',salvaguarda='Strength DC 12')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Prefere atacar de cima e usar o mergulho para ampliar o dano de Claws.',
 'secoes_nao_listadas':['ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/1618', 'citation':'turn6view2'
},
'TF-360': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Huge', 'tipo_fonte':'ooze', 'alinhamento':'', 'nd_fonte':'7', 'ca':6, 'ca_base':'', 'pv':136, 'formula_pv':'13d12 + 52; bloodied 68',
 'deslocamento':{'walk_ft':30,'swim_ft':15}, 'scores':[16,2,18,1,6,1],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','deafened','fatigue','frightened','prone'],
 'sentidos':['blindsight 60 ft. (blind beyond range)'], 'percepcao_passiva':8, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Engulfing Body','Uma criatura que entra no espaço da parede sofre os efeitos de Engulf.'), tr('Sunlight Sensitivity','Sob luz solar, tem desvantagem em ataques.'), tr('Transparent','Imóvel, só é percebida por criatura desavisada que passe em Perception CD 15.'), tr('Ooze Nature','Não precisa respirar nem dormir.')],
 'acoes':[act('Pseudopod','Ataque corpo a corpo +5, alcance 5 ft.; 3d6 acid e 2d6+2 bludgeoning.',ataque='+5',alcance='5 ft.',dano=[{'dados':'3d6','tipo':'acid'},{'dados':'2d6+2','tipo':'bludgeoning'}]), act('Engulf','Move até 30 ft. e pode atravessar espaços de criaturas Large ou menores. Cada criatura no caminho faz salvaguarda de Destreza CD 13; se não sabia da parede, tem desvantagem. Em sucesso, pode usar reação para se mover metade do deslocamento sem provocar ataques de oportunidade; se não se mover, é engolida. Engolida: sofre 3d6 acid, fica sem respirar e Restrained, recebe 3d6 acid no início de cada turno da parede, fica visível mas com total cover e se move com a parede. Escapa com ação e teste de Força CD 13; sucesso a coloca a até 5 ft. Um aliado adjacente pode tentar o mesmo teste, mas sofre 3d6 acid + 2d6+2 bludgeoning.',salvaguarda='Dexterity DC 13; escape Strength DC 13')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Move continuamente e aguarda imóvel que criaturas entrem em seu espaço; recua se estiver cheia ou exposta à luz solar.',
 'secoes_nao_listadas':['salvaguardas','perícias','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/1756', 'citation':'turn6view3'
},
'TF-461': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'1/4', 'ca':13, 'ca_base':'natural armor; 10 enquanto prone', 'pv':11, 'formula_pv':'2d8 + 2; bloodied 5',
 'deslocamento':{'walk_ft':30,'burrow_ft':10}, 'scores':[14,12,12,2,14,8],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['acid'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['tremorsense 30 ft.'], 'percepcao_passiva':12, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[],
 'acoes':[act('Bite','Ataque corpo a corpo +4, alcance 5 ft.; 1d6+2 slashing.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d6+2','tipo':'slashing'}]), act('Claws','Ataque corpo a corpo +4, alcance 5 ft.; 1d4+2 slashing contra alvo Medium ou menor, que faz teste de Força CD 12 ou cai Prone. Se já estiver Prone, o spawn pode andar metade do deslocamento arrastando-o.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d4+2','tipo':'slashing'}],salvaguarda='Strength DC 12'), act('Acid Spit','Ataque à distância +3, alcance 30 ft.; 1d8 acid.',ataque='+3',alcance='30 ft.',dano=[{'dados':'1d8','tipo':'acid'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Ataca em grupo; algumas crias arrastam uma vítima enquanto outras mordem e cospem ácido.',
 'secoes_nao_listadas':['salvaguardas','perícias','traços','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/1439', 'citation':'turn6view4'
},
'TF-209': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'3', 'ca':14, 'ca_base':'natural armor', 'pv':85, 'formula_pv':'10d10 + 30; bloodied 42',
 'deslocamento':{'walk_ft':30,'fly_ft':50}, 'scores':[16,14,16,8,12,8],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':11, 'idiomas':['Common'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[],
 'acoes':[act('Multiattack','Faz um ataque Bite e um Claws.'), act('Bite','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 piercing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'piercing'}]), act('Claws','Ataque corpo a corpo +5, alcance 5 ft.; 2d4+3 slashing. Se avançou 20 ft. em linha reta antes do ataque, o alvo faz salvaguarda de Força CD 13 ou cai Prone.',ataque='+5',alcance='5 ft.',dano=[{'dados':'2d4+3','tipo':'slashing'}],salvaguarda='Strength DC 13'), act('Tail','Ataque corpo a corpo +5, alcance 10 ft.; 1d8+3 piercing.',ataque='+5',alcance='10 ft.',dano=[{'dados':'1d8+3','tipo':'piercing'}]), act('Tail Spike Volley','4/dia; linha de 5 por 60 ft.; salvaguarda de Destreza CD 12, 4d6 piercing em falha ou metade em sucesso. Quem sofre dano também sofre 1d10 de dano contínuo por sangramento, removido por uma ação para retirar espinhos.',uso='4/day',salvaguarda='Dexterity DC 12')],
 'acoes_bonus':[], 'reacoes':[act('Tail Whip','Quando uma criatura que vê o adamanticore o acerta com ataque corpo a corpo, pode atacar com a cauda; se acertar, voa até metade do deslocamento de voo sem provocar ataque de oportunidade daquele atacante.')], 'conjuracao':None, 'nota_tatica':'Abre à distância com uma saraivada de espinhos, depois alterna ataques aéreos de cauda e investida de garras.',
 'secoes_nao_listadas':['salvaguardas','perícias','traços','ações bônus','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/2280', 'citation':'turn7view0'
},
'TF-434': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'construct', 'alinhamento':'', 'nd_fonte':'10', 'ca':20, 'ca_base':'natural armor; 14 enquanto prone', 'pv':115, 'formula_pv':'11d10 + 55; bloodied 57',
 'deslocamento':{'walk_ft':20}, 'scores':[20,8,20,1,6,1],
 'salvaguardas':{}, 'pericias':{'Perception':2}, 'resistencias_dano':[], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','deafened','exhaustion','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['blindsight 60 ft. (blind beyond range)'], 'percepcao_passiva':12, 'idiomas':[], 'bonus_proficiencia':4, 'maneuver_dc':17,
 'tracos':[tr('Clockwork Nature','Não precisa respirar, alimentar-se ou descansar e é imune a doença.'), tr('Immutable Form','Imune a efeitos que alterariam sua forma.')],
 'acoes':[act('Crush','Move até o deslocamento em linha reta e tenta ocupar espaços de criaturas Large ou menores. Alvo escolhe salvaguarda de Destreza ou Força CD 17. Sucesso em Força encerra o movimento; sucesso em Destreza permite usar reação para mover metade do deslocamento sem provocar ataques de oportunidade. Na primeira entrada em espaço de criatura por turno, derruba e causa 10d8+5 bludgeoning; a criatura fica Prone dentro do espaço.'), act('Ram','Ataque corpo a corpo +9, alcance 5 ft.; 4d8+5 bludgeoning, mais 4d8 se avançou 20 ft. em linha reta antes do ataque.',ataque='+9',alcance='5 ft.',dano=[{'dados':'4d8+5 (mais 4d8 após investida)','tipo':'bludgeoning'}])],
 'acoes_bonus':[act('Overclock','Recarga 5–6; usa a ação Dash.',uso='Recharge 5–6')], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Segue instruções programadas e esmaga intrusos; pode usar Overclock para continuar o avanço.',
 'secoes_nao_listadas':['salvaguardas','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/1455', 'citation':'turn7view1'
},
'TF-523': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'humanoid', 'alinhamento':'', 'nd_fonte':'4', 'ca':14, 'ca_base':'Unarmored Defense (10 + DEX + WIS)', 'pv':75, 'formula_pv':'10d8 + 30; bloodied 37',
 'deslocamento':{'walk_ft':40}, 'scores':[16,14,16,10,14,10],
 'salvaguardas':{'STR':5,'DEX':4}, 'pericias':{'Athletics':5,'Intimidation':2}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':[], 'percepcao_passiva':12, 'idiomas':['any one'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Unarmored Defense','CA igual a 10 + modificador de Destreza + modificador de Sabedoria.')],
 'acoes':[act('Multiattack','Faz três ataques com os punhos.'), act('Fists','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 bludgeoning.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'bludgeoning'}])],
 'acoes_bonus':[act('Haymaker','1/dia; ataque de punho causa 2d6 de dano extra se acertar.',uso='1/day'), act('Head Shot','1/dia; após acertar com punho, alvo faz salvaguarda de Constituição CD 13 ou fica Stunned até o fim do próximo turno do pugilista.',uso='1/day',salvaguarda='Constitution DC 13')],
 'reacoes':[act('Opportune Jab','Quando uma criatura tenta agarrar o pugilista, ele ataca-a com os punhos.')], 'conjuracao':None, 'nota_tatica':'Luta com três golpes, podendo gastar usos diários para ampliar dano ou atordoar.',
 'secoes_nao_listadas':['perícias adicionais','resistências e imunidades','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/1893', 'citation':'turn7view2'
},
'TF-477': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'1/2', 'ca':13, 'ca_base':'', 'pv':22, 'formula_pv':'4d8 + 4; bloodied 11',
 'deslocamento':{'walk_ft':50,'climb_ft':40}, 'scores':[14,16,12,6,14,10],
 'salvaguardas':{}, 'pericias':{'Perception':4,'Stealth':5}, 'pericias_bonus_dado':{'Stealth':'1d4'}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Keen Smell','Vantagem em testes de Perception que dependem do olfato.')],
 'acoes':[act('Claws (True Form Only)','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 slashing. Se avançar pelo menos 20 ft. em linha reta em direção ao alvo antes do ataque, o alvo faz salvaguarda de Força CD 12 ou cai Prone.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'slashing'}],salvaguarda='Strength DC 12'), act('Bite','Ataque corpo a corpo +5, alcance 5 ft.; 1d4+3 piercing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d4+3','tipo':'piercing'}])],
 'acoes_bonus':[act('Opportune Bite (True Form Only)','Faz um ataque Bite contra uma criatura Prone.'), act('Shapeshift','Muda entre gato Tiny e forma verdadeira semelhante a pantera; as estatísticas permanecem iguais exceto o tamanho. Retorna à forma verdadeira ao morrer.')],
 'reacoes':[], 'conjuracao':None, 'nota_tatica':'A forma verdadeira habilita Claws e Opportune Bite; o ataque bônus aproveita alvos Prone.',
 'secoes_nao_listadas':['salvaguardas','resistências e imunidades','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/1964', 'citation':'turn13view0'
},
'TF-207': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'4', 'ca':12, 'ca_base':'natural armor', 'pv':136, 'formula_pv':'16d10 + 48; bloodied 68',
 'deslocamento':{'walk_ft':40,'climb_ft':40}, 'scores':[18,12,16,8,12,16],
 'salvaguardas':{}, 'pericias':{'Perception':3,'Stealth':3}, 'resistencias_dano':[], 'imunidades_dano':['cold'], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':[], 'percepcao_passiva':13, 'idiomas':['Yeti'], 'bonus_proficiencia':2, 'maneuver_dc':14, 'tags':['Elite'],
 'tracos':[tr('Camouflage','Vantagem em Stealth para se esconder em terreno nevado.'), tr('Fire Fear','Ao receber dano de fogo, fica rattled até o fim do próximo turno.'), tr('Storm Sight','A visão não é obscurecida por condições climáticas.')],
 'acoes':[act('Multiattack','Usa Chilling Gaze e faz dois ataques de Claw.'), act('Claw','Ataque corpo a corpo +6, alcance 10 ft.; 2d4+4 slashing.',ataque='+6',alcance='10 ft.',dano=[{'dados':'2d4+4','tipo':'slashing'}]), act('Chilling Gaze','Uma criatura a até 30 ft. sem imunidade a dano cold faz salvaguarda de Constituição CD 13; falha: 3d6 cold e Paralyzed por 1 minuto. Repete o teste no fim de cada turno, encerrando o efeito no sucesso. Sucesso ou encerramento concede imunidade a Chilling Gaze por 24 horas.',salvaguarda='Constitution DC 13')],
 'acoes_bonus':[act('Elite Recovery (somente bloodied)','Encerra um efeito negativo que o afeta; pode usar mesmo inconsciente ou incapacitado se tiver ao menos 1 PV.'), act('Cold Breath (somente bloodied)','Cone de 30 ft.; salvaguarda de Constituição CD 13, 6d10 cold em falha ou metade em sucesso.',salvaguarda='Constitution DC 13'), act('Blizzard (1/day; somente bloodied)','Cria nevasca mágica em raio de 500 ft. por 10 minutos ou até morrer; área é terreno difícil, visibilidade reduzida a 20 ft., e criatura que não se move no próprio turno sofre 2d6 cold.',uso='1/day; somente bloodied'), act('Roar (1/day; somente bloodied)','Criaturas escolhidas que ouvem o rugido a até 120 ft. fazem salvaguarda de Carisma CD 13; falha: Frightened por 1 minuto e Paralyzed enquanto assim. Repetem o teste ao fim de cada turno.',uso='1/day; somente bloodied',salvaguarda='Charisma DC 13')],
 'reacoes':[], 'conjuracao':None, 'nota_tatica':'A ficha marca o monstro como Elite; ações bônus especiais só podem ser usadas enquanto bloodied.',
 'secoes_nao_listadas':['salvaguardas','resistências além da imunidade a cold','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/1826', 'citation':'turn13view1'
},
'TF-474': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'6', 'ca':17, 'ca_base':'natural armor', 'pv':90, 'formula_pv':'12d10 + 24; bloodied 45',
 'deslocamento':{'walk_ft':40,'climb_ft':40}, 'scores':[20,14,14,2,14,5],
 'salvaguardas':{}, 'pericias':{'Stealth':5}, 'resistencias_dano':['damage from nonmagical weapons'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':12, 'idiomas':[], 'bonus_proficiencia':3, 'maneuver_dc':16,
 'tracos':[tr('Camouflage','Vantagem em Stealth para se esconder em terreno rochoso.'), tr('Spider Climb','Usa o deslocamento de escalada inclusive em superfícies difíceis e tetos invertidos.')],
 'acoes':[act('Tentacles','Ataque corpo a corpo +8, alcance 20 ft., um ou dois alvos; 4d8+5 bludgeoning. Criatura atingida faz salvaguarda de Força CD 16 ou é puxada para até 5 ft., agarrada (escape CD 16) e Restrained enquanto o agarrão durar. Pode agarrar até duas criaturas Medium ou menores, ou uma Large.',ataque='+8',alcance='20 ft.',dano=[{'dados':'4d8+5','tipo':'bludgeoning'}],salvaguarda='Strength DC 16; escape DC 16')],
 'acoes_bonus':[act('Beak','Ataque corpo a corpo +8, alcance 5 ft. contra uma criatura agarrada pelo grick; 2d8+5 piercing.',ataque='+8',alcance='5 ft.',dano=[{'dados':'2d8+5','tipo':'piercing'}])],
 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Embosca de paredes ou tetos, puxa alvos e usa Beak contra criatura agarrada.',
 'secoes_nao_listadas':['salvaguardas','imunidades e vulnerabilidades','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/1661', 'citation':'turn13view2'
},
'TF-226': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'8', 'ca':16, 'ca_base':'natural armor', 'pv':85, 'formula_pv':'10d10 + 30; bloodied 42',
 'deslocamento':{'walk_ft':40,'swim_ft':40}, 'scores':[16,16,16,16,14,16],
 'salvaguardas':{'DEX':6,'CON':6,'WIS':5,'CHA':6}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':12, 'idiomas':['Abyssal','Celestial','Common'], 'bonus_proficiencia':3, 'maneuver_dc':14,
 'tracos':[tr('Amphibious','Respira ar e água.'), tr('Magic Resistance','Vantagem em salvaguardas contra magias e efeitos mágicos.')],
 'acoes':[act('Bite','Ataque corpo a corpo +6, alcance 5 ft.; 2d6+3 piercing e alvo faz salvaguarda de Constituição CD 15, sofrendo 8d6 poison em falha ou metade em sucesso.',ataque='+6',alcance='5 ft.',dano=[{'dados':'2d6+3','tipo':'piercing'},{'dados':'8d6','tipo':'poison; salvaguarda reduz à metade'}],salvaguarda='Constitution DC 15'), act('Hypnotic Pattern (3rd-Level; V, Concentration)','Ponto a até 120 ft.; criaturas que veem o padrão a até 10 ft. fazem salvaguarda de Sabedoria CD 14; falha: Charmed por 1 minuto, Incapacitated e Speed 0. Dano ou uma ação de outra criatura para sacudir encerra o efeito.',salvaguarda='Wisdom DC 14'), act('Lightning Bolt (3rd-Level; V)','Linha de 100 ft. por 5 ft.; salvaguarda de Destreza CD 14, 8d6 lightning em falha ou metade em sucesso.',salvaguarda='Dexterity DC 14'), act('Blight (4th-Level; V, Concentration)','Criatura viva ou planta a até 30 ft. faz salvaguarda de Constituição CD 14; 8d8 necrotic em falha ou metade em sucesso. Plantas têm desvantagem e sofrem dano máximo; planta não mágica morre.',salvaguarda='Constitution DC 14'), act('Multiattack','Conjura uma magia e usa Vampiric Bite.'), act('Vampiric Bite','Faz ataque de Bite; se acertar e o alvo falhar na salvaguarda contra poison, naga ganha PV temporários iguais ao dano poison causado.')],
 'acoes_bonus':[], 'reacoes':[act('Shield (1st-Level; V)','Quando atingida por ataque ou alvo de magic missile, ganha +5 CA inclusive contra ataque gatilho e imunidade a magic missile até o início do próximo turno.')],
 'conjuracao':{'nivel_conjurador':9,'atributo':'INT','cd':14,'ataque_magia':None,'componentes':['somente componentes vocais'],'cantrips_at_will':['mage hand','minor illusion'],'slots':{'1st':{'slots':4,'spells':['charm person','shield','false life']},'2nd':{'slots':3,'spells':['detect thoughts','levitate','locate object']},'3rd':{'slots':3,'spells':['hypnotic pattern','lightning bolt']},'4th':{'slots':3,'spells':['arcane eye','blight']},'5th':{'slots':1,'spells':['dominate person','scrying']}}},
 'nota_tatica':'O texto tático da página cita Spirit Naga; a seção estatística consultada está intitulada Accursed Spirit Naga e seus ataques foram registrados sem importar ações da Spirit Naga.',
 'secoes_nao_listadas':['perícias','resistências e vulnerabilidades','ações bônus','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.a5e.tools/node/1745', 'citation':'turn10view0'
},
'TF-515': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'fiend', 'alinhamento':'', 'nd_fonte':'4', 'ca':14, 'ca_base':'natural armor', 'pv':78, 'formula_pv':'12d8 + 24; bloodied 39',
 'deslocamento':{'walk_ft':30,'fly_ft':60,'fly_true_form_only':True}, 'scores':[10,16,14,14,16,20],
 'salvaguardas':{}, 'pericias':{'Deception':7,'Insight':5,'Perception':5,'Persuasion':7,'Stealth':5}, 'pericias_bonus_dado':{'Deception':'1d4','Persuasion':'1d4'}, 'resistencias_dano':['cold','fire','lightning','poison','damage from nonmagical weapons'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':15, 'idiomas':['Abyssal','Common','Infernal','telepathy 60 ft.'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Cloaked Mind','Salvaguarda de Carisma CD 15 contra efeito de adivinhação que detecte ínferos ou alinhamento; em sucesso, sua natureza não é detectada.'), tr('Evil','Emana uma aura Evil.'), tr('Telepathic Bond','Comunica-se telepaticamente a qualquer distância com criatura Charmed, inclusive entre planos.')],
 'acoes':[act('Claw (Malcubus Form Only)','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 slashing e 2d6 necrotic.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'slashing'},{'dados':'2d6','tipo':'necrotic'}]), act('Charm','Humanoide no mesmo plano a até 30 ft. faz salvaguarda de Sabedoria CD 15; falha: Charmed por 1 dia ou até a criatura encantar outra, obedecendo comandos. Repete ao sofrer dano ou receber comando suicida; sucesso ou término concede imunidade por 24h.'), act('Draining Kiss','Criatura willing ou Charmed faz salvaguarda de Constituição CD 15; 4d10 psychic em falha ou metade em sucesso, reduzindo máximo de PV pelo mesmo valor até descanso longo; malcubus recupera PV iguais. Se alvo estava Charmed, condição termina.',salvaguarda='Constitution DC 15'), act('Etherealness','Viaja magicamente ao plano etéreo; dali vê e ouve o plano material e pode tornar-se audível e vagamente visível. Retorna ao material usando ação se um humanoide o convidar.'), act('Dream (1/day)','No plano etéreo, toca humanoide adormecido no plano material sem proteção de magic circle ou proteção semelhante. Se o sonho durar 1h, alvo não obtém benefício do descanso e o malcubus pode usar Charm mesmo entre planos.',uso='1/day')],
 'acoes_bonus':[act('Shapeshift','Muda entre forma verdadeira e forma humanoide Medium ou Small; estatísticas não mudam exceto tamanho e deslocamento. Voo só na forma verdadeira; equipamento não muda; retorna à forma verdadeira ao morrer.')],
 'reacoes':[act('Living Shield','Quando criatura visível acerta o malcubus, ele pode ordenar a criatura Charmed adjacente a trocar de lugar usando sua reação; o ataque acerta a criatura Charmed.')], 'conjuracao':None,
 'nota_tatica':'A ação Claw é exclusiva da forma de malcubus; a página descreve voo apenas nessa forma.',
 'secoes_nao_listadas':['salvaguardas','vulnerabilidades','ações lendárias','ações míticas','ações de covil','lista de magias'],
 'url':'https://www.a5e.tools/node/1723', 'citation':'turn10view2'
},
'TF-463': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Tiny', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'1/8', 'ca':12, 'ca_base':'', 'pv':3, 'formula_pv':'1d4 + 1; bloodied 1',
 'deslocamento':{'walk_ft':20,'burrow_ft':5,'climb_ft':15,'swim_ft':15}, 'scores':[3,14,12,1,8,6],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['poison'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','frightened','poisoned'],
 'sentidos':['blindsight 40 ft.','tremorsense 40 ft.'], 'percepcao_passiva':9, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[tr('Disconcerting Leap','Pode saltar até metade do deslocamento na horizontal e na vertical; se terminar a até 5 ft. de criatura, pode fazer Bite com vantagem.')],
 'acoes':[act('Bite','Ataque corpo a corpo +4, alcance 5 ft.; 1d4+2 piercing; prende-se ao alvo. Qualquer criatura pode removê-lo com teste de Força CD 11; preso, não ataca outras criaturas.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d4+2','tipo':'piercing'}],salvaguarda='Strength DC 11'), act('Burrow (após prender-se)','Alvo faz salvaguarda de Constituição CD 11; falha: 1d4+2 dano, sucesso: metade. Pode ser removido por ataque piercing ou slashing e sofre metade do dano causado. Se não for removido em três rodadas, causa infestação; se hospedeiro morrer durante o processo, levanta como gorger zombie após 1 minuto.',salvaguarda='Constitution DC 11')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'A criatura se fixa ao hospedeiro; o limite de três rodadas para a remoção é central para a infestação.',
 'secoes_nao_listadas':['salvaguardas','perícias','imunidades e vulnerabilidades','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/2511', 'citation':'turn10view3'
},
'TF-497': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'fey', 'alinhamento':'', 'nd_fonte':'1/8', 'ca':12, 'ca_base':'natural armor', 'pv':6, 'formula_pv':'1d8 + 2; bloodied 3',
 'deslocamento':{'walk_ft':30}, 'scores':[10,12,14,10,8,14],
 'salvaguardas':{}, 'pericias':{'Perception':1,'Performance':4}, 'pericias_bonus_dado':{'Performance':'1d4'}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':[], 'percepcao_passiva':11, 'idiomas':['Common','Sylvan'], 'bonus_proficiencia':2, 'maneuver_dc':11,
 'tracos':[tr('Magic Resistance','Vantagem em salvaguardas contra magias e outros efeitos mágicos.')],
 'acoes':[act('Hooves','Ataque corpo a corpo +3, alcance 5 ft.; 1d6+1 bludgeoning.',ataque='+3',alcance='5 ft.',dano=[{'dados':'1d6+1','tipo':'bludgeoning'}]), act('Panpipes','Escolhe uma criatura a até 30 ft. para salvaguarda de Sabedoria CD 12; sucesso ou término do efeito dá imunidade às panpipes deste faun por 24h. Clever Scherzo: falha provoca risadas, Prone e Incapacitated por 1 minuto; INT 4 ou menos é imune. Frightening Strain: falha causa Frightened por 1 minuto. Repete o teste no fim de cada turno.',salvaguarda='Wisdom DC 12')],
 'acoes_bonus':[act('Complicated Melody','Se começar o turno tocando as panpipes, escolhe criatura já afetada; ela tem desvantagem no próximo teste para encerrar o efeito.')], 'reacoes':[], 'conjuracao':None,
 'nota_tatica':'Os efeitos de Panpipes são escolhidos pelo faun; a ação bônus piora o próximo teste de encerramento.',
 'secoes_nao_listadas':['salvaguardas','defesas','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/3261', 'citation':'turn12view2'
},
'TF-376': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Small', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'1/2', 'ca':13, 'ca_base':'', 'pv':21, 'formula_pv':'6d6; bloodied 10',
 'deslocamento':{'walk_ft':30,'climb_ft':20}, 'scores':[5,17,10,7,12,7],
 'salvaguardas':{'INT':7,'CON':6}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':[], 'percepcao_passiva':11, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Keen Hearing and Smell','Vantagem em Perception que dependa de audição ou olfato.'), tr('Ethereal Sight','Os sentidos se estendem ao plano etéreo.'), tr('Guardian of the Dead','Quando morto-vivo começa o turno ou tenta aproximar-se a até 30 ft., faz salvaguarda de Sabedoria CD 11. Falha impede aproximação voluntária e dá desvantagem em ataques por 1 minuto enquanto estiver no raio; sucesso concede imunidade por 24h. Criaturas com vantagem contra Turned fazem o teste com vantagem; criatura com ações lendárias é imune.')],
 'acoes':[act('Claws','Ataque corpo a corpo +5, alcance 5 ft.; 1d4+3 slashing; contra morto-vivo causa também 2d4 radiant.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d4+3','tipo':'slashing'},{'dados':'2d4','tipo':'radiant contra undead'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'nota_tatica':'A página lista salvaguardas Int +7 e Con +6 apesar dos scores Int 7 e Con 10; valores foram preservados como impressos e exigem confirmação editorial.',
 'secoes_nao_listadas':['perícias','resistências e imunidades','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/4136', 'citation':'turn12view0'
},
'TF-481': {
 'fonte_publicacao':"Dungeon Delver's Guide", 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Small', 'tipo_fonte':'plant', 'alinhamento':'', 'nd_fonte':'1/2', 'ca':5, 'ca_base':'', 'pv':35, 'formula_pv':'10d6; bloodied 17',
 'deslocamento':{'walk_ft':0}, 'scores':[1,1,10,1,2,1],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':['bludgeoning','slashing'], 'imunidades_condicao':['blinded','charmed','deafened','fatigue','frightened','poisoned','prone','restrained','stunned'],
 'sentidos':['blindsight 30 ft. (blind beyond radius)'], 'percepcao_passiva':6, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':5,
 'tracos':[tr('False Appearance','Imóvel, indistinguível de um fungo comum.'), tr('Spell Sense','Sente criaturas capazes de conjurar ou itens mágicos com capacidade de conjuração a até 30 ft.')],
 'acoes':[act('Shriek','Se perceber criatura conjuradora ou item mágico com capacidade de conjurar a até 30 ft., grita continuamente e é ouvido a até 300 ft. Continua por 1 minuto após o alvo sair do alcance. Criaturas a até 30 ft. não podem conjurar magias com componentes vocalizados nem manter concentração.')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'A habilidade de assinatura detecta conjuração e suprime componentes vocais e concentração em raio de 30 ft.',
 'secoes_nao_listadas':['salvaguardas','perícias','resistências e imunidades','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/2853', 'citation':'turn12view3'
},
'TF-446': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'construct', 'alinhamento':'', 'nd_fonte':'1', 'ca':14, 'ca_base':'natural armor', 'pv':30, 'formula_pv':'4d8 + 12; bloodied 15',
 'deslocamento':{'walk_ft':40}, 'scores':[16,15,16,2,12,1],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['bludgeoning','piercing','slashing'], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','fatigue','frightened','paralyzed','petrified','poisoned','strife'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':11, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Gravekiller','Ataques de arma causam 1d6 radiant adicional contra mortos-vivos. Crítico de arma contra criatura exige salvaguarda de Constituição CD 13 ou Blinded por 1 minuto; repete no fim de cada turno para encerrar.'), tr('Magic Weapons','Ataques de arma são mágicos.')],
 'acoes':[act('Multiattack','Faz dois ataques.'), act('Scimitar','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 slashing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'slashing'}])],
 'acoes_bonus':[act('Wound','Ao acertar com ataque de arma que cause slashing, causa dano contínuo de 1 por cada ferimento de Grave Guardian. No fim do turno, alvo faz salvaguarda de Constituição CD 13 para encerrar. A criatura ferida ou aliado a até 5 ft. também pode usar ação e teste de Medicine CD 13 para encerrar.')],
 'reacoes':[], 'conjuracao':None, 'nota_tatica':'A página chama o traço de “Gravekiller” mas se refere ao “graven guardian” em sua descrição; mantido o conteúdo como impresso.',
 'secoes_nao_listadas':['salvaguardas','perícias','vulnerabilidades','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/3363', 'citation':'turn12view1'
},
'TF-015': {
 'fonte_publicacao':"Dungeon Delver's Guide", 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5E SRD)',
 'porte':'Large', 'tipo_fonte':'aberration', 'alinhamento':'', 'nd_fonte':'13', 'ca':18, 'ca_base':'natural armor', 'pv':210, 'formula_pv':'20d10 + 100; bloodied 105',
 'deslocamento':{'walk_ft':10,'swim_ft':40}, 'scores':[22,14,20,20,20,18],
 'salvaguardas':{'DEX':7,'CON':10,'INT':10,'WIS':10}, 'pericias':{'Deception':9,'History':10,'Intimidation':9,'Stealth':7}, 'resistencias_dano':['poison','psychic'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['blindsight 30 ft.','darkvision 120 ft.'], 'percepcao_passiva':15, 'idiomas':['Deep Speech','telepathy 120 ft.'], 'bonus_proficiencia':5, 'maneuver_dc':19,
 'tracos':[tr('Amphibious','Respira ar e água.')],
 'acoes':[act('Multiattack','Faz um ataque de Bite e dois de Tentacle.'), act('Bite','Ataque corpo a corpo +11, alcance 5 ft.; 4d12+6 piercing. O alvo fica Grappled (escape CD 19) e Restrained enquanto o agarrão durar; não pode morder outra criatura.',ataque='+11',alcance='5 ft.',dano=[{'dados':'4d12+6','tipo':'piercing'}],salvaguarda='escape DC 19'), act('Tentacle','Ataque corpo a corpo +11, alcance 15 ft.; 4d6+6 bludgeoning. Criatura atingida faz salvaguarda de Constituição CD 18 ou contrai Sea Change; sucesso concede imunidade à doença por 24h. Enquanto afetada, tem desvantagem em salvaguardas de Sabedoria. Após 1h surgem guelras e pele viscosa; sem ao menos 1h imersa a cada 12h, começa a sufocar. Magia que remove doença em espaço de 4º nível ou superior encerra; também termina 24h após a morte do aboleth.',ataque='+11',alcance='15 ft.',dano=[{'dados':'4d6+6','tipo':'bludgeoning'}],salvaguarda='Constitution DC 18; disease')],
 'acoes_bonus':[act('Ink Jet (Recharge 5–6; underwater)','Expele limo escuro em esfera de raio 30 ft.; a área fica heavily obscured por 1 minuto ou até uma corrente forte dissipar a nuvem. Depois move-se até seu deslocamento sem provocar ataques de oportunidade.',uso='Recharge 5–6; underwater')], 'reacoes':[], 'conjuracao':None,
 'nota_tatica':'Ataca o inimigo mais forte com Bite e Grapple; usa tentáculos nos demais. Quando bloodied, pode usar Ink Jet para escapar.',
 'secoes_nao_listadas':['vulnerabilidades de dano','imunidades a dano e condições','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/2819', 'citation':'turn18view0'
},
'TF-016': {
 'fonte_publicacao':"Dungeon Delver's Guide", 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5E SRD)',
 'porte':'Large', 'tipo_fonte':'aberration', 'alinhamento':'', 'nd_fonte':'13', 'ca':18, 'ca_base':'natural armor', 'pv':210, 'formula_pv':'20d10 + 100; bloodied 105',
 'deslocamento':{'walk_ft':10,'swim_ft':40}, 'scores':[22,14,20,20,20,18],
 'salvaguardas':{'DEX':7,'CON':10,'INT':10,'WIS':10}, 'pericias':{'Deception':9,'History':10,'Intimidation':9,'Stealth':7}, 'resistencias_dano':['poison','psychic'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['blindsight 30 ft.','darkvision 120 ft.'], 'percepcao_passiva':15, 'idiomas':['Deep Speech','telepathy 120 ft.'], 'bonus_proficiencia':5, 'maneuver_dc':19,
 'tracos':[tr('Amphibious','Respira ar e água.')],
 'acoes':[act('Multiattack','Faz um ataque de Bite e dois de Tentacle.'), act('Bite','Ataque corpo a corpo +11, alcance 5 ft.; 4d12+6 piercing. O alvo fica Grappled (escape CD 19) e Restrained enquanto o agarrão durar; não pode morder outra criatura.',ataque='+11',alcance='5 ft.',dano=[{'dados':'4d12+6','tipo':'piercing'}],salvaguarda='escape DC 19'), act('Tentacle','Ataque corpo a corpo +11, alcance 15 ft.; 4d6+6 bludgeoning. Criatura atingida faz salvaguarda de Constituição CD 18 ou contrai Sea Change; sucesso concede imunidade à doença por 24h. Enquanto afetada, tem desvantagem em salvaguardas de Sabedoria. Após 1h surgem guelras e pele viscosa; sem ao menos 1h imersa a cada 12h, começa a sufocar. Magia que remove doença em espaço de 4º nível ou superior encerra; também termina 24h após a morte do aboleth.',ataque='+11',alcance='15 ft.',dano=[{'dados':'4d6+6','tipo':'bludgeoning'}],salvaguarda='Constitution DC 18; disease')],
 'acoes_bonus':[act('Ink Jet (Recharge 5–6; underwater)','Expele limo escuro em esfera de raio 30 ft.; a área fica heavily obscured por 1 minuto ou até uma corrente forte dissipar a nuvem. Depois move-se até seu deslocamento sem provocar ataques de oportunidade.',uso='Recharge 5–6; underwater'), act('Eyebite (6th level; concentration)','Uma criatura que o aboleth vê e que também o vê, a até 60 ft., faz salvaguarda de Sabedoria CD 18 ou sofre um efeito por até 1 minuto. A cada turno, como ação bônus, pode escolher um alvo que ainda não tenha obtido sucesso contra esta conjuração: Asleep deixa o alvo Unconscious até sofrer dano ou alguém gastar ação para acordá-lo; Panicked dá Frightened e força Dash para longe pela rota segura mais curta, terminando ao ficar a 60 ft. sem ver o aboleth; Sickened impõe desvantagem em ataques e testes de atributo, com novo teste ao final de cada turno.',uso='6th level; concentration; bonus action to retarget',salvaguarda='Wisdom DC 18')], 'reacoes':[],
 'conjuracao':{'atributo':'WIS','cd':18,'ataque_magia':'+10','sem_componentes':['todos'],'tempo_conjuracao':'ações bônus','3/day':['detect thoughts (120 ft.)','eyebite','phantasmal force','project image (1 mile)']},
 'nota_tatica':'A ficha preserva os mesmos valores de combate do Aboleth Brute, mas acrescenta conjuração inata e Eyebite; a página não explica a semelhança estatística.',
 'secoes_nao_listadas':['vulnerabilidades de dano','imunidades a dano e condições','reações','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/2820', 'citation':'turn18view1'
},
'TF-017': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5E SRD)',
 'porte':'Huge', 'tipo_fonte':'aberration', 'alinhamento':'', 'nd_fonte':'11', 'ca':17, 'ca_base':'natural armor', 'pv':342, 'formula_pv':'36d10 + 144; bloodied 171',
 'deslocamento':{'walk_ft':10,'swim_ft':40}, 'scores':[20,12,18,20,20,18], 'tags':['Elite','Legendary'],
 'salvaguardas':{'DEX':5,'CON':8,'INT':9,'WIS':9}, 'pericias':{'Deception':8,'History':9,'Stealth':5}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['blindsight 30 ft.','darkvision 120 ft.'], 'percepcao_passiva':15, 'idiomas':['Deep Speech','telepathy 120 ft.'], 'bonus_proficiencia':4, 'maneuver_dc':17,
 'tracos':[tr('Amphibious','Respira ar e água.'), tr('Legendary Resistance (3/day)','Quando falha em salvaguarda, pode escolher ter sucesso. Cada uso escurece um dos três olhos; com todos negros, fica cego além do alcance de blindsight até completar descanso longo.')],
 'acoes':[act('Multiattack','Faz três ataques de Tentacle.'), act('Tentacle','Ataque corpo a corpo +9, alcance 15 ft.; 4d6+5 bludgeoning, ou pode escolher causar 0 dano. Criatura atingida faz salvaguarda de Constituição CD 16 ou contrai Sea Change; sucesso concede imunidade à doença por 24h. A doença impõe desvantagem em salvaguardas de Sabedoria; após 1h surgem guelras e pele viscosa, e sem pelo menos 1h submersa a cada 12h a criatura começa a sufocar. Magia de remoção de doença com espaço de 4º nível ou superior cura; termina 24h após a morte do aboleth.',ataque='+9',alcance='15 ft.',dano=[{'dados':'4d6+5','tipo':'bludgeoning; pode causar 0'}],salvaguarda='Constitution DC 16; disease'), act('Slimy Cloud (1/day; while bloodied; underwater)','Esfera de raio 30 ft. Cada criatura exceto aboleths na área faz salvaguarda de Constituição CD 16; falha causa 8d10 poison e condição Poisoned por 1 minuto. A área fica heavily obscured por 1 minuto ou até corrente forte dissipar a nuvem.',uso='1/day; while bloodied; underwater',salvaguarda='Constitution DC 16')],
 'acoes_lendarias':[act('Move','Move até o deslocamento de natação sem provocar ataques de oportunidade.'), act('Telepathic Summon','Uma criatura a até 90 ft. faz salvaguarda de Sabedoria CD 16; falha obriga-a a usar sua reação, se disponível, para mover-se até o deslocamento em direção ao aboleth pela rota mais direta sem evitar ataques de oportunidade. É efeito mágico de encanto.',salvaguarda='Wisdom DC 16'), act('Baleful Charm (custa 2 ações)','Alvo a até 60 ft. que contraiu Sea Change faz salvaguarda de Sabedoria CD 16; falha fica Charmed até o aboleth morrer. Repete o teste a cada 24h e ao sofrer dano do aboleth ou aliados. Encantado, comunica-se telepaticamente a qualquer distância e obedece ordens.',uso='2 legendary actions',salvaguarda='Wisdom DC 16'), act('Soul Drain (custa 2 ações)','Uma criatura Charmed sofre 4d10 psychic; o aboleth recupera PV iguais ao dano.',uso='2 legendary actions')],
 'economia_lendaria':'2 ações lendárias por rodada; só uma opção por vez e ao fim do turno de outra criatura; recupera no início do próprio turno.',
 'acoes_especiais':[act('Elite Recovery (while bloodied)','Encerra um efeito negativo que o afete; pode usar mesmo inconsciente ou incapacitado se tiver ao menos 1 PV.'), act('Look Upon My Works (while bloodied; 1/day)','Cada criatura a até 90 ft. faz salvaguarda de Sabedoria CD 16; falha sofre 6d10 psychic ao ver fragmento de memórias do aboleth. Depois do dano, esquece a visão, mas pode aprender uma informação de lore.',uso='1/day; while bloodied',salvaguarda='Wisdom DC 16'), act('Lunging Attack (while bloodied)','Move até o deslocamento de natação sem provocar ataques de oportunidade e faz um ataque de Tentacle.')],
 'conjuracao':{'atributo':'CHA','cd':16,'ataque_magia':None,'sem_componentes':['todos'],'3/day':['detect thoughts (120 ft.)','project image (1 mile)','major image']},
 'nota_tatica':'Usa Tentacle para espalhar Sea Change e depois Baleful Charm nos alvos mais perigosos; bloodied, pode criar Slimy Cloud e escapar.',
 'secoes_nao_listadas':['vulnerabilidades de dano','imunidades a dano e condições','ações bônus','reações','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1459', 'citation':'turn19view1'
},
'TF-055': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5E SRD)',
 'porte':'Gargantuan', 'tipo_fonte':'celestial', 'alinhamento':'', 'nd_fonte':'22', 'ca':21, 'ca_base':'breastplate', 'pv':656, 'formula_pv':'32d20 + 320; bloodied 328',
 'deslocamento':{'walk_ft':60,'fly_ft':60}, 'scores':[30,24,30,22,24,26], 'tags':['Elite','Legendary'],
 'salvaguardas':{'STR':17,'CON':17,'INT':13,'WIS':14,'CHA':15}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['radiant','damage from nonmagical weapons'], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['truesight 120 ft.'], 'percepcao_passiva':17, 'idiomas':['Celestial','Common','six more (not enumerated)'], 'bonus_proficiencia':7, 'maneuver_dc':25,
 'tracos':[tr('Divine Grace','Se fizer salvaguarda contra efeito que causa metade do dano no sucesso, não sofre dano no sucesso e sofre metade na falha. Com armadura média, soma o modificador total de Destreza à CA; bônus já incluído.'), tr('Magic Resistance','Vantagem em salvaguardas contra magias e outros efeitos mágicos.'), tr('Regeneration','Recupera 10 PV no início do turno enquanto tiver ao menos 1 PV.'), tr('Immortal Nature','Não precisa respirar, alimentar-se ou dormir.'), tr('Blind Rage (while bloodied)','Enquanto bloodied, pode usar 3 ações lendárias em vez de 1. Se bloodied e com outras criaturas na linha de visão, deve usar cada ação e ação lendária para atacar com arma uma criatura visível ao alcance ou voar em direção à criatura visível mais próxima.'), tr('Elite Recovery','No fim do turno, encerra um efeito negativo que a afete; pode usar enquanto tiver ao menos 1 PV, mesmo inconsciente ou incapacitada.')],
 'acoes':[act('Maul','Ataque corpo a corpo +17, alcance 10 ft.; 8d6+10 bludgeoning e 4d6 radiant. Alvo faz salvaguarda de Força CD 25; falha é empurrado até 30 ft. e cai Prone.',ataque='+17',alcance='10 ft.',dano=[{'dados':'8d6+10','tipo':'bludgeoning'},{'dados':'4d6','tipo':'radiant'}],salvaguarda='Strength DC 25'), act('Lightning Bolt (3rd-level; V, S)','Linha de 100 ft. por 5 ft.; salvaguarda de Destreza CD 23, 8d6 lightning em falha ou metade no sucesso.',salvaguarda='Dexterity DC 23'), act('Flame Strike (5th-level; V, S)','Cilindro de raio 10 ft. e altura 40 ft. em ponto a até 60 ft.; salvaguarda de Destreza CD 23, 4d6 fire + 4d6 radiant em falha ou metade no sucesso.',salvaguarda='Dexterity DC 23'), act('Hold Monster (5th-level; V, S, concentration)','Uma criatura visível a até 60 ft. faz salvaguarda de Sabedoria CD 23; falha causa Paralyzed por até 1 minuto. Repete o teste ao fim de cada turno, encerrando no sucesso.',salvaguarda='Wisdom DC 23; concentration')],
 'acoes_bonus':[act('Immortal Form','Muda magicamente de tamanho entre Gargantuan e Medium. Enquanto Medium, tem desvantagem em testes de Força; demais estatísticas não mudam.')],
 'acoes_lendarias':[act('Attack','Faz um ataque com arma.'), act('Cast Spell','Conjura uma magia; não pode escolher se conjurou uma magia desde o início do turno anterior.'), act('Fly','Voa até metade do deslocamento de voo.'), act('Shout (Recharge 5–6)','Cada criatura a até 120 ft. que ouve faz salvaguarda de Constituição CD 25; falha causa 7d6 thunder e Stunned até o fim do próximo turno de Aklea, sucesso causa metade do dano.',uso='Recharge 5–6',salvaguarda='Constitution DC 25')],
 'economia_lendaria':'1 ação lendária por rodada; enquanto bloodied, Blind Rage permite até 3 ações lendárias.',
 'reacoes':[],
 'conjuracao':{'atributo':'CHA','cd':23,'ataque_magia':None,'sem_componentes':['material'],'at_will':['charm person','command','telekinesis'],'3/day':['flame strike','hold monster','lightning bolt'],'1/day':['commune','greater restoration','heroes’ feast','plane shift (self only; não pode entrar/sair do Plano Material)']},
 'nota_tatica':'A página nomeia a criatura Aklea e em algumas linhas a chama de empyrean; seis idiomas adicionais são mencionados sem enumeração. Enquanto bloodied, a fúria restringe as ações e eleva a economia lendária.',
 'secoes_nao_listadas':['perícias','vulnerabilidades de dano','imunidades a condições','reações','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1801', 'citation':'turn19view0'
},
'TF-093': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5E SRD)',
 'porte':'Huge', 'tipo_fonte':'dragon', 'alinhamento':'', 'nd_fonte':'17', 'ca':18, 'ca_base':'natural armor', 'pv':241, 'formula_pv':'23d12 + 92; bloodied 120',
 'deslocamento':{'walk_ft':40,'burrow_ft':30,'fly_ft':60}, 'scores':[22,22,18,22,12,18], 'tags':['Legendary'], 'terreno':['Caverns','Ruin','Sewer'],
 'salvaguardas':{'CON':10,'INT':12,'WIS':7,'CHA':10}, 'pericias':{'Deception':10,'History':12,'Perception':7,'Stealth':12}, 'resistencias_dano':['psychic','thunder'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue'],
 'sentidos':['darkvision 120 ft.'], 'percepcao_passiva':17, 'idiomas':['Common','Deep Speech','Draconic','Undercommon','telepathy 120 ft.'], 'bonus_proficiencia':6, 'maneuver_dc':20,
 'tracos':[tr('Legendary Resistance (3/Day)','Quando falha em salvaguarda, pode escolher obter sucesso; até o fim do próximo turno, seus ataques corpo a corpo têm vantagem contra a criatura que provocou o uso e desvantagem contra todas as outras.'), tr('Psionic Powers','Suas habilidades psônicas contam como mágicas e psônicas.'), tr('Far Thoughts','Percebe criaturas a até 100 milhas que usam habilidade psônica ou telepatia. Como ação, observa psionicamente criatura, objeto ou lugar familiar nessa distância, podendo ver, ouvir e comunicar-se telepaticamente; enquanto observa, fica cega e surda aos próprios sentidos físicos. Pode manter o efeito indefinidamente e encerrá-lo como ação; não necessita de alimento ou água enquanto observa.'), tr('Innate Spellcasting','Conjuração por Carisma, CD 18, sem componentes materiais; cada magia listada pode ser lançada 3 vezes por dia.')],
 'acoes':[act('Multiattack','Faz uma mordida e dois ataques de garras; pode substituir a mordida por Psionic Wave.'), act('Bite','Ataque corpo a corpo +12, alcance 10 ft.; 3d10+6 piercing e 1d8 thunder.',ataque='+12',alcance='10 ft.',dano=[{'dados':'3d10+6','tipo':'piercing'},{'dados':'1d8','tipo':'thunder'}]), act('Claws','Ataque corpo a corpo +12, alcance 5 ft.; 3d8+6 slashing.',ataque='+12',alcance='5 ft.',dano=[{'dados':'3d8+6','tipo':'slashing'}]), act('Psionic Wave','Onda psíquica atinge criaturas a até 20 ft.; salvaguarda de Sabedoria CD 18, 3d10 psychic em falha ou metade em sucesso. Criaturas Confused fazem o teste com desvantagem.',salvaguarda='Wisdom DC 18'), act('Maddening Breath (Recharge 5–6)','Cone de 60 ft.; salvaguarda de Constituição CD 18, 13d10 thunder em falha ou metade em sucesso. Quem falhar por 10 ou mais fica psionicamente Confused até o fim do próximo turno.',uso='Recharge 5–6',salvaguarda='Constitution DC 18')],
 'acoes_bonus':[], 'reacoes':[act('Spiteful Retort (while bloodied)','Quando uma criatura visível causa dano ao dragão, ela faz salvaguarda de Sabedoria CD 15; falha causa 4d8 thunder, sucesso metade. Criaturas Confused fazem o teste com desvantagem.',salvaguarda='Wisdom DC 15')],
 'acoes_lendarias':[act('Paranoid Ranting','Uma criatura que possa ouvir a até 60 ft. faz salvaguarda de Sabedoria CD 15; em falha recebe um efeito aleatório de estresse mental de curto prazo ou loucura.',salvaguarda='Wisdom DC 15'), act('Pandorum (custa 2 ações)','Uma criatura a até 60 ft. faz salvaguarda de Sabedoria CD 15; em falha fica Confused e passa a considerar aliados como inimigos traidores. Ao determinar ações aleatórias, resultados 1–4 contam como 8. Repete a salvaguarda ao fim de cada turno, encerrando o efeito no sucesso.',uso='2 legendary actions',salvaguarda='Wisdom DC 15'), act('Psionic Wave (custa 2 ações)','Usa Psionic Wave.',uso='2 legendary actions'), act('Maddening Harmonics (1/Day)','Criaturas escolhidas que possam ouvir a até 90 ft. fazem salvaguarda de Sabedoria CD 15; em falha ficam psionicamente Confused por 1 minuto e repetem a salvaguarda ao fim de cada turno, encerrando o efeito no sucesso.',uso='1/day',salvaguarda='Wisdom DC 15')],
 'economia_lendaria':'3 ações lendárias; usa uma opção por vez apenas ao fim do turno de outra criatura e recupera os usos no início do próprio turno.',
 'caracteristicas_de_covil':[tr('Servos manipulados','Uma vez por dia, quando usaria Pandorum, pode invocar três berserkers no lugar; lutam até morrer ou até serem dispensados como ação bônus.'), tr('Ressonância de paranoia','A primeira criatura além do dragão que entrar no covil por dia faz salvaguarda contra a CD do covil (13 + bônus de proficiência); em falha recebe 1 Strife.'), tr('Passagens imprevisíveis','Se terminar o turno fora da vista de outras criaturas, pode Esconder-se como ação bônus.'), tr('Armadilhas do covil','O covil contém 1d4 portas, baús ou alavancas armadilhados; interagir aciona lâminas ou foices com efeito equivalente ao ataque de garras.')],
 'conjuracao':{'atributo':'CHA','cd':18,'ataque_magia':None,'sem_componentes':['material'],'3/day':['confusion','dominate person','hideous laughter','suggestion']},
 'nota_tatica':'A fonte marca esta criatura como Legendary. Os efeitos de covil são apresentados como características ambientais, não como ações de covil.',
 'secoes_nao_listadas':['alinhamento','vulnerabilidades de dano','imunidades a dano','imunidades a condições além de fatigue','ações bônus','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1567', 'citation':'turn25view0'
},
'TF-094': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5E SRD)',
 'porte':'Huge', 'tipo_fonte':'dragon', 'alinhamento':'', 'nd_fonte':'17', 'ca':18, 'ca_base':'natural armor', 'pv':252, 'formula_pv':'24d12 + 96; bloodied 126',
 'deslocamento':{'walk_ft':60,'fly_ft':80,'swim_ft':90}, 'scores':[18,20,18,14,20,16], 'tags':['Legendary'], 'terreno':['Grassland','Water'],
 'salvaguardas':{'DEX':9,'CON':8,'INT':6,'WIS':9,'CHA':7}, 'pericias':{'Acrobatics':8,'Deception':7,'Insight':9,'Nature':6,'Perception':9,'Stealth':9}, 'resistencias_dano':['damage from nonmagical weapons'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue'],
 'sentidos':['darkvision 120 ft.','tremorsense 200 ft. (detecta apenas vibrações na água)'], 'percepcao_passiva':19, 'idiomas':['Aquan','Common','Draconic'], 'bonus_proficiencia':6, 'maneuver_dc':19,
 'tracos':[tr('Amphibious','Respira ar e água.'), tr('Flowing Grace','Ao voar ou nadar para fora do alcance de um inimigo, não provoca ataques de oportunidade.'), tr('Legendary Resistance (3/Day)','Quando falha em salvaguarda, pode obter sucesso; ao fazer isso, perde Flowing Grace e Shimmering Scales até o início do próximo turno.'), tr('Shimmering Scales','Enquanto está na água, recebe três quartos de cobertura contra ataques de criaturas a mais de 30 ft.'), tr('Essence Link','Vínculo espiritual a uma área ou marco específico; não obtém benefício de descanso longo a mais de 1 milha da área. Se morrer, a área perde sua essência vital até que surja outro dragão de essência, o que pode levar séculos. Criaturas que entram nessa área pela primeira vez recebem 1 nível de Fatigue e 1 de Strife; esses níveis só são removidos após descanso longo fora da área.'), tr('Innate Spellcasting','Conjuração por Carisma, CD 15, sem componentes materiais; cada magia listada pode ser lançada 3 vezes por dia.')],
 'acoes':[act('Multiattack','Faz uma mordida e dois ataques de garras.'), act('Bite','Ataque corpo a corpo +11, alcance 10 ft.; 3d10+5 piercing.',ataque='+11',alcance='10 ft.',dano=[{'dados':'3d10+5','tipo':'piercing'}]), act('Claws','Ataque corpo a corpo +11, alcance 5 ft.; 3d8+5 slashing.',ataque='+11',alcance='5 ft.',dano=[{'dados':'3d8+5','tipo':'slashing'}]), act('Torrential Breath (Recharge 5–6)','Linha de água de 60 ft. de comprimento e 5 ft. de largura; salvaguarda de Destreza CD 18, 16d6 bludgeoning em falha ou metade em sucesso. Falha também deixa a criatura Prone e a empurra até 30 ft.; se atingir objeto sólido, sofre 3d6 bludgeoning adicionais.',uso='Recharge 5–6',salvaguarda='Dexterity DC 18')],
 'acoes_bonus':[act('Whirlpool','Cria redemoinho ou tromba-d’água cilíndrica de 15 ft. de altura e raio 10 ft. em água ou ar, centrada em ponto a até 60 ft. Criaturas na área fazem salvaguarda de Força CD 18. A fonte declara que, em falha, a criatura sofre 5d6 bludgeoning, fica Prone e é empurrada até 15 ft.; a frase seguinte também atribui dano pela metade a “falha”, sem definir o resultado de sucesso.',salvaguarda='Strength DC 18')],
 'reacoes':[act('Snap Back (while bloodied)','Quando uma criatura que o dragão vê acerta-o com ataque de arma corpo a corpo, o dragão faz uma mordida contra ela.')],
 'acoes_lendarias':[act('Dart Away','Nada até metade do deslocamento.'), act('Lurk','Usa a ação Esconder-se.'), act('River Surge (custa 2 ações)','Gera onda de 20 ft. de altura e 100 ft. de largura na superfície da água a até 90 ft.; desloca-a até 45 ft. em direção escolhida e carrega criaturas e veículos Huge ou menores. Veículos têm 25% de chance de virar; criatura que colide com objeto sólido sofre 6d6 bludgeoning.',uso='2 legendary actions'), act('Sudden Maelstrom (bloodied; 1/Day)','Por 1 minuto, envolve-se em maelstrom de vento e chuva com raio de 60 ft. Criatura além do dragão que inicie o turno na área ou entre nela pela primeira vez no turno faz salvaguarda de Força CD 18; em falha fica Prone e é empurrada 15 ft.',uso='while bloodied; 1/day',salvaguarda='Strength DC 18')],
 'economia_lendaria':'3 ações lendárias; usa uma opção por vez apenas ao fim do turno de outra criatura e recupera os usos no início do próprio turno.',
 'caracteristicas_de_covil':[tr('Fauna aliada','Como ação bônus, invoca 1d6 crocodilos ou 1d4 enxames de quippers; lutam até morrer, serem dispensados por ação bônus ou a habilidade ser usada novamente.'), tr('Defensores locais','No início de cada rodada, role 1d6; com 5–6 chegam 1d4 locais com estatísticas de thug, agindo na iniciativa do dragão até morrer ou receber ordem para parar.'), tr('Margens rochosas','Quando ataque ou habilidade do dragão faz criatura colidir com objeto sólido, a criatura sofre 2d8 bludgeoning adicional.'), tr('Água turva','A visibilidade submersa no rio é reduzida a 20 ft.')],
 'conjuracao':{'atributo':'CHA','cd':15,'ataque_magia':None,'sem_componentes':['material'],'3/day':['create or destroy water','fog cloud','control water','freedom of movement']},
 'nota_fonte':'A ação bônus Whirlpool contém duas frases consecutivas sobre falha no teste: uma determina dano integral e efeitos; a seguinte diz dano pela metade também em falha. O resultado do sucesso não é informado e não foi inferido. Mecânica registrada parcialmente até confirmação editorial.',
 'secoes_nao_listadas':['alinhamento','imunidades a dano','vulnerabilidades de dano','ações míticas','ações de covil (a fonte fornece características de covil, não uma seção de ações)'], 'completa':False,
 'url':'https://a5e.tools/node/1555', 'citation':'turn25view1'
},
'TF-088': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'dragon', 'alinhamento':'', 'variante':'Amethyst Dragon Wyrmling', 'nd_fonte':'2', 'ca':16, 'ca_base':'natural armor', 'pv':45, 'formula_pv':'7d8 + 14; bloodied 22',
 'deslocamento':{'walk_ft':30,'burrow_ft':15,'fly_ft':50}, 'scores':[14,14,14,16,10,14],
 'salvaguardas':{}, 'pericias':{'Deception':4,'Insight':2,'Perception':2,'Persuasion':4}, 'resistencias_dano':['force','psychic'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue'],
 'sentidos':['darkvision 120 ft.'], 'percepcao_passiva':12, 'idiomas':['Deep Speech','Draconic','Undercommon','telepathy 120 ft.'], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[tr('Far Thoughts','Percebe criaturas a até 100 milhas que usem habilidade psiônica ou comuniquem-se por telepatia. Como ação, observa psiquicamente por tempo indefinido criatura, objeto ou local familiar nessa distância; durante isso vê, ouve e comunica-se por telepatia, mas fica cega e surda aos sentidos físicos e não precisa de comida ou água. Encerra o efeito e retorna aos sentidos próprios como ação.')],
 'acoes':[act('Bite','Ataque corpo a corpo +4, alcance 5 ft.; 13 (2d10+2) piercing.',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d10+2','tipo':'piercing'}]), act('Concussive Breath (Recharge 5–6)','Cone de 15 ft.; criaturas na área fazem salvaguarda de Constituição CD 12, sofrendo 16 (3d10) force em falha ou metade em sucesso.',uso='Recharge 5–6',salvaguarda='Constitution DC 12',alcance='15-ft. cone',dano=[{'dados':'3d10','tipo':'force'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'caracteristicas_de_covil':[tr('Servants','CD das características de covil: 13 + bônus de proficiência do dragão (15). Uma vez por dia, quando usaria Charm, pode invocar três cult fanatics; lutam até serem mortos ou dispensados pelo dragão com ação bônus.'),tr('Psionic Illusions','Ilusões psiônicas ocultam passagens. Percebê-las exige teste de Perception contra a CD do covil; interação física também revela a ilusão.'),tr('Resonant Lair','O alcance das habilidades psiônicas do dragão é dobrado.'),tr('Words of the Lair','Testes de Insight para perceber as verdadeiras intenções do dragão são feitos com desvantagem.')],
 'tags':[], 'terreno':['Caverns'],
 'secoes_nao_listadas':['alinhamento','salvaguardas','imunidades e vulnerabilidades de dano','resistências ou vulnerabilidades a condições','ações bônus','reações','conjuração','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1565', 'citation':'turn41view0'
},
'TF-092': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Huge', 'tipo_fonte':'dragon', 'alinhamento':'', 'variante':'Adult Earth Dragon', 'nd_fonte':'18', 'ca':19, 'ca_base':'natural armor', 'pv':287, 'formula_pv':'23d12 + 138; bloodied 143',
 'deslocamento':{'walk_ft':40,'fly_ft':40,'burrow_ft':60}, 'scores':[22,14,22,14,20,12],
 'salvaguardas':{'STR':12,'CON':12,'INT':8,'WIS':8,'CHA':7}, 'pericias':{'Athletics':12,'Insight':8,'Nature':12,'Perception':8}, 'pericias_bonus_dado':{'Insight':'1d6','Perception':'1d6'},
 'resistencias_dano':['damage from nonmagical weapons'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['petrified'],
 'sentidos':['darkvision 120 ft.','tremorsense 90 ft.'], 'percepcao_passiva':21, 'idiomas':['Common','Draconic','Terran'], 'bonus_proficiencia':6, 'maneuver_dc':20, 'tags':['Legendary'], 'terreno':['Desert','Hills','Mountains'],
 'tracos':[tr('Earth Glide','Escava terra e pedra natural não trabalhada sem perturbá-las.'),tr('False Appearance','Imóvel dentro da área vinculada, é indistinguível de um afloramento rochoso natural.'),tr('Legendary Resistance (3/Day)','Quando falha em salvaguarda, pode escolher obter sucesso; ao fazê-lo, seu deslocamento é reduzido à metade até o fim do próximo turno.'),tr('Essence Link','Ligado espiritualmente a uma área ou marco específico; não recebe benefício de descanso longo a mais de 1 milha dela. Se morrer, a área perde a essência vital até formar outro dragão de essência, processo que pode levar séculos. Quem entra pela primeira vez na área sem essência recebe 1 nível de Fatigue e 1 de Strife; ambos só podem ser removidos com descanso longo fora dela.'),tr('Innate Spellcasting','Conjuração por Carisma, CD 15, sem componentes materiais.')],
 'acoes':[act('Multiattack','Faz uma mordida e dois ataques de Slam. Em vez da mordida, pode usar Rock Spire.'),act('Bite','Ataque corpo a corpo +12, alcance 10 ft.; 28 (4d10+6) piercing. Em vez do dano, pode agarrar (escape CD 20); criatura Large ou menor agarrada fica Restrained. Enquanto mantém a criatura agarrada, não pode morder outro alvo.',ataque='+12',alcance='10 ft.',dano=[{'dados':'4d10+6','tipo':'piercing'}],salvaguarda='escape DC 20'),act('Slam','Ataque corpo a corpo +12, alcance 5 ft.; 19 (3d8+6) bludgeoning.',ataque='+12',alcance='5 ft.',dano=[{'dados':'3d8+6','tipo':'bludgeoning'}]),act('Scouring Breath (Recharge 5–6)','Cone de 60 ft.; salvaguarda de Destreza CD 20, 56 (16d6) slashing em falha ou metade em sucesso. Falha também deixa a criatura Blinded até o fim do próximo turno.',uso='Recharge 5–6',salvaguarda='Dexterity DC 20',alcance='60-ft. cone',dano=[{'dados':'16d6','tipo':'slashing'}]),act('Rock Spire','Ergue permanentemente uma coluna rochosa de 25 ft. de altura e raio de 5 ft. a partir de ponto no chão a até 60 ft. Criatura na área quando surge faz salvaguarda de Destreza CD 19, sofrendo 13 (3d8) piercing em falha ou metade em sucesso. Falha por 10 ou mais empala a criatura no topo. Uma ação e teste de Força CD 12 libertam-na; destruir a coluna também a liberta. A coluna é objeto com CA 16, 30 PV e imunidade a poison e psychic.',salvaguarda='Dexterity DC 19; escape Strength DC 12',alcance='60 ft.',dano=[{'dados':'3d8','tipo':'piercing'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':{'atributo':'CHA','cd':15,'ataque_magia':None,'sem_componentes':['material'],'3/day each':['locate animals or plants','spike growth','stone shape','wall of stone']},
 'economia_lendaria':'3 ações lendárias; usa uma opção por vez ao fim do turno de outra criatura e recupera todas no início do próprio turno.',
 'acoes_lendarias':[act('Shake the Foundation','Torna permanentemente terreno difícil uma área de raio 40 ft. centrada em ponto que vê. Se estiver Bloodied, criaturas na área fazem salvaguarda de Destreza CD 20; falha deixa Prone.'),act('Slam Attack (custa 2 ações)','Faz um ataque Slam.',uso='2 legendary actions'),act('Entomb (Bloodied; custa 3 ações)','Alvo no chão a até 60 ft. faz salvaguarda de Destreza CD 15; em falha é enterrado magicamente 5 ft. sob a terra, Blinded, Restrained e sem poder respirar. Uma ação e teste de Força CD 15 libertam a criatura.',uso='while bloodied; 3 legendary actions',salvaguarda='Dexterity DC 15; escape Strength DC 15')],
 'caracteristicas_de_covil':[tr('Desolate Peak','A jornada até o covil na montanha aciona o dobro dos desafios de exploração usuais.'),tr('Jagged Stone','Quando o dragão acerta com Slam uma criatura a até 5 ft. de uma parede do covil, ela sofre 5 (1d10) piercing adicionais.'),tr('Volcanic Lair','Ao morder criatura agarrada, pode mergulhá-la em magma em vez de causar o dano piercing; sofre dano fire igual ao dano piercing que a mordida causaria.'),tr('Loose Sand','Seu deslocamento de escavação aumenta para 100 ft.; pode usar Scouring Breath revelando apenas o focinho e mantendo cobertura de três quartos.')],
 'secoes_nao_listadas':['alinhamento','salvaguarda de Destreza','imunidades e vulnerabilidades de dano','resistências ou vulnerabilidades a condições','ações bônus','reações','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1551', 'citation':'turn41view1'
},
'TF-095': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Huge', 'tipo_fonte':'dragon', 'alinhamento':'', 'variante':'Adult Sapphire Dragon', 'nd_fonte':'19', 'ca':19, 'ca_base':'natural armor', 'pv':304, 'formula_pv':'29d12 + 116; bloodied 152',
 'deslocamento':{'walk_ft':40,'burrow_ft':30,'fly_ft':80}, 'scores':[22,22,18,22,20,16],
 'salvaguardas':{'CON':10,'INT':12,'WIS':11,'CHA':10}, 'pericias':{'Arcana':12,'Deception':10,'History':12,'Insight':11,'Perception':11,'Persuasion':10}, 'pericias_bonus_dado':{'Insight':'1d6','Perception':'1d6'},
 'resistencias_dano':[], 'imunidades_dano':['psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue'],
 'sentidos':['darkvision 120 ft.'], 'percepcao_passiva':24, 'idiomas':['Common','Deep Speech','Draconic','Undercommon','telepathy 120 ft.'], 'bonus_proficiencia':6, 'maneuver_dc':20, 'tags':['Legendary'], 'terreno':['Caverns'],
 'tracos':[tr('Legendary Resistance (3/Day)','Quando falha em salvaguarda, pode escolher obter sucesso. O texto então limita Foretell, Prognosticate e Prophesy Doom até o fim do próximo turno e remove Predictive Harmonics; Prophesy Doom não aparece entre as ações listadas na página.'),tr('Predictive Harmonics','Não pode ser Surprised; qualquer rolagem que sofreria Disadvantage é feita normalmente.'),tr('Psionic Powers','As habilidades psiônicas do dragão são consideradas mágicas e psiônicas.'),tr('Far Thoughts','Percebe criaturas a até 100 milhas que usem habilidade psiônica ou comuniquem-se por telepatia. Como ação, observa psiquicamente por tempo indefinido criatura, objeto ou local familiar nessa distância; durante isso vê, ouve e comunica-se por telepatia, mas fica cega e surda aos sentidos físicos e não precisa de comida ou água. Encerra o efeito e retorna aos sentidos próprios como ação.'),tr('Innate Spellcasting','Conjuração por Carisma, CD 18, sem componentes materiais.')],
 'acoes':[act('Multiattack','Faz uma mordida e dois ataques de Claws. Em vez da mordida, pode usar Psionic Wave.'),act('Bite','Ataque corpo a corpo +12, alcance 10 ft.; 22 (3d10+6) piercing e 4 (1d8) psychic.',ataque='+12',alcance='10 ft.',dano=[{'dados':'3d10+6','tipo':'piercing'},{'dados':'1d8','tipo':'psychic'}]),act('Claws','Ataque corpo a corpo +12, alcance 5 ft.; 19 (3d8+6) slashing.',ataque='+12',alcance='5 ft.',dano=[{'dados':'3d8+6','tipo':'slashing'}]),act('Psionic Wave','Criaturas a até 20 ft. fazem salvaguarda de Sabedoria CD 18, sofrendo 16 (3d10) psychic em falha ou metade em sucesso. Criaturas que sofram psychic ongoing damage fazem essa salvaguarda com desvantagem.',salvaguarda='Wisdom DC 18',alcance='20 ft.',dano=[{'dados':'3d10','tipo':'psychic'}]),act('Discognitive Breath (Recharge 5–6)','Cone de 60 ft.; salvaguarda de Inteligência CD 18. Em falha: 60 (11d10) psychic e 11 (2d10) psychic ongoing damage; em sucesso, metade do dano psychic e nenhum ongoing damage. O dano contínuo termina se a criatura ficar Unconscious ou usar uma ação para se ancorar à realidade.',uso='Recharge 5–6',salvaguarda='Intelligence DC 18',alcance='60-ft. cone',dano=[{'dados':'11d10','tipo':'psychic'},{'dados':'2d10 ongoing','tipo':'psychic'}]),act('Prognosticate (3/Day)','Faz previsão psiônica de evento até 100 anos no futuro, com 67% de chance de ser perfeitamente correta e 33% de ser parcialmente ou totalmente errada; alternativamente ganha Truesight 90 ft. por 1 minuto.',uso='3/day')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':{'atributo':'CHA','cd':18,'ataque_magia':None,'sem_componentes':['material'],'3/day each':['comprehend languages','detect thoughts','telekinesis','wall of force']},
 'economia_lendaria':'3 ações lendárias; usa uma opção por vez ao fim do turno de outra criatura e recupera todas no início do próprio turno.',
 'acoes_lendarias':[act('Foretell','Rola 1d20 e registra o resultado. Até o fim do próximo turno do dragão, substitui por esse número qualquer rolagem de d20 sua ou de criatura a até 120 ft.; cada rolagem prevista só pode ser usada uma vez.'),act('Psionic Wave (custa 2 ações)','Usa Psionic Wave.',uso='2 legendary actions'),act('Shatter Mind (custa 2 ações)','Uma criatura a até 60 ft. faz salvaguarda de Inteligência CD 23; em falha sofre 22 (4d10) psychic ongoing damage. Repete a salvaguarda ao fim de cada turno, encerrando o dano contínuo em sucesso; uma ação para se ancorar à realidade também o encerra.',uso='2 legendary actions',salvaguarda='Intelligence DC 23',dano=[{'dados':'4d10 ongoing','tipo':'psychic'}])],
 'caracteristicas_de_covil':[tr('Academic Companion','Uma vez por dia, quando usaria Shatter Mind, pode invocar um mage aliado, que age na iniciativa do dragão.'),tr('Ancient Depictions','Murais e inscrições centenárias retratam qualquer criatura que entre no covil; quem vê a própria imagem fica Rattled enquanto permanecer nele.'),tr('Esoteric Layout','Testes de Perception e Survival para observar ou navegar no covil são feitos com desvantagem.'),tr('Prepared Welcome','Criaturas hostis ao dragão começam combate Surprised enquanto estiverem no covil.')],
 'nota_fonte':'A trait Legendary Resistance referencia Prophesy Doom, mas a página não apresenta ação com esse nome. Nenhuma regra para essa ação foi inferida; a mecânica restante está resumida, porém o registro não é contado como completo.',
 'secoes_nao_listadas':['alinhamento','salvaguardas de Força e Destreza','resistências e vulnerabilidades de dano','resistências ou vulnerabilidades a condições','ações bônus','reações','ações míticas','ações de covil','ação Prophesy Doom mencionada mas não listada'], 'completa':False,
 'url':'https://a5e.tools/node/1571', 'citation':'turn43view0'
},
'TF-096': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Huge', 'tipo_fonte':'dragon', 'alinhamento':'evil', 'variante':'Adult Shadow Dragon', 'nd_fonte':'19', 'ca':18, 'ca_base':'natural armor', 'pv':212, 'formula_pv':'17d12 + 102; bloodied 106',
 'deslocamento':{'walk_ft':40,'climb_ft':40,'fly_ft':80,'swim_ft':40}, 'scores':[22,14,22,14,14,23],
 'salvaguardas':{'DEX':8,'CON':12,'INT':8,'WIS':8}, 'pericias':{'Deception':12,'Insight':8,'Nature':8,'Perception':8,'Stealth':8}, 'pericias_bonus_dado':{'Stealth':'1d6'},
 'resistencias_dano':['acid','cold','fire','lightning','thunder','damage from nonmagical weapons'], 'imunidades_dano':['necrotic','poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue','frightened','grappled','paralyzed','poisoned','prone','restrained'],
 'sentidos':['darkvision 240 ft.'], 'percepcao_passiva':18, 'idiomas':['Common','Draconic'], 'bonus_proficiencia':6, 'maneuver_dc':20, 'tags':['Legendary'], 'terreno':['Caverns','The Bleak Gate'],
 'tracos':[tr('Evil','O dragão emana aura Evil.'),tr('Incorporeal Movement','Atravessa criaturas e objetos; se terminar o turno dentro de objeto, sofre 11 (2d10) force.'),tr('Legendary Resistance (3/Day)','Quando falha em salvaguarda, pode escolher obter sucesso; ao fazê-lo, torna-se mais sólido, perdendo o traço Incorporeal Movement (referido no texto como “Incorporeal trait”) e suas resistências a dano até o fim do próximo turno.'),tr('Essence Link','Ligado espiritualmente a uma área ou marco específico; não recebe benefício de descanso longo a mais de 1 milha dela. Se morrer, a área perde a essência vital até formar outro dragão de essência, processo que pode levar séculos. Quem entra pela primeira vez na área sem essência recebe 1 nível de Fatigue e 1 de Strife; ambos só podem ser removidos com descanso longo fora dela.'),tr('Innate Spellcasting','Conjuração por Carisma, CD 20, sem componentes materiais.')],
 'acoes':[act('Multiattack','Usa Grasp of Shadows e depois faz uma mordida e dois ataques de Claws.'),act('Bite','Ataque corpo a corpo +12, alcance 10 ft.; 22 (3d10+6) piercing e 4 (1d8) necrotic.',ataque='+12',alcance='10 ft.',dano=[{'dados':'3d10+6','tipo':'piercing'},{'dados':'1d8','tipo':'necrotic'}]),act('Claws','Ataque corpo a corpo +12, alcance 5 ft.; 19 (3d8+6) slashing e 4 (1d8) necrotic.',ataque='+12',alcance='5 ft.',dano=[{'dados':'3d8+6','tipo':'slashing'},{'dados':'1d8','tipo':'necrotic'}]),act('Grasp of Shadows','Alvo a até 60 ft. faz salvaguarda de Destreza CD 16; em falha fica Grappled por tentáculos de sombra (escape CD 20) e Restrained enquanto agarrado. O efeito termina se o dragão ficar Incapacitated ou usar esta habilidade novamente.',salvaguarda='Dexterity DC 16; escape DC 20',alcance='60 ft.'),act('Anguished Breath (Recharge 5–6)','Cone de 60 ft.; salvaguarda de Sabedoria CD 20, 67 (15d8) necrotic e 1 nível de Strife em falha, ou metade do dano em sucesso.',uso='Recharge 5–6',salvaguarda='Wisdom DC 20',alcance='60-ft. cone',dano=[{'dados':'15d8','tipo':'necrotic'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':{'atributo':'CHA','cd':20,'ataque_magia':None,'sem_componentes':['material'],'3/day each':['darkness','detect evil and good','bane','create undead']},
 'economia_lendaria':'3 ações lendárias; usa uma opção por vez ao fim do turno de outra criatura e recupera todas no início do próprio turno.',
 'acoes_lendarias':[act('Corrupting Presence','Criaturas escolhidas pelo dragão, a até 120 ft. e cientes dele, fazem salvaguarda de Sabedoria CD 16; em falha recebem 1 nível de Strife. Depois de passar ou falhar, cada alvo fica imune à presença por 24 horas.',salvaguarda='Wisdom DC 16',alcance='120 ft.'),act('Lurk','Em penumbra ou escuridão, fica invisível magicamente até atacar, provocar salvaguarda ou entrar em luz plena. Não pode usar se sofreu dano radiant desde o fim do próprio turno anterior.'),act('Slip Through Shadows','Em penumbra ou escuridão, teleporta até 45 ft. para espaço desocupado também em penumbra/escuridão. Não pode usar se sofreu dano radiant desde o fim do próprio turno anterior.',alcance='45 ft.'),act('Horrid Whispers (custa 2 ações)','Criatura que possa ouvir o dragão faz salvaguarda de Sabedoria CD 21; em falha sofre 13 (3d8) psychic e o dragão recupera a mesma quantidade de PV.',uso='2 legendary actions',salvaguarda='Wisdom DC 21',dano=[{'dados':'3d8','tipo':'psychic'}])],
 'caracteristicas_de_covil':[tr('Rotten Quagmire','Aproximadamente 90% do covil é terreno difícil pantanoso.'),tr('Shambling Undead','No início de cada rodada de combate, role 1d6; com 3–6, chegam 2d4 zombies na iniciativa do dragão. Lutam até morrer ou até receberem ordem verbal para parar.'),tr('Perpetual Twilight','Enquanto o dragão estiver presente, o covil não pode ser iluminado acima de penumbra, nem por meios mágicos.'),tr('Black Water','Como ação lendária, o dragão pode beber de uma poça e recuperar PV iguais ao valor de Constituição.')],
 'secoes_nao_listadas':['salvaguardas de Força e Carisma','vulnerabilidades de dano','resistências ou vulnerabilidades a condições','ações bônus','reações','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1559', 'citation':'turn43view1'
},
'TF-098': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Gargantuan', 'tipo_fonte':'dragon', 'alinhamento':'', 'variante':'Ancient Earth Dragon', 'nd_fonte':'24', 'ca':22, 'ca_base':'natural armor', 'pv':425, 'formula_pv':'23d20 + 184; bloodied 212',
 'deslocamento':{'walk_ft':40,'fly_ft':40,'burrow_ft':60}, 'scores':[26,14,26,16,22,14],
 'salvaguardas':{'STR':15,'CON':15,'INT':10,'WIS':13,'CHA':9}, 'pericias':{'Athletics':15,'Insight':13,'Nature':10,'Perception':13}, 'pericias_bonus_dado':{'Insight':'1d6','Perception':'1d6'},
 'resistencias_dano':['damage from nonmagical weapons'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['petrified'],
 'sentidos':['darkvision 120 ft.','tremorsense 120 ft.'], 'percepcao_passiva':26, 'idiomas':['Common','Draconic','Terran'], 'bonus_proficiencia':7, 'maneuver_dc':23, 'tags':['Legendary'], 'terreno':['Desert','Hills','Mountains'],
 'tracos':[tr('Earth Glide','Escava terra e pedra natural não trabalhada sem perturbá-las.'),tr('False Appearance','Imóvel dentro da área vinculada, é indistinguível de um afloramento rochoso natural.'),tr('Legendary Resistance (3/Day)','Quando falha em salvaguarda, pode escolher obter sucesso; ao fazê-lo, seus deslocamentos de caminhada, escavação e voo são reduzidos à metade até o fim do próximo turno.'),tr('Essence Link','Ligado espiritualmente a uma área ou marco específico; não recebe benefício de descanso longo a mais de 1 milha dela. Se morrer, a área perde a essência vital até formar outro dragão de essência, processo que pode levar séculos. Quem entra pela primeira vez na área sem essência recebe 1 nível de Fatigue e 1 de Strife; ambos só podem ser removidos com descanso longo fora dela.'),tr('Innate Spellcasting','Conjuração por Carisma, CD 17, sem componentes materiais.')],
 'acoes':[act('Multiattack','Faz uma mordida e dois ataques de Slam. Em vez da mordida, pode usar Rock Spire.'),act('Bite','Ataque corpo a corpo +15, alcance 15 ft.; 35 (5d10+8) piercing. Em vez do dano, pode agarrar (escape CD 23); criatura Huge ou menor agarrada fica Restrained. Enquanto mantém a criatura agarrada, não pode morder outro alvo.',ataque='+15',alcance='15 ft.',dano=[{'dados':'5d10+8','tipo':'piercing'}],salvaguarda='escape DC 23'),act('Slam','Ataque corpo a corpo +15, alcance 10 ft.; 21 (3d8+8) bludgeoning, empurra até 10 ft. e deixa Prone se colidir com parede ou objeto sólido. Causa 9 (2d8) bludgeoning adicional se o alvo já estava Prone.',ataque='+15',alcance='10 ft.',dano=[{'dados':'3d8+8','tipo':'bludgeoning'}]),act('Scouring Breath (Recharge 5–6)','Cone de 90 ft.; salvaguarda de Destreza CD 23, 70 (20d6) slashing em falha ou metade em sucesso. Falha também deixa a criatura Blinded até o fim do próximo turno.',uso='Recharge 5–6',salvaguarda='Dexterity DC 23',alcance='90-ft. cone',dano=[{'dados':'20d6','tipo':'slashing'}]),act('Rock Spire','Ergue permanentemente uma coluna rochosa de 25 ft. de altura e raio de 5 ft. a partir de ponto no chão a até 60 ft. Criatura na área quando surge faz salvaguarda de Destreza CD 21, sofrendo 18 (4d8) piercing em falha ou metade em sucesso. Falha por 10 ou mais empala e deixa Restrained no topo. Uma ação e teste de Força CD 13 libertam-na; destruir a coluna também a liberta. A coluna é objeto com CA 16, 30 PV e imunidade a poison e psychic.',salvaguarda='Dexterity DC 21; escape Strength DC 13',alcance='60 ft.',dano=[{'dados':'4d8','tipo':'piercing'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':{'atributo':'CHA','cd':17,'ataque_magia':None,'sem_componentes':['material'],'3/day each':['locate animals or plants','spike growth','stone shape','wall of stone'],'1/day':['earthquake','move earth']},
 'economia_lendaria':'3 ações lendárias; usa uma opção por vez ao fim do turno de outra criatura e recupera todas no início do próprio turno.',
 'acoes_lendarias':[act('Shake the Foundation','Torna permanentemente terreno difícil uma área de raio 40 ft. centrada em ponto que vê. Se estiver Bloodied, criaturas na área fazem salvaguarda de Destreza CD 23; falha causa 21 (6d6) slashing e Prone, sucesso causa metade do dano.'),act('Slam Attack (custa 2 ações)','Faz um ataque Slam.',uso='2 legendary actions'),act('Entomb (Bloodied; custa 3 ações)','Alvo no chão a até 60 ft. faz salvaguarda de Destreza CD 17; em falha é enterrado magicamente 5 ft. sob a terra, Blinded, Restrained e sem poder respirar. Uma ação e teste de Força CD 17 libertam a criatura.',uso='while bloodied; 3 legendary actions',salvaguarda='Dexterity DC 17; escape Strength DC 17')],
 'caracteristicas_de_covil':[tr('Desolate Peak','A jornada até o covil na montanha aciona o dobro dos desafios de exploração usuais.'),tr('Jagged Stone','Quando o dragão acerta com Slam uma criatura a até 5 ft. de uma parede do covil, ela sofre 5 (1d10) piercing adicionais.'),tr('Volcanic Lair','Ao morder criatura agarrada, pode mergulhá-la em magma em vez de causar o dano piercing; sofre dano fire igual ao dano piercing que a mordida causaria.'),tr('Loose Sand','Seu deslocamento de escavação aumenta para 100 ft.; pode usar Scouring Breath revelando apenas o focinho e mantendo cobertura de três quartos.')],
 'secoes_nao_listadas':['alinhamento','salvaguarda de Destreza','imunidades e vulnerabilidades de dano','resistências ou vulnerabilidades a condições','ações bônus','reações','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1550', 'citation':'turn43view2'
},
'TF-183': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'humanoid', 'alinhamento':'', 'variante':'Aboleth Thrall', 'nd_fonte':'2', 'ca':12, 'ca_base':'', 'pv':45, 'formula_pv':'7d8 + 14; bloodied 22',
 'deslocamento':{'walk_ft':30,'swim_ft':30}, 'scores':[14,14,14,10,10,12],
 'salvaguardas':{}, 'pericias':{}, 'pericias_nao_especificadas':'A fonte indica “Any one skill”, sem informar qual perícia nem o bônus.', 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':[], 'percepcao_passiva':10, 'idiomas':['Common','unlimited-range telepathy with aboleth'], 'bonus_proficiencia':2, 'maneuver_dc':12, 'terreno':['Caverns','Settlement','Water'],
 'tracos':[tr('Sea Changed','Respira água e ar, mas precisa banhar-se em água por 1 hora a cada 12 horas que passar seco; caso contrário, começa a sufocar. É magicamente Charmed pelo aboleth.')],
 'acoes':[act('Poison Ink Knife','Ataque corpo a corpo +4, alcance 5 ft.; 4 (1d4+2) slashing e 10 (3d6) poison.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d4+2','tipo':'slashing'},{'dados':'3d6','tipo':'poison'}])],
 'acoes_bonus':[], 'reacoes':[act('Self-Sacrifice','Quando uma criatura a até 5 ft. do thrall que ele possa ver acerta um aboleth com um ataque, o thrall pode tornar-se alvo do ataque em seu lugar.')], 'conjuracao':None,
 'secoes_nao_listadas':['alinhamento','salvaguardas','perícias específicas e bônus (a fonte só diz “Any one skill”)','resistências, imunidades e vulnerabilidades a dano','imunidades ou resistências a condições','ações bônus','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/1435', 'citation':'turn42view3'
},
'TF-185': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'humanoid', 'alinhamento':'evil', 'variante':'Alleyway Strangler', 'nd_fonte':'4', 'ca':14, 'ca_base':'padded cloth', 'pv':78, 'formula_pv':'12d8 + 24; bloodied 39',
 'deslocamento':{'walk_ft':30,'climb_ft':20}, 'scores':[12,16,15,13,12,15],
 'salvaguardas':{'STR':3,'DEX':3,'CON':4,'INT':1,'WIS':1,'CHA':2}, 'pericias':{'Deception':4,'Perception':3,'Stealth':5,'thieves’ tools':5}, 'pericias_bonus_dado':{'Deception':'1d8','Perception':'1d4','Stealth':'1d8'},
 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[], 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':15, 'idiomas':['Common'], 'bonus_proficiencia':2, 'maneuver_dc':13, 'terreno':['Settlement'],
 'tracos':[tr('Bundled Prey (1/Turn)','Tem vantagem em ataques contra criaturas Grappled.'),tr('Evil','Emana aura Evil.'),tr('Hide in the Crowd','Tem vantagem em testes de Stealth para esconder-se em multidão.'),tr('Sneak Attack (1/Turn)','Causa 10 (3d6) de dano adicional ao acertar com ataque de arma quando tem vantagem no ataque, ou quando o alvo está a até 5 ft. de um aliado do strangler e ele não tem desvantagem no ataque.')],
 'acoes':[act('Multiattack','Faz dois ataques.'),act('Garrote (1/Turn)','Ataque corpo a corpo +5, alcance 5 ft., contra uma criatura viva Large ou menor; em acerto, agarra (escape CD 13). Enquanto agarrada dessa forma, sofre 5 (2d4) bludgeoning ongoing damage e não pode falar. O strangler não pode usar o garrote contra outra criatura enquanto o mantém nessa vítima.',ataque='+5',alcance='5 ft.',uso='1/turn',salvaguarda='escape DC 13',dano=[{'dados':'2d4 ongoing','tipo':'bludgeoning'}]),act('Dueling Dagger','Ataque corpo a corpo +5, alcance 5 ft.; 5 (1d4+3) piercing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d4+3','tipo':'piercing'}]),act('Throwing Dagger','Ataque à distância +5, alcance 30/80 ft.; 5 (1d4+3) piercing.',ataque='+5',alcance='30/80 ft.',dano=[{'dados':'1d4+3','tipo':'piercing'}])],
 'acoes_bonus':[act('Lock Garrote','Trava juntas as alças do garrote, encerrando a condição Grappled da vítima atingida. Ela continua sofrendo 5 (2d4) bludgeoning ongoing damage e não pode falar; também não consegue respirar e começa a sufocar. Uma criatura pode destravá-lo gastando uma ação e passando em teste de thieves’ tools CD 15 ou de Força CD 15, ou usando uma chave própria. O garrote trancado tem CA 18, 12 PV e resistência a fire, bludgeoning e piercing.')],
 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas adicionais além das seis listadas','resistências, imunidades e vulnerabilidades a dano','imunidades ou resistências a condições','reações','conjuração','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/5497', 'citation':'turn42view4'
},
'TF-001': {
 'fonte_publicacao':'Creature Codex', 'editora_fonte':'Kobold Press / Open Design LLC', 'sistema':'D&D 5e (bloco atribuído a Kobold Press, hospedado pelo 5eSRD)',
 'porte':'Large', 'tipo_fonte':'aberration', 'alinhamento':'neutral evil', 'nd_fonte':'3', 'ca':14, 'ca_base':'clockwork armor', 'pv':67, 'formula_pv':'9d10 + 18 (armadura; forma interna com 37 PV, 5d10 + 10)',
 'deslocamento':{'walk_ft':30,'fly_ft':30,'swim_ft':30}, 'scores':[17,15,14,19,13,10],
 'salvaguardas':{}, 'pericias':{'Perception':3}, 'resistencias_dano':[], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','exhaustion','frightened','paralyzed','petrified','poisoned','prone'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':13, 'idiomas':['Deep Speech','Void Speech'], 'bonus_proficiencia':2, 'bonus_proficiencia_origem':'derivado do ND 3 pela tabela padrão de proficiência de D&D 5e; não impresso no bloco',
 'tracos':[tr('Clockwork Encasement','A criatura é protegida por armadura mecânica com manipuladores. Ao chegar a 0 PV, a armadura quebra e a criatura emerge. Na forma interna: CA 12, 37 PV (5d10+10), Força 9 (-1), todos os deslocamentos caem a 20 ft. e perde ações de ataque, mas ainda pode conjurar. Mantém apenas imunidade a dano psíquico e à condição Prone; os demais benefícios de imunidade da armadura se perdem. Os apêndices podem manipular objetos, mas não atacar; as janelas da armadura podem ser abertas sem ação. Pode entrar ou sair da armadura como ação bônus.'), tr('Immutable Form','A armadura mecânica é imune a magias ou efeitos que alterariam sua forma; a criatura também é protegida enquanto permanece dentro dela.'), tr('Innate Spellcasting','Conjuração por Inteligência, CD 14, +6 para acertar com ataques mágicos; sem componentes materiais. Magias à vontade: fear, fire bolt (2d10), telekinesis.')],
 'acoes':[act('Multiattack','Faz três ataques corpo a corpo; pode substituir dois ataques por uma magia à vontade.'), act('Whirring Blades','Ataque corpo a corpo +5, alcance 5 ft.; 2d4+3 slashing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'2d4+3','tipo':'slashing'}]), act('Pronged Scepter','Ataque corpo a corpo +5, alcance 10 ft.; 1d6+3 piercing.',ataque='+5',alcance='10 ft.',dano=[{'dados':'1d6+3','tipo':'piercing'}]), act('Bashing Rod','Ataque corpo a corpo +5, alcance 5 ft.; 1d10+3 bludgeoning.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d10+3','tipo':'bludgeoning'}])],
 'acoes_bonus':[act('Enter or Exit Clockwork Armor','Entra ou sai da armadura mecânica como ação bônus; ao emergir aplicam-se as estatísticas internas e as limitações descritas em Clockwork Encasement.')], 'reacoes':[], 'conjuracao':{'atributo':'INT','cd':14,'ataque_magia':'+6','sem_componentes':['material'],'at_will':['fear','fire bolt (2d10)','telekinesis']},
 'secoes_nao_listadas':['salvaguardas','resistências de dano','vulnerabilidades','ações especiais além dos traços','reações','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.5esrd.com/database/creature/ahu-nixta/', 'citation':'turn24view0'
},
'TF-003': {
 'fonte_publicacao':'Tome of Beasts 1', 'editora_fonte':'Kobold Press / Open Design LLC', 'sistema':'D&D 5e (bloco atribuído a Kobold Press, hospedado pelo 5eSRD)',
 'porte':'Large', 'tipo_fonte':'aberration', 'alinhamento':'chaotic evil', 'nd_fonte':'5', 'ca':14, 'ca_base':'natural armor', 'pv':102, 'formula_pv':'12d10 + 36',
 'deslocamento':{'walk_ft':40,'climb_ft':15}, 'scores':[18,13,17,11,10,5],
 'salvaguardas':{}, 'pericias':{'Acrobatics':4,'Perception':3,'Stealth':4}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':13, 'idiomas':['Giant'], 'bonus_proficiencia':3,
 'tracos':[tr('Spider Climb','Escala superfícies difíceis, inclusive tetos de cabeça para baixo, sem teste de atributo.')],
 'acoes':[act('Multiattack','Faz um ataque de Bite e um de Claws.'), act('Bite','Ataque corpo a corpo +7, alcance 5 ft.; 2d10+4 piercing. Alvo criatura faz salvaguarda de Constituição CD 14; em falha sofre 2d10 poison e contrai doença, ficando Poisoned até a doença terminar. Repete o teste a cada 24 horas: sucesso encerra a doença; falha reduz o máximo de PV em 1d10 (5 em média), redução que dura até a doença terminar. Se o máximo chegar a 0, morre.',ataque='+7',alcance='5 ft.',dano=[{'dados':'2d10+4','tipo':'piercing'},{'dados':'2d10','tipo':'poison em falha na salvaguarda'}],salvaguarda='Constitution DC 14'), act('Claws','Ataque corpo a corpo +7, alcance 10 ft.; 3d10+4 piercing e agarra o alvo (fuga CD 14). Enquanto agarrado, fica Restrained e o asanbosam não pode usar Claws contra outro alvo. Alvo criatura faz salvaguarda de Constituição CD 14 ou contrai a doença descrita em Bite.',ataque='+7',alcance='10 ft.',dano=[{'dados':'3d10+4','tipo':'piercing'}],salvaguarda='Constitution DC 14; escape DC 14')],
 'acoes_bonus':[act('Arboreal Escape','Enquanto estiver em uma árvore, usa Disengage ou Hide como ação bônus.')], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','resistências, imunidades e vulnerabilidades','imunidades a condições','reações','conjuração','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.5esrd.com/database/creature/asanbosam-3pp/', 'citation':'turn24view1'
},
'TF-006': {
 'fonte_publicacao':'Creature Codex', 'editora_fonte':'Kobold Press / Open Design LLC', 'sistema':'D&D 5e (bloco atribuído a Kobold Press, hospedado pelo 5eSRD)',
 'porte':'Medium', 'tipo_fonte':'aberration', 'alinhamento':'chaotic neutral', 'nd_fonte':'3', 'ca':15, 'ca_base':'natural armor', 'pv':65, 'formula_pv':'10d8 + 20',
 'deslocamento':{'walk_ft':30}, 'scores':[17,12,15,10,13,15],
 'salvaguardas':{}, 'pericias':{'Deception':4,'Perception':5}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':15, 'idiomas':['Common'], 'bonus_proficiencia':2, 'bonus_proficiencia_origem':'derivado do ND 3 pela tabela padrão de proficiência de D&D 5e; não impresso no bloco',
 'tracos':[tr('Disguise','Tem vantagem em testes de Deception para se passar pelo tipo de criatura que imita, desde que possua ao menos uma característica desse tipo.'), tr('Trait Mimicry','Como ação bônus, copia uma característica física, ataque ou reação não mágico de besta ou humanoide com ND igual ou inferior a 3 que tenha visto na última semana. Pode manter até cinco características simultâneas, no máximo dois ataques; substitui uma ao usar novamente e perde todas após uma semana sem exposição a besta ou humanoide. Não copia swarm, shapechanger, Change Shape ou características/ataques/reações de Spellcasting. Ataques copiados causam sempre 1d10+3 (8 em média) do tipo normal; CD de salvaguarda fixa 13. Pode copiar condições adicionais do ataque, como grapple ou prone, mas não veneno; precisa satisfazer pré-requisitos. Também copia locomoção natural, não mágica, de besta/humanoide à própria velocidade.')],
 'acoes':[act('Multiattack','Faz dois ataques corpo a corpo.'), act('Slam','Ataque corpo a corpo +5, alcance 5 ft.; 1d10+3 bludgeoning.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d10+3','tipo':'bludgeoning'}])],
 'acoes_bonus':[act('Trait Mimicry','Adquire ou substitui uma característica física, ataque, reação ou modo natural de locomoção elegível observado na última semana, conforme os limites do traço Trait Mimicry.')], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','resistências, imunidades e vulnerabilidades','imunidades a condições','reações','conjuração','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.5esrd.com/database/creature/xenabsorber/', 'citation':'turn24view2'
},
'TF-484': {
 'fonte_publicacao':'Flee, Mortals! (prévia)', 'editora_fonte':'MCDM Productions', 'sistema':'D&D 5e; estatísticas e ações de MCDM conforme prévia da editora; sem conversão para outra edição.', 'papel_fonte':'Ambusher', 'xp_fonte':100,
 'porte':'Small', 'tipo_fonte':'Humanoid (Goblin)', 'alinhamento':'Any Alignment', 'nd_fonte':'1/2', 'ca':15, 'ca_base':'studded leather armor', 'pv':16, 'formula_pv':'3d6 + 6',
 'deslocamento':{'walk_ft':30,'climb_ft':20}, 'scores':[8,16,14,10,10,8],
 'salvaguardas':{}, 'pericias':{'Stealth':7}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':10, 'idiomas':['Common','Goblin'], 'bonus_proficiencia':2,
 'tracos':[tr('Backstab','Quando tem vantagem contra criatura que não seja Construct ou Undead, o ataque causa 1d6 extra e aplica uma ferida sangrante. Cada ferida reduz os PV atuais em 2 no início do turno da vítima; a condição termina quando ela recupera ao menos 1 PV ou quando qualquer criatura usa uma ação para estancar todas as feridas.'), tr('Crafty','Ao sair do alcance de uma criatura inimiga, não provoca ataques de oportunidade.')],
 'acoes':[act('Scimitar','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 slashing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'slashing'}]), act('Dagger','Ataque corpo a corpo ou à distância +5, alcance 5 ft. ou 20/60 ft.; 1d4+3 piercing.',ataque='+5',alcance='5 ft. ou 20/60 ft.',dano=[{'dados':'1d4+3','tipo':'piercing'}]), act('Summon Shadows','1/dia; cria escuridão mágica em esfera de raio 10 ft. por 1 minuto, originada em ponto visível. O assassino enxerga através dela. No início de seu turno, pode movê-la até 30 ft. para ponto visível; sofrer dano encerra o efeito.')],
 'acoes_bonus':[act('Sneak','Usa a ação Hide como ação bônus.')], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','defesas especiais','Multiattack','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://mcdm.gg/FleeMortals/FleeMortalsPreview.pdf', 'citation':'turn72search0'
},
'TF-485': {
 'fonte_publicacao':'Flee, Mortals! (prévia)', 'editora_fonte':'MCDM Productions', 'sistema':'D&D 5e; estatísticas e ações de MCDM conforme prévia da editora; sem conversão para outra edição.', 'papel_fonte':'Support', 'xp_fonte':450,
 'porte':'Small', 'tipo_fonte':'Humanoid (Goblin)', 'alinhamento':'Any Alignment', 'nd_fonte':'2', 'ca':17, 'ca_base':'studded leather armor, shield', 'pv':36, 'formula_pv':'8d6 + 8',
 'deslocamento':{'walk_ft':30,'climb_ft':20}, 'scores':[10,16,13,12,12,10],
 'salvaguardas':{'DEX':5,'WIS':3}, 'pericias':{'Insight':3,'Intimidation':2,'Stealth':5}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':11, 'idiomas':['Common','Goblin'], 'bonus_proficiencia':2,
 'tracos':[tr('Crafty','Ao sair do alcance de uma criatura inimiga, não provoca ataques de oportunidade.')],
 'acoes':[act('Multiattack','Faz dois ataques de Shortsword ou Shortbow; pode substituir um ataque por Command.'), act('Shortsword','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 piercing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'piercing'}]), act('Shortbow','Ataque à distância +5, alcance 80/320 ft.; 1d6+3 piercing.',ataque='+5',alcance='80/320 ft.',dano=[{'dados':'1d6+3','tipo':'piercing'}]), act('Command','Escolhe aliado visível a até 30 ft.; se puder ouvir o boss, usa a reação para mover até seu deslocamento ou fazer um ataque com arma.')],
 'acoes_bonus':[act('Get Reckless','Recarga 6; aliados voluntários a até 30 ft. que possam ouvi-lo ficam reckless até o início do próximo turno do boss: têm vantagem em jogadas de ataque, mas ataques contra eles também têm vantagem.',uso='Recharge 6')],
 'reacoes':[act('Cowardly Commander','Quando uma criatura que o boss vê o acerta, escolhe um aliado voluntário a até 5 ft.; esse aliado recebe o ataque.')], 'conjuracao':None,
 'secoes_nao_listadas':['defesas especiais','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://mcdm.gg/FleeMortals/FleeMortalsPreview.pdf', 'citation':'turn69search0'
},
'TF-486': {
 'fonte_publicacao':'Flee, Mortals! (prévia)', 'editora_fonte':'MCDM Productions', 'sistema':'D&D 5e; estatísticas e ações de MCDM conforme prévia da editora; sem conversão para outra edição.', 'papel_fonte':'Controller', 'xp_fonte':200,
 'porte':'Small', 'tipo_fonte':'Humanoid (Goblin)', 'alinhamento':'Any Alignment', 'nd_fonte':'1', 'ca':15, 'ca_base':'leather armor, shield', 'pv':27, 'formula_pv':'5d6 + 10',
 'deslocamento':{'walk_ft':30,'climb_ft':20}, 'scores':[8,14,14,10,10,15],
 'salvaguardas':{'WIS':2}, 'pericias':{'Stealth':4}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':10, 'idiomas':['Common','Goblin'], 'bonus_proficiencia':2,
 'tracos':[tr('Crafty','Ao sair do alcance de uma criatura inimiga, não provoca ataques de oportunidade.')],
 'acoes':[act('Toxic Touch','Ataque mágico corpo a corpo ou à distância +4, alcance 5 ft. ou 30 ft.; 2d6 poison. Alvo faz salvaguarda de Constituição CD 12 ou fica Poisoned por 1 minuto, com salvaguarda ao fim de cada turno para encerrar.'), act('Brittle Bone Hex','Escolhe criatura visível a até 60 ft.; até o fim do próximo turno do cursespitter, na primeira vez em que o alvo se mover voluntariamente ou usar ação, ação bônus ou reação, faz salvaguarda de Constituição CD 12; falha causa 2d8 necrotic.'), act('Dizzying Hex','2/dia; escolhe criatura visível a até 60 ft. para salvaguarda de Sabedoria CD 12. Falha derruba Prone e impede levantar por até 1 minuto; a criatura repete a salvaguarda ao fim de cada turno.',uso='2/day',salvaguarda='Wisdom DC 12')],
 'acoes_bonus':[act('To Me!','Escolhe até duas criaturas voluntárias visíveis a até 30 ft.; cada uma teleporta para espaço desocupado a até 5 ft. do cursespitter.')],
 'reacoes':[act('Cowardly Commander','Quando uma criatura que vê o cursespitter o acerta, escolhe um aliado voluntário a até 5 ft.; esse aliado recebe o ataque.')], 'conjuracao':None,
 'secoes_nao_listadas':['defesas especiais','Multiattack','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://mcdm.gg/FleeMortals/FleeMortalsPreview.pdf', 'citation':'turn69search0'
},
'TF-487': {
 'fonte_publicacao':'Where Evil Lives (prévia)', 'editora_fonte':'MCDM Productions', 'sistema':'D&D 5e; estatísticas e ações de vilão de MCDM conforme prévia da editora; sem conversão para outra edição.', 'papel_fonte':'Leader', 'xp_fonte':700,
 'porte':'Small', 'tipo_fonte':'Humanoid (Goblin)', 'alinhamento':'Neutral Evil', 'nd_fonte':'3', 'ca':17, 'ca_base':'studded leather, shield', 'pv':54, 'formula_pv':'12d6 + 12',
 'deslocamento':{'walk_ft':30,'climb_ft':20}, 'scores':[10,17,13,14,12,13],
 'salvaguardas':{'DEX':5,'WIS':3}, 'pericias':{'Insight':3,'Intimidation':3,'Perception':3,'Stealth':5}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':13, 'idiomas':['Common','Goblin'], 'bonus_proficiencia':2,
 'tracos':[tr('Crafty','Ao sair do alcance de uma criatura inimiga, não provoca ataques de oportunidade.'), tr('Take My Pain','3/dia; ao falhar em salvaguarda contra magia ou outro efeito sobrenatural, escolhe criatura voluntária a até 30 ft. A Queen tem sucesso e a criatura escolhida é tratada como alvo do mesmo efeito, falhando automaticamente na salvaguarda.',uso='3/day')],
 'acoes':[act('Multiattack','Faz três ataques de Shortsword ou dois de Shortbow.'), act('Shortsword','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 piercing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'piercing'}]), act('Shortbow','Ataque à distância +5, alcance 80/320 ft.; 1d6+3 piercing.',ataque='+5',alcance='80/320 ft.',dano=[{'dados':'1d6+3','tipo':'piercing'}])],
 'acoes_bonus':[act('Get In Here','Convoca 1d4 goblin lackeys, que aparecem em espaços desocupados a até 60 ft.')],
 'reacoes':[act('No Dying!','Quando aliado visível a até 30 ft. chega a 0 PV, reduz o resultado a 1 PV.')],
 'acoes_de_vilao':[act('What Are You Waiting For?!','Uma vez por encontro, após o turno de inimigo: aliados escolhidos a até 60 ft. que possam ouvi-la podem mover até seu deslocamento ou fazer ataque corpo a corpo sem ação.'), act('Focus Fire','Uma vez por encontro, após o turno de inimigo: escolhe inimigo visível a até 60 ft.; Queen e aliados escolhidos a até 60 ft. que possam ouvi-la podem mover até seu deslocamento em direção ao alvo, sem ação.'), act('Kill!','Uma vez por encontro, após o turno de inimigo: aliados escolhidos a até 60 ft. que possam ouvi-la fazem um ataque com arma com vantagem; acerto causa 1d6 extra. Cada ação de vilão só pode ser usada uma vez no encontro e apenas uma por rodada.')],
 'conjuracao':None,
 'secoes_nao_listadas':['defesas especiais','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://files.mcdmproductions.com/Evil/WhereEvilLives-Preview.pdf', 'citation':'turn60search1'
},
'TF-488': {
 'fonte_publicacao':'Flee, Mortals! (prévia)', 'editora_fonte':'MCDM Productions', 'sistema':'D&D 5e; estatísticas e ações de MCDM conforme prévia da editora; sem conversão para outra edição.', 'papel_fonte':'Brute', 'xp_fonte':700,
 'porte':'Huge', 'tipo_fonte':'Beast', 'alinhamento':'Unaligned', 'nd_fonte':'3', 'ca':15, 'ca_base':'natural armor', 'pv':73, 'formula_pv':'7d12 + 28',
 'deslocamento':{'walk_ft':40,'climb_ft':40}, 'scores':[18,14,18,2,11,4],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['blindsight 10 ft.','darkvision 60 ft.'], 'percepcao_passiva':10, 'idiomas':[], 'bonus_proficiencia':2,
 'tracos':[tr('Baby Burst','Quando morre, uma swarm de spiders sai de seus restos e age na mesma contagem de iniciativa.'), tr('Rider Launcher','Aliado que salta da aranha pode fazer salto em distância de 30 ft. ou salto em altura de 15 ft., com ou sem corrida; seu primeiro ataque corpo a corpo com arma no mesmo turno tem vantagem.'), tr('Spider Climb','Escala superfícies difíceis, inclusive tetos de cabeça para baixo, sem teste.'), tr('Web Walker','Ignora restrições de movimento causadas por teias.'), tr('Wide Back','Duas criaturas Small ou Tiny podem compartilhar espaço montadas nela; capacidade máxima de 18 Small ou 64 Tiny.')],
 'acoes':[act('Bite','Ataque corpo a corpo +6, alcance 5 ft.; 2d6+4 piercing e 2d6 poison.',ataque='+6',alcance='5 ft.',dano=[{'dados':'2d6+4','tipo':'piercing'},{'dados':'2d6','tipo':'poison'}]), act('Bladed Leg','Ataque corpo a corpo +6, alcance 10 ft.; 2d6+4 slashing.',ataque='+6',alcance='10 ft.',dano=[{'dados':'2d6+4','tipo':'slashing'}]), act('Web Spray','Cubo de teias de 15 ft.; cada criatura na área faz salvaguarda de Destreza CD 13 ou fica Restrained. Uma ação permite a si ou a criatura alcançável tentar teste de Força ou Destreza CD 13 para se libertar.'), act('Trample','Recarga 6; move até o deslocamento através dos espaços de outras criaturas e faz um ataque Bladed Leg contra cada criatura cujo espaço atravessar. Alvo atingido não pode usar reações até o início do próximo turno.',uso='Recharge 6')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','perícias','defesas especiais','Multiattack','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://files.mcdmproductions.com/FleeMortals/FleeMortalsPreview.pdf', 'citation':'turn71search0'
},
'TF-489': {
 'fonte_publicacao':'Flee, Mortals! (prévia)', 'editora_fonte':'MCDM Productions', 'sistema':'D&D 5e; estatísticas e ações de MCDM conforme prévia da editora; sem conversão para outra edição.', 'papel_fonte':'Soldier', 'xp_fonte':450,
 'porte':'Medium', 'tipo_fonte':'Swarm of Tiny Beasts', 'alinhamento':'Unaligned', 'nd_fonte':'2', 'ca':13, 'ca_base':'', 'pv':36, 'formula_pv':'8d8',
 'deslocamento':{'walk_ft':30,'fly_ft':60}, 'scores':[10,16,10,3,12,5],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['bludgeoning','piercing','slashing'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','frightened','grappled','paralyzed','petrified','prone','restrained','stunned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':11, 'idiomas':[], 'bonus_proficiencia':2,
 'tracos':[tr('In Your Face','Enquanto ocupa o espaço de inimigo, este tem desvantagem em ataques contra qualquer alvo que não seja o swarm e sofre 1d6 slashing se atacar outra criatura.'), tr('Swarm','Pode ocupar o espaço de outra criatura e vice-versa, e passar por aberturas que comportem um skitterling Tiny; não recupera PV nem recebe PV temporários.')],
 'acoes':[act('Claws','Ataque corpo a corpo +5, alcance 0 ft., contra alvo no espaço do swarm; 4d6 slashing, ou 2d6 quando o swarm tem metade dos PV ou menos. Alvo faz salvaguarda de Constituição CD 10 ou fica Blinded até o início do próximo turno. Criatura imune a poison ou à condição Poisoned tem sucesso automático.',ataque='+5',alcance='0 ft.',dano=[{'dados':'4d6 (ou 2d6 com metade dos PV ou menos)','tipo':'slashing'}],salvaguarda='Constitution DC 10')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','perícias','defesas especiais','Multiattack','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://files.mcdmproductions.com/FleeMortals/FleeMortalsPreview.pdf', 'citation':'turn71search0'
},
'TF-490': {
 'fonte_publicacao':'Where Evil Lives (prévia)', 'editora_fonte':'MCDM Productions', 'sistema':'D&D 5e; regras de minion de MCDM conforme prévia da editora; sem conversão para outra edição.', 'papel_fonte':'Minion', 'xp_fonte':10,
 'porte':'Small', 'tipo_fonte':'Humanoid (Goblin)', 'alinhamento':'Any Alignment', 'nd_fonte':'1/4', 'ca':14, 'ca_base':'leather armor, shield', 'pv':6, 'formula_pv':'6 (valor fixo de minion)',
 'deslocamento':{'walk_ft':30,'climb_ft':20}, 'scores':[8,13,10,10,8,8],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':9, 'idiomas':['Common','Goblin'], 'bonus_proficiencia':2,
 'tracos':[tr('Crafty','Ao sair do alcance de uma criatura inimiga, não provoca ataques de oportunidade.'), tr('Minion','Dano de ataque ou de salvaguarda fracassada reduz seus PV a 0. Outro dano só o mata quando iguala ou supera seu máximo de PV; caso contrário, não causa dano.'), tr('Tiny Stabs','Se inimigo inicia turno a até 5 ft. de pelo menos três lackeys que o veem, faz salvaguarda de Destreza contra CD 10 + quantidade de lackeys nessa distância; falha causa 1 piercing por lackey adjacente.')],
 'acoes':[act('Dagger (Group Attack)','Ataque com arma corpo a corpo ou à distância +3, alcance informado de 20/60 ft.; um alvo, 1 piercing.',ataque='+3',alcance='20/60 ft.',dano=[{'dados':'1','tipo':'piercing'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','perícias','defesas especiais','Multiattack','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://files.mcdmproductions.com/Evil/WhereEvilLives-Preview.pdf', 'citation':'turn54search0'
},
'TF-275': {
 'fonte_publicacao':"Dungeon Delver's Guide", 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Abyss','Water'],
 'porte':'Medium', 'tipo_fonte':'Aberration', 'alinhamento':'', 'nd_fonte':'4', 'ca':13, 'ca_base':'', 'pv':71, 'formula_pv':'11d8 + 22; bloodied 35',
 'deslocamento':{'walk_ft':0,'fly_ft':40,'fly_hover':True,'swim_ft':40}, 'scores':[10,16,14,3,10,6],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['bludgeoning','piercing','slashing'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','frightened','grappled','paralyzed','petrified','prone','restrained','stunned','unconscious'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':10, 'idiomas':['Deep Speech'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Aberrant Physiology','Não precisa respirar nem dormir.'), tr('Swarm','Pode ocupar o espaço de outra criatura e atravessar aberturas para criatura Tiny; não pode ganhar PV nem PV temporários.'), tr('Whispers of the Weird','Sussurra continuamente. Criatura que inicia turno a até 5 ft. e consegue ouvir faz salvaguarda de Sabedoria CD 13 ou sofre 3d6 psychic.')],
 'acoes':[act('Bites','Ataque corpo a corpo +5, alcance 0 ft., um alvo; 4d6+3 piercing, reduzido para 2d6+3 quando a swarm está bloodied.',ataque='+5',alcance='0 ft.',dano=[{'dados':'4d6+3 (ou 2d6+3 quando bloodied)','tipo':'piercing'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Na seção de combate, move-se até o espaço do não-aberration mais próximo e o ataca; luta até a morte.',
 'secoes_nao_listadas':['salvaguardas','perícias','imunidades e vulnerabilidades a dano','Multiattack','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/2840', 'citation':'turn78view0'
},
'TF-291': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Tundra'],
 'porte':'Large', 'tipo_fonte':'Beast', 'alinhamento':'', 'nd_fonte':'1', 'ca':14, 'ca_base':'natural armor', 'pv':30, 'formula_pv':'4d10 + 8; bloodied 15',
 'deslocamento':{'walk_ft':40,'climb_ft':15}, 'scores':[15,13,14,2,11,6],
 'salvaguardas':{}, 'pericias':{'Survival':3}, 'resistencias_dano':['cold','poison'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':[], 'percepcao_passiva':11, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[tr('Charge','Se avançar ao menos 20 ft. em linha reta até o alvo e acertá-lo com Tusk no mesmo turno, causa 1d6 slashing extra; alvo criatura faz salvaguarda de Força CD 12 ou cai Prone.'), tr('Hard Stomach','Tem vantagem nas salvaguardas contra poison e consegue comer quase qualquer coisa que não seja venenosa.'), tr('Relentless','Recupera o uso após descanso curto ou longo. Se dano de até 7 o reduziria a 0 PV, fica com 1 PV.',uso='Recharge after a Short or Long Rest')],
 'acoes':[act('Hooves','Ataque corpo a corpo +4, alcance 5 ft., uma criatura Prone; 2d4+2 bludgeoning.',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d4+2','tipo':'bludgeoning'}]), act('Tusk','Ataque corpo a corpo +4, alcance 5 ft., um alvo; 1d6+2 slashing.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d6+2','tipo':'slashing'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','defesas especiais','Multiattack','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/3421', 'citation':'turn78view1'
},
'TF-321': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Laboratory','Ruin','Tomb'],
 'porte':'Medium', 'tipo_fonte':'Construct', 'alinhamento':'', 'nd_fonte':'7', 'ca':14, 'ca_base':'natural armor', 'pv':102, 'formula_pv':'12d8 + 48; bloodied 51',
 'deslocamento':{'walk_ft':35,'climb_ft':35,'swim_ft':35}, 'scores':[15,17,18,6,14,5],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['necrotic','bludgeoning, piercing, slashing from magical weapons'], 'imunidades_dano':['cold','fire','force','thunder','bludgeoning, piercing, slashing from nonmagical weapons that aren’t adamantine'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','fatigue','frightened','paralyzed','petrified','prone','strife'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':12, 'idiomas':['understands creator’s languages; cannot speak'], 'bonus_proficiencia':3, 'maneuver_dc':14,
 'tracos':[tr('Berserk','Quando começa turno com 60 PV ou menos, rola d6; em 6 fica berserk. A cada turno berserk ataca a criatura visível mais próxima. Se não puder alcançar e atacar criatura, ataca objeto, preferindo um menor que ela. Permanece assim até ser destruído ou recuperar todos os PV; não pode ser acalmada.'), tr('Magic Resistance','Tem vantagem nas salvaguardas contra magias e outros efeitos mágicos.'), tr('Mastered Form','Passa por espaço de 1 polegada sem apertar e é imune a magia ou efeito que alteraria sua forma.')],
 'acoes':[act('Multiattack','Faz três ataques de Slam.'), act('Slam','Ataque corpo a corpo +6, alcance 5 ft., um alvo; 2d12+3 magical bludgeoning. Se o alvo for criatura viva, o guardião recupera metade do dano causado.',ataque='+6',alcance='5 ft.',dano=[{'dados':'2d12+3','tipo':'magical bludgeoning'}]), act('Blood Bullets','Ataque à distância +6, alcance 100 ft., até três alvos iniciais. Cada projétil causa 2d8+4 magical piercing e explode mesmo se errar; cada criatura a até 5 ft. do impacto faz salvaguarda de Destreza CD 15 ou sofre 2d6 necrotic.',ataque='+6',alcance='100 ft.',dano=[{'dados':'2d8+4','tipo':'magical piercing'},{'dados':'2d6 em falha na salvaguarda','tipo':'necrotic'}],salvaguarda='Dexterity DC 15')],
 'acoes_bonus':[act('Alter Arms','Muda o dano de Slam para piercing ou slashing.'), act('Bloodsight','Descobre direção e distância de criatura viva que já tenha ferido, se estiver a até 5 milhas.')], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','perícias','vulnerabilidades a dano','Multiattack além da sequência de 3 Slams','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/3397', 'citation':'turn78view2'
},
'TF-324': {
 'fonte_publicacao':"Dungeon Delver's Guide", 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Caverns','Ruin','Tomb'],
 'porte':'Medium', 'tipo_fonte':'Dragon', 'alinhamento':'', 'nd_fonte':'1/2', 'ca':12, 'ca_base':'natural armor', 'pv':27, 'formula_pv':'5d8 + 5; bloodied 13',
 'deslocamento':{'walk_ft':40}, 'scores':[14,12,12,8,10,8],
 'salvaguardas':{}, 'pericias':{'Perception':2}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':12, 'idiomas':['understands Draconic; cannot speak'], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[],
 'acoes':[act('Bite','Ataque corpo a corpo +4, alcance 5 ft., um alvo; 1d6+2 piercing e 1d6 poison.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d6+2','tipo':'piercing'},{'dados':'1d6','tipo':'poison'}]), act('Poison Breath','1/dia; cone de poison de 15 ft.; salvaguarda de Constituição CD 11, 2d6 poison em falha ou metade em sucesso.',uso='1/day',salvaguarda='Constitution DC 11')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'A seção de combate recomenda Poison Breath quando pode atingir pelo menos dois inimigos; depois usa Bite. Quando está só, foge ao ficar bloodied; se estiver sendo montado, obedece ao cavaleiro.',
 'secoes_nao_listadas':['salvaguardas','defesas especiais','Multiattack','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/2860', 'citation':'turn78view3'
},
'TF-380': {
 'fonte_publicacao':"Dungeon Delver's Guide", 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Plane of Earth','Underland'],
 'porte':'Large', 'tipo_fonte':'Monstrosity', 'alinhamento':'', 'nd_fonte':'4', 'ca':13, 'ca_base':'natural armor', 'pv':85, 'formula_pv':'9d10 + 36; bloodied 42',
 'deslocamento':{'walk_ft':0,'burrow_ft':40,'fly_ft':40,'fly_hover':True}, 'scores':[18,12,18,2,10,4],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['tremorsense 60 ft.'], 'percepcao_passiva':10, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':14,
 'tracos':[tr('Stone Glide','Pode atravessar pedra não mágica sem perturbar o material. Armas e projéteis de pedra atravessam o tubarão sem feri-lo.')],
 'acoes':[act('Bite','Ataque corpo a corpo +6, alcance 5 ft.; 2d10+4 piercing. Alvo Large ou menor fica Grappled (escape CD 14); enquanto o segura, o tubarão não pode morder outra criatura e o alvo recebe o traço Stone Glide. Se escapar enquanto estiver dentro da pedra, sofre 5d10 force e é deslocado ao espaço desocupado mais próximo fora da pedra.',ataque='+6',alcance='5 ft.',dano=[{'dados':'2d10+4','tipo':'piercing'},{'dados':'5d10 se escapar dentro de pedra','tipo':'force'}],salvaguarda='escape DC 14'), act('Tail','Ataque corpo a corpo +6, alcance 10 ft.; 2d6+4 bludgeoning.',ataque='+6',alcance='10 ft.',dano=[{'dados':'2d6+4','tipo':'bludgeoning'}])],
 'acoes_bonus':[], 'reacoes':[act('Tail Swat','Quando uma criatura que o tubarão vê o acerta com ataque corpo a corpo, ele ataca essa criatura com Tail.')], 'conjuracao':None,
 'nota_tatica':'Começa escondido em pedra, emerge voando para tentar agarrar com Bite e volta para a pedra se conseguir. Usa Tail Swat contra ataques de oportunidade; pode recuar após obter uma presa ou quando estiver bloodied se nenhum inimigo também estiver bloodied.',
 'secoes_nao_listadas':['salvaguardas','perícias','resistências e imunidades a dano','Multiattack','ações bônus','conjuração','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.a5e.tools/node/2896', 'citation':'turn80view0'
},
'TF-400': {
 'fonte_publicacao':'Mythological Figures & Maleficent Monsters', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Forest','Hills','Ruin','The Bleak Gate','Swamp','Tomb'], 'tags':['NPC','Unique'],
 'porte':'Medium', 'tipo_fonte':'Undead', 'alinhamento':'', 'nd_fonte':'6', 'ca':16, 'ca_base':'natural armor', 'pv':68, 'formula_pv':'8d8 + 32; bloodied 34',
 'deslocamento':{'walk_ft':30}, 'scores':[18,16,19,14,15,17],
 'salvaguardas':{}, 'pericias':{'Animal Handling':5,'Athletics':7,'Intimidation':6,'Perception':5,'Survival':5}, 'resistencias_dano':['acid','cold','fire','lightning','thunder','bludgeoning, piercing, slashing de ataques não mágicos que não sejam prateados'], 'imunidades_dano':['necrotic','poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','frightened','exhaustion','petrified','poisoned'],
 'sentidos':['blindsight 30 ft.','darkvision 120 ft.'], 'percepcao_passiva':15, 'idiomas':['os idiomas que conhecia em vida'], 'bonus_proficiencia':3, 'maneuver_dc':15,
 'tracos':[tr('Incorporeal Movement','Atravessa criaturas e objetos como terreno difícil; se terminar o turno dentro de um objeto, sofre 1d10 force. A seção permite compartilhar temporariamente este traço com criatura tocada.'), tr('Magic Resistance','Tem vantagem nas salvaguardas contra magias e outros efeitos mágicos.'), tr('Regeneration','Recupera 5 PV no início do turno; se sofreu dano radiante ou de água benta, a regeneração não funciona no início do próximo turno.')],
 'acoes':[act('Multiattack','Usa Frightful Presence e faz um ataque, ou faz dois ataques: um Chilling Blade e um Spinal Whip.'), act('Chilling Blade','Ataque corpo a corpo +7, alcance 5 ft.; 1d8+5 magical slashing e 1d8 cold.',ataque='+7',alcance='5 ft.',dano=[{'dados':'1d8+5','tipo':'magical slashing'},{'dados':'1d8','tipo':'cold'}]), act('Spinal Whip','Ataque corpo a corpo +7, alcance 10 ft.; 1d6+5 magical bludgeoning e 1d8 necrotic.',ataque='+7',alcance='10 ft.',dano=[{'dados':'1d6+5','tipo':'magical bludgeoning'},{'dados':'1d8','tipo':'necrotic'}]), act('Death’s Calling','Escolhe criatura visível até 60 ft.; salvaguarda de Carisma CD 14. Em falha, por 1 minuto não pode usar reações e no turno escolhe entre ação ou ação bônus. Pode gastar ação para repetir o teste, encerrando o efeito em sucesso. Até concluir descanso longo, ataques com armas contra ela são críticos com 19–20 e ela falha automaticamente em testes contra a morte.',salvaguarda='Charisma DC 14',duracao='1 minute; efeito crítico até descanso longo'), act('Frightful Presence','Criaturas escolhidas conscientes a até 100 ft. fazem salvaguarda de Sabedoria CD 14; falha causa Frightened por 1 minuto. Repetem ao fim dos turnos; sucesso encerra. Após sucesso ou fim do efeito, ficam imunes à presença por 24 horas.',salvaguarda='Wisdom DC 14',duracao='1 minute; imunidade 24 hours')],
 'acoes_bonus':[act('Compartilhar Incorporeal Movement','Como ação bônus, compartilha o traço Incorporeal Movement com criatura que toca até o início do próximo turno.')], 'reacoes':[],
 'conjuracao':{'atributo':'CHA','cd':14,'ataque_magia':None,'sem_componentes':['material'],'at_will':['detect magic','phantom steed'],'3/day':['gust of wind','misty step'],'1/day':['blight']},
 'equipamento_fonte':[tr('Spinal Whip (item associado, não ação adicional)','Entrada independente da fonte: chicote mágico muito raro, custo 7.000 gp; base 1d6 bludgeoning e +1d8 necrotic contra criatura viva. Em 20 natural contra alvo vivo, criaturas escolhidas em raio de 50 ft. fazem Sabedoria CD 18 ou ficam Frightened por 1 minuto; enquanto assim, afastam-se, não podem aproximar-se voluntariamente a 50 ft. nem usar reações, e sua ação fica restrita a Dash ou tentar escapar de impedimento de movimento (Dodge se não houver espaço). Repetem salvaguarda ao final de cada turno. Componente de criação indicado: cadáver de bone devil.')],
 'nota_tatica':'A ficha também descreve o Spinal Whip como item independente; sua regra foi registrada separadamente e não contada como nova ação do monstro.',
 'secoes_nao_listadas':['salvaguardas','vulnerabilidades a dano','ações especiais adicionais','reações','ações lendárias','ações míticas','ações de covil'],
 'url':'https://a5e.tools/node/2449', 'citation':'turn80view1'
},
'TF-450': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Laboratory','Ruin','Temple','Tomb'],
 'porte':'Large', 'tipo_fonte':'Construct', 'alinhamento':'', 'nd_fonte':'14', 'ca':20, 'ca_base':'natural armor', 'pv':210, 'formula_pv':'20d10 + 100; bloodied 105',
 'deslocamento':{'walk_ft':30}, 'scores':[24,12,20,3,12,1],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['fire','poison','psychic','dano de armas não mágicas que não sejam adamantinas'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','fatigue','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['darkvision 120 ft.'], 'percepcao_passiva':11, 'idiomas':['compreende idiomas do criador; não fala'], 'bonus_proficiencia':5, 'maneuver_dc':20,
 'tracos':[tr('Fire Absorption','Dano de fogo restaura PV em quantidade igual ao dano que seria sofrido.'), tr('Immutable Form','Imune a efeitos que alterariam sua forma.'), tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e efeitos mágicos.'), tr('Constructed Nature','Não precisa de ar, alimento ou sono.')],
 'acoes':[act('Multiattack','Faz dois ataques de Sword.'), act('Sword','Ataque corpo a corpo +12, alcance 10 ft.; 4d10+7 slashing.',ataque='+12',alcance='10 ft.',dano=[{'dados':'4d10+7','tipo':'slashing'}]), act('Poison Breath','Recarga 5–6; cone de 15 ft.; salvaguarda de Constituição CD 18, 10d8 poison em falha ou metade em sucesso.',uso='Recharge 5–6',salvaguarda='Constitution DC 18')],
 'acoes_bonus':[], 'reacoes':[act('Deflection','Quando um ataque à distância de criatura que vê erra o guardião, pode redirecioná-lo contra criatura que vê a até 60 ft.; o atacante original repete a jogada contra o novo alvo.')], 'conjuracao':None,
 'nota_tatica':'A estratégia depende da programação: ataca o inimigo mais próximo ou alvos determinados. Usa Poison Breath se atingir ao menos duas criaturas; usa Deflection contra alvo menos protegido ou um alvo preferido.',
 'secoes_nao_listadas':['salvaguardas','perícias','resistências e vulnerabilidades a dano','ações bônus','conjuração','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.a5e.tools/node/1671', 'citation':'turn80view2'
},
'TF-465': {
 'fonte_publicacao':'Gate Pass Gazette Issue #3 (Mount Jino)', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Desert','Forest','Grassland','Hills','Jungle','Mountains','Tundra'],
 'porte':'Large', 'tipo_fonte':'Monstrosity', 'alinhamento':'', 'nd_fonte':'2', 'ca':14, 'ca_base':'natural armor', 'pv':51, 'formula_pv':'6d10 + 18; bloodied 25',
 'deslocamento':{'walk_ft':30}, 'scores':[16,14,16,8,12,8],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':11, 'idiomas':['Common'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Pack Tactics','Tem vantagem em jogadas de ataque contra criatura se ao menos um aliado não incapacitado estiver a até 5 ft. dela.'), tr('Gliding 30 ft.','Ao planar, percorre horizontalmente até 1 ft. por cada 1 ft. de descida; cai se não se mover ao menos 5 ft. no turno.'), tr('Poison Stinger','Criatura ferida pela cauda faz salvaguarda de Constituição CD 13 ou fica Poisoned; repete no fim de cada turno, encerrando o efeito em sucesso.')],
 'acoes':[act('Multiattack','Faz um ataque de Bite e um de Claws.'), act('Bite','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 piercing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'piercing'}]), act('Claws','Ataque corpo a corpo +5, alcance 5 ft.; 2d4+3 slashing. Se avançar 20 ft. em linha reta até o alvo, ele faz salvaguarda de Força CD 13 ou cai Prone.',ataque='+5',alcance='5 ft.',dano=[{'dados':'2d4+3','tipo':'slashing'}],salvaguarda='Strength DC 13'), act('Tail','Ataque corpo a corpo +5, alcance 10 ft.; 1d8+3 piercing.',ataque='+5',alcance='10 ft.',dano=[{'dados':'1d8+3','tipo':'piercing'}])],
 'acoes_bonus':[], 'reacoes':[act('Tail Whip','Quando uma criatura que vê o atinge com ataque corpo a corpo, ataca o atacante com Tail.')], 'conjuracao':None,
 'secoes_nao_listadas':['salvaguardas','perícias','defesas e vulnerabilidades','ações bônus','conjuração','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.a5e.tools/node/2271', 'citation':'turn81view0'
},
'TF-467': {
 'fonte_publicacao':'Gate Pass Gazette Issue #4', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Desert','Forest','Grassland','Hills','Jungle','Ruin','Swamp'],
 'porte':'Tiny', 'tipo_fonte':'Monstrosity', 'alinhamento':'', 'nd_fonte':'1', 'ca':15, 'ca_base':'natural armor', 'pv':22, 'formula_pv':'5d6 + 5; bloodied 11',
 'deslocamento':{'walk_ft':30,'climb_ft':30,'fly_ft':30}, 'scores':[8,14,13,8,8,8],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['poison'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':9, 'idiomas':['telepathy 60 ft.'], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[tr('Spider Climb','Escala superfícies difíceis, inclusive tetos de cabeça para baixo, sem teste de atributo.')],
 'acoes':[act('Putrid Bite','Ataque corpo a corpo +4, alcance 5 ft.; 2d4+2 piercing. O alvo faz salvaguarda de Constituição CD 12: falha contrai Blood Maggot Infestation; sucesso sofre 1d4 poison em vez da infecção. Se este ataque reduzir o alvo a 0 PV, ele morre e se ergue como Gorger Zombie após 1 minuto.',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d4+2','tipo':'piercing'},{'dados':'1d4 no sucesso do teste','tipo':'poison'}],salvaguarda='Constitution DC 12'), act('Corrosive Bile Spit','Recarga 5–6; ataque à distância +4, alcance 15/30 ft.; 2d6+2 acid.',ataque='+4',alcance='15/30 ft.',dano=[{'dados':'2d6+2','tipo':'acid'}],uso='Recharge 5–6')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'efeitos_dependentes':[tr('Blood Maggot Infestation','Após infecção: ao fim de cada descanso longo, sofre 1d4+2 piercing e faz salvaguarda de Constituição CD 11 ou ganha 1 nível de Fatigue que não pode ser removido por descanso longo enquanto houver maggot. A CD aumenta em 1 por maggot adicional. Três sucessos consecutivos matam e expulsam o maggot. Lesser restoration remove a infestação; também pode ser removida cirurgicamente com teste de Medicine CD 13, causando 1d4+2 dano por tentativa, e cada maggot requer um teste. Se o hospedeiro morrer infectado, retorna como Gorger Zombie após 1 minuto.',fonte_url='https://a5e.tools/rules/blood-maggot-infestation')],
 'fontes_adicionais':[{'titulo':'Blood Maggot Infestation — Gate Pass Gazette','url':'https://a5e.tools/rules/blood-maggot-infestation','citation':'turn87view1'}],
 'secoes_nao_listadas':['salvaguardas','perícias','defesas especiais','Multiattack','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/2513', 'citation':'turn86view0'
},
'TF-471': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Forest','Settlement'],
 'porte':'Large', 'tipo_fonte':'Monstrosity', 'alinhamento':'', 'nd_fonte':'3', 'ca':16, 'ca_base':'natural armor', 'pv':59, 'formula_pv':'7d10 + 21; bloodied 29',
 'deslocamento':{'walk_ft':50}, 'scores':[18,15,17,2,15,8],
 'salvaguardas':{}, 'pericias':{'Perception':4,'Stealth':4}, 'pericias_bonus_dado':{'Stealth':'1d4'}, 'resistencias_dano':['cold','fire','radiant'], 'imunidades_dano':['necrotic','poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['frightened','poisoned'],
 'sentidos':['darkvision 120 ft.'], 'percepcao_passiva':14, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':14,
 'tracos':[tr('Charge','Se avançar ao menos 20 ft. em linha reta e acertar Tusk no mesmo turno, causa 1d8 slashing extra; alvo criatura faz salvaguarda de Força CD 14 ou cai Prone.'), tr('Evil','Emite uma aura maligna.'), tr('Keen Smell','Tem vantagem em testes de Perception que dependam de olfato.'), tr('Magic Resistance','Tem vantagem nas salvaguardas contra magias e outros efeitos mágicos.'), tr('Relentless (1/Short Rest)','Se dano de até 20 o reduziria a 0 PV, fica com 1 PV.',uso='1/Short Rest')],
 'acoes':[act('Tusk','Ataque corpo a corpo +6, alcance 5 ft.; 2d8+4 piercing.',ataque='+6',alcance='5 ft.',dano=[{'dados':'2d8+4','tipo':'piercing'}])],
 'acoes_bonus':[], 'reacoes':[act('Infernal Mark (1/Short Rest)','Quando causa dano a criatura não maligna, pode marcá-la. Até morrer ou passar 24 horas, todos os ataques do javali contra ela causam +1d8 necrotic.',uso='1/Short Rest',duracao='até o alvo morrer ou 24 horas')], 'conjuracao':None,
 'completa':True,
 'observacao_resolucao':'A extração textual da página mostra “Speed 5 0 ft.” com espaçamento, enquanto o resultado indexado do próprio site oficial apresenta “Speed 50 ft.”; deslocamento de caminhada 50 ft. adotado com base na confirmação primária indexada.',
 'secoes_nao_listadas':['salvaguardas','vulnerabilidades a dano','Multiattack','ações bônus','conjuração','ações lendárias','ações míticas','ações de covil'],
 'url':'https://www.a5e.tools/node/3327', 'citation':'turn7view0; turn6search2'
},
'TF-478': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Forest','Grassland','Hills','Jungle','Mountains','Ruin','Swamp'], 'tags':['Legendary','NPC','Unique'],
 'porte':'Medium', 'tipo_fonte':'Plant', 'alinhamento':'', 'nd_fonte':'3', 'ca':14, 'ca_base':'natural armor', 'pv':60, 'formula_pv':'8d8 + 24; bloodied 30 (metade dos PV, derivado da regra A5E)',
 'deslocamento':{'walk_ft':40,'burrow_ft':20,'climb_ft':30}, 'scores':[17,9,16,7,10,8],
 'salvaguardas':{'STR':5,'DEX':1,'CON':5}, 'pericias':{'Athletics':5,'Perception':2}, 'pericias_bonus_dado':{'Perception':'1d8'}, 'resistencias_dano':['necrotic','poison','psychic'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 120 ft.'], 'percepcao_passiva':16, 'idiomas':['Squash'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Natural Artistry','Em teste de atributo, recebe um Expertise Die por cada gourdling cooperando na mesma tarefa, até 1d12.')],
 'acoes':[act('Multiattack','Faz dois ataques.'), act('Slam','Ataque corpo a corpo +5, alcance 5 ft.; 1d10+3 bludgeoning.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d10+3','tipo':'bludgeoning'}]), act('Vines','Ataque corpo a corpo +5, alcance 10 ft.; 1d6+3 bludgeoning. Alvo Medium ou menor fica Grappled (escape CD 13).',ataque='+5',alcance='10 ft.',dano=[{'dados':'1d6+3','tipo':'bludgeoning'}],salvaguarda='escape DC 13')],
 'acoes_bonus':[act('Dread Rend','Quando acerta criatura que está agarrando com Slam, causa 1d6 necrotic + 1d6 psychic; alvo faz salvaguarda de Carisma CD 13 ou fica Rattled até o fim do próximo turno.')],
 'reacoes':[act('Root Down (1/day)','Quando seria reduzido a 0 PV, se estiver tocando terra/solo, fica com 10 PV (4d4) em vez disso. Nenhuma planta comum cresce naquela área por 1d10 anos.',uso='1/day')], 'conjuracao':None,
 'efeitos_dependentes':[tr('Rattled','Até o fim do próximo turno, não pode beneficiar-se de Expertise Dice nem usar reações. Criatura imune a Stunned também é imune a Rattled.',fonte_url='https://a5e.tools/rules/conditions')],
 'fontes_adicionais':[{'titulo':'Conditions (Bloodied e Rattled) — Level Up','url':'https://a5e.tools/rules/conditions','citation':'turn87view2'}],
 'nota_tatica':'O valor de bloodied não é impresso numericamente na ficha; 30 foi derivado da definição A5E de bloodied como metade dos PV ou menos. A página também classifica o monstro com tag Legendary, mas não publica bloco de ações lendárias.',
 'secoes_nao_listadas':['defesas especiais','Multiattack além da contagem de ataques','ações especiais adicionais','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/3665', 'citation':'turn86view2'
},
'TF-482': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Underland'],
 'porte':'Medium', 'tipo_fonte':'Plant', 'alinhamento':'', 'nd_fonte':'1/4', 'ca':8, 'ca_base':'', 'pv':15, 'formula_pv':'2d8 + 6; bloodied 7',
 'deslocamento':{'walk_ft':20}, 'scores':[12,6,16,3,6,4],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':8, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':11,
 'tracos':[tr('Sporous Resilience (2/day)','Se dano não necrótico nem crítico o reduziria a 0 PV, fica com 1 PV, cai Prone e fica Stunned até o fim do próximo turno, parecendo morto. Um teste de Medicine CD 11 detecta a farsa.',uso='2/day'), tr('Undead Nature','Não precisa respirar, alimentar-se ou dormir. A redação da página usa “zombie” dentro deste traço embora o tipo da criatura seja Plant; não foi acrescentada outra regra.')],
 'acoes':[act('Grab','Ataque corpo a corpo +3, alcance 5 ft.; 1d6+1 bludgeoning. Alvo Medium ou menor fica Grappled (escape CD 11); enquanto o segura, não pode agarrar outro alvo.',ataque='+3',alcance='5 ft.',dano=[{'dados':'1d6+1','tipo':'bludgeoning'}],salvaguarda='escape DC 11'), act('Spore Bite','Ataque corpo a corpo +3, alcance 5 ft., contra alvo agarrado; 1d10+1 piercing e salvaguarda de Constituição CD 11; falha infecta com Eltare’s Malaise.',ataque='+3',alcance='5 ft.',dano=[{'dados':'1d10+1','tipo':'piercing'}],salvaguarda='Constitution DC 11')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'efeitos_dependentes':[tr('Eltare’s Malaise','Pode ser contraída por esporos inalados ou mordida do spore thrall. Dura 1d10 menos o modificador de Constituição em dias (mínimo 1). Enquanto afligido, tem desvantagem na iniciativa e, se adormecer, permanece Unconscious até sofrer dano ou outra criatura usar ação para despertá-lo. Ao fim de cada descanso longo, perde 1d4 Inteligência (a página informa valor médio 2); Int 0 causa morte. Humanoide que morre pelo efeito vira spore thrall em 1d4 horas; beast, dragon, giant ou monstrosity que morre pelo efeito recebe o template Spore Thrall. Gentle repose previne a reanimação. Após a doença passar, recupera 1d4 Int ao fim de cada descanso longo; Lesser Restoration cura e recupera 1d4 Int, com déficit restante recuperado normalmente, e Greater Restoration encerra e restaura todo o Int perdido.',fonte_url='https://a5e.tools/rules/eltares-malaise')],
 'fontes_adicionais':[{'titulo':'Eltare’s Malaise — Gate Pass Gazette Issue #15','url':'https://a5e.tools/rules/eltares-malaise','citation':'turn87view0'}],
 'nota_tatica':'A seção narrativa diz que em florestas estes thralls são controlados pela mente de Davek’dran; em outros locais, trabalham para melhorar a situação do eltare que os criou.',
 'secoes_nao_listadas':['salvaguardas','perícias','defesas especiais','Multiattack','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/3209', 'citation':'turn86view3'
},
'TF-483': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Forest','Grassland','Hills','Jungle','Mountains','Ruin','Swamp'],
 'porte':'Tiny', 'tipo_fonte':'Plant', 'alinhamento':'', 'nd_fonte':'1', 'ca':13, 'ca_base':'natural armor', 'pv':36, 'formula_pv':'8d4 + 16; bloodied 16 (como impresso; discrepância com regra de metade dos PV)',
 'deslocamento':{'walk_ft':25,'burrow_ft':15,'climb_ft':20}, 'scores':[8,9,15,12,14,13],
 'salvaguardas':{'INT':3}, 'pericias':{'Athletics':1,'Nature':3,'Performance':2,'Persuasion':3,'Religion':3,'Survival':4}, 'pericias_bonus_dado':{'Nature':'1d4','Performance':'1d8','Persuasion':'1d6'}, 'resistencias_dano':['necrotic','poison','psychic'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 120 ft.'], 'percepcao_passiva':12, 'idiomas':['Common','Squash'], 'bonus_proficiencia':2, 'maneuver_dc':9,
 'tracos':[],
 'acoes':[act('Slam','Ataque corpo a corpo +1, alcance 5 ft.; 1 (1d4−1) bludgeoning; a página repete o valor fixo 1 depois da fórmula.',ataque='+1',alcance='5 ft.',dano=[{'dados':'1d4−1','tipo':'bludgeoning'}]), act('Seed Shot','Recarga 3–6; ataque mágico à distância +4, alcance 50/200 ft.; 2d4 necrotic e 2d4 psychic. Criatura que sofre 12 ou mais de dano fica Rattled até o fim do próximo turno.',ataque='+4',alcance='50/200 ft.',dano=[{'dados':'2d4','tipo':'necrotic'},{'dados':'2d4','tipo':'psychic'}],uso='Recharge 3–6')],
 'acoes_bonus':[act('Charming Aspect (2/day)','Criatura visível a até 30 ft. faz salvaguarda de Sabedoria CD 12; falha deixa-a Charmed por 1 hora. Repete o teste ao fim de cada minuto e sempre que sofre dano, encerrando em sucesso.',uso='2/day',salvaguarda='Wisdom DC 12',duracao='1 hour')],
 'reacoes':[act('Fell Sustenance','Quando recebe dano necrotic ou psychic, recarrega o uso de Seed Shot.')], 'conjuracao':None,
 'efeitos_dependentes':[tr('Rattled','Até o fim do próximo turno, não pode beneficiar-se de Expertise Dice nem usar reações. Criatura imune a Stunned também é imune a Rattled.',fonte_url='https://a5e.tools/rules/conditions')],
 'fontes_adicionais':[{'titulo':'Conditions (Bloodied e Rattled) — Level Up','url':'https://a5e.tools/rules/conditions','citation':'turn87view2'}],
 'completa':False, 'nota_fonte':"Registro parcial: a fonte imprime PV 36 com bloodied 16 (a regra A5E de metade dos PV indica limiar 18), e a linha de salvaguardas mostra 'Int +3, Chat +2'. Também repete '1' após a fórmula de dano do Slam. Os valores ambíguos foram preservados como observação; não houve correção presumida.",
 'nota_tatica':'A página é a fonte da habilidade e dos campos transcritos; discrepâncias de limiar bloodied, nome do atributo da salvaguarda e repetição de dano impedem confirmar o bloco como completo.',
 'secoes_nao_listadas':['salvaguarda associada a “Chat +2” não confirmada','defesas especiais','Multiattack','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/3666', 'citation':'turn91view1'
},
'TF-493': {
 'fonte_publicacao':'Gate Pass Gazette Issue #3 (Mount Jino)', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Caverns','The Dreaming','Forest','Grassland','Hills','Jungle','Mountains','Ruin','Swamp'],
 'porte':'Large', 'tipo_fonte':'Giant', 'alinhamento':'', 'nd_fonte':'6', 'ca':18, 'ca_base':'natural armor', 'pv':84, 'formula_pv':'8d10 + 40; bloodied 42',
 'deslocamento':{'walk_ft':40}, 'scores':[18,12,20,8,12,8],
 'salvaguardas':{}, 'pericias':{'Stealth':4}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':11, 'idiomas':['Giant'], 'bonus_proficiencia':3, 'maneuver_dc':15,
 'tracos':[tr('False Appearance','Quando imóvel, é indistinguível de um rochedo comum.'), tr('Regeneration','Recupera 10 PV no início do turno. Se sofreu dano thunder ou cold, não regenera no turno seguinte. Só morre se começar turno com 0 PV e não regenerar.'), tr('Severed Limbs','Crítico causado por arma slashing pode decepar extremidade. A extremidade tem CA 15, 10 PV, deslocamento 10 ft. e regeneração do troll; ele a controla e percebe pelos sentidos apropriados. Enquanto falta uma extremidade, PV máximos caem 10. Role d6: 1–4 braço, que substitui um ataque Claw; 5–6 cabeça, que substitui Bite. A extremidade separada pode fazer o ataque correspondente.')],
 'acoes':[act('Multiattack','Faz um ataque de Bite e dois de Claw.'), act('Bite','Ataque corpo a corpo +7, alcance 5 ft.; 2d6+4 piercing.',ataque='+7',alcance='5 ft.',dano=[{'dados':'2d6+4','tipo':'piercing'}]), act('Claw','Ataque corpo a corpo +7, alcance 10 ft.; 2d4+4 slashing.',ataque='+7',alcance='10 ft.',dano=[{'dados':'2d4+4','tipo':'slashing'}]), act('Ambushing Shove','Pode escolher criatura Large ou menor ao alcance se ela ainda não agiu no combate, está a 5 ft. de outro inimigo, ou o troll tem vantagem contra ela. Salvaguarda de Força CD 14; falha empurra até 30 ft. horizontalmente e derruba. Se colidir com objeto, sofre 3d6 bludgeoning; se colidir com outra criatura, ela faz Destreza CD 14 ou ambas sofrem esse dano e caem Prone.',salvaguarda='Strength DC 14; Dexterity DC 14')],
 'acoes_bonus':[act('Reattach Extremity','Como ação bônus, reanexa uma extremidade decepada.')], 'reacoes':[], 'conjuracao':None,
 'completa':False, 'nota_fonte':'A página contém instruções de combate que dizem que o troll ignora todo dano exceto fire/acid e recua após dano acid/fire, enquanto o traço Regeneration indica que cold ou thunder impede a cura no turno seguinte. A incompatibilidade entre os dois trechos não foi reconciliada.',
 'nota_tatica':'A orientação de combate descreve emboscada, preferência pelo oponente mais próximo ou lento e retirada apenas quando bloodied, após receber acid/fire, e sem inimigos derrotados; isso entra em conflito com a regra de Regeneration escrita na mesma página.',
 'secoes_nao_listadas':['salvaguardas','resistências e imunidades a dano','ações de covil','ações lendárias','ações míticas','conjuração'],
 'url':'https://www.a5e.tools/node/2270', 'citation':'turn90view1'
},
'TF-494': {
 'fonte_publicacao':'Gate Pass Gazette Issue #1 (The Fellspire)', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Forest','The Bleak Gate','Swamp'],
 'porte':'Tiny', 'tipo_fonte':'Fey', 'alinhamento':'', 'nd_fonte':'1/4', 'ca':15, 'ca_base':'', 'pv':2, 'formula_pv':'1d4; bloodied 1',
 'deslocamento':{'walk_ft':20}, 'scores':[2,20,10,10,12,14],
 'salvaguardas':{}, 'pericias':{'Perception':3,'Stealth':7}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':13, 'idiomas':['Sylvan'], 'bonus_proficiencia':2, 'maneuver_dc':15,
 'tracos':[tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e efeitos mágicos.')],
 'acoes':[act('Thorn Dagger','Ataque corpo a corpo +7, alcance 5 ft., ou à distância +7, alcance 10/30 ft.; 1 piercing.',ataque='+7',alcance='5 ft. ou 10/30 ft.',dano=[{'dados':'1','tipo':'piercing'}]), act('Oath Keeper (3/day)','Escolhe até quatro criaturas voluntárias a até 30 ft. que acabaram de fazer um juramento. Durante 1 ano, na primeira vez por dia em que cada uma age contra seu juramento, sofre 7d10 psychic. A criatura sempre sabe o texto exato e quem está afetado; pode encerrar o efeito em uma criatura usando ação. Remove curse, greater restoration ou wish com espaço de 7º nível ou superior também encerra.',uso='3/day',duracao='1 year'), act('Faerie Curse','Escolhe criatura a até 30 ft. que não esteja sob esta maldição; salvaguarda de Sabedoria CD 12. Em falha, por 1 hora escolhe um efeito: Blinded; Charmed pelo guardião; se já estiver Charmed por ele, adormece; ou cabeça adquire aparência animal e só pode emitir sons, sem alteração de estatísticas. A maldição termina se o guardião morrer ou ficar Incapacitated, se ele ou aliado causar dano ao alvo, se usar ação para encerrá-la, ou por remove curse, dispel magic ou lesser restoration. Alvo bem-sucedido ou cujo efeito termina fica imune a Faerie Curse por 24 horas. O adormecido desperta se receber dano ou se outra criatura usar ação para sacudi-lo.',salvaguarda='Wisdom DC 12',duracao='1 hour; imunidade 24 hours')],
 'acoes_bonus':[act('Shadow Shroud','Como ação bônus, reduz a luz num raio de 30 ft.: bright light vira dim light e dim light vira darkness. Não afeta fontes de luz mágica.'), act('Invisibility','Fica invisível junto com equipamento carregado até atacar, conjurar magia, ficar Incapacitated ou usar ação bônus para tornar-se visível.')], 'reacoes':[], 'conjuracao':None,
 'completa':False, 'nota_fonte':'A ficha registra apenas deslocamento walk 20 ft., mas a seção de combate diz que o askwise keeper fica invisível e voa para outra posição; não há valor de deslocamento fly no bloco. Nenhuma velocidade de voo foi inferida.',
 'nota_tatica':'Prefere Faerie Curse, depois invisibilidade e deslocamento aéreo. Também tende a fugir em grupo quando um keeper morre. A ausência de velocidade fly explícita impede fechar a ficha para simulação.',
 'secoes_nao_listadas':['salvaguardas','defesas especiais','reações','ações lendárias','ações míticas','ações de covil','velocidade de voo mencionada na tática mas ausente do bloco'],
 'url':'https://www.a5e.tools/node/2206', 'citation':'turn90view2'
},
'TF-495': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up: Advanced 5th Edition (página da ferramenta A5E; não é o A5ESRD; sem conversão para D&D 5e).', 'terreno_fonte':['Caverns','Forest','Underland'],
 'porte':'Medium', 'tipo_fonte':'Fey', 'alinhamento':'', 'nd_fonte':'1/2', 'ca':15, 'ca_base':'natural armor', 'pv':22, 'formula_pv':'5d8; bloodied 11',
 'deslocamento':{'walk_ft':30}, 'scores':[14,12,10,12,16,18],
 'salvaguardas':{}, 'pericias':{'Nature':3,'Perception':5,'Stealth':3,'Survival':5}, 'pericias_bonus_dado':{'Nature':'1d4','Stealth':'1d4'}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':['radiant'], 'imunidades_condicao':['diseased','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Undercommon','Sylvan'], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e efeitos mágicos.'), tr('Speak with Nature','Comunica-se com bestas e plantas.'), tr('Fungal Pathway','Uma vez por turno, gasta 10 ft. de movimento para entrar em anel de cogumelos e teleportar-se até 30 ft. de distância.'), tr('Web Walker','Ignora restrições de movimento causadas por teias.')],
 'acoes':[act('Club','Ataque corpo a corpo +4, alcance 5 ft.; 1d8+2 bludgeoning.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d8+2','tipo':'bludgeoning'}]), act('Sling','Ataque à distância +3, alcance 30/120 ft.; 1d4+1 bludgeoning.',ataque='+3',alcance='30/120 ft.',dano=[{'dados':'1d4+1','tipo':'bludgeoning'}]), act('Dragon’s Head Mushroom (3/day)','Arremessa cogumelo a local visível a até 30 ft.; libera esporos numa área de raio 10 ft. Cada criatura exceto Mykand faz salvaguarda de Sabedoria CD 13; falha causa Frightened e deve usar o movimento de cada turno para sair da visão de cogumelos deste tipo. Pode repetir o teste se Mykand ou aliado causar dano, encerrando o efeito em sucesso; sem isso dura 24 horas. Sucesso ou fim do efeito concede imunidade a esta habilidade por 24 horas.',uso='3/day',salvaguarda='Wisdom DC 13',duracao='24 hours; imunidade 24 hours')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'efeitos_dependentes':[tr('Frightened','Enquanto consegue ver a origem do medo, tem desvantagem em testes de atributo e jogadas de ataque; não pode aproximar-se voluntariamente da origem. A habilidade Dragon’s Head Mushroom ainda impõe sair da visão dos cogumelos.',fonte_url='https://a5e.tools/rules/conditions')],
 'fontes_adicionais':[{'titulo':'Conditions — Level Up','url':'https://a5e.tools/rules/conditions','citation':'turn87view2'}],
 'nota_tatica':'Tenta afastar os oponentes dos cogumelos que guarda e atraí-los para montes de tesouro que entende serem atraentes para outras criaturas.',
 'secoes_nao_listadas':['salvaguardas','defesas especiais','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/2990', 'citation':'turn91view0'
},
'TF-496': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'fey', 'alinhamento':'', 'nd_fonte':'2', 'ca':13, 'ca_base':'', 'pv':52, 'formula_pv':'8d8 + 16; bloodied 26',
 'deslocamento':{'walk_ft':30,'fly_ft':60}, 'terreno_fonte':['Forest','The Dreaming','Underland'], 'scores':[10,16,14,14,16,20],
 'salvaguardas':{}, 'pericias':{'Deception':7,'Perception':5,'Persuasion':7,'Stealth':5}, 'pericias_bonus_dado':{'Deception':'1d4','Persuasion':'1d4'},
 'resistencias_dano':['cold','fire','lightning','poison','damage from nonmagical weapons'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':15, 'idiomas':['Abyssal','Common','Sylvan','telepathy 60 ft.'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Remorse','Sempre que mata uma criatura viva, faz salvaguarda de Sabedoria CD 13; em falha, sofre remorso por 1d6 rodadas e tem desvantagem em testes de atributo e jogadas de ataque.',salvaguarda='Wisdom DC 13'), tr('Telepathic Bond','Pode comunicar-se telepaticamente a qualquer distância com criatura que esteja Charmed, mesmo em outro plano.')],
 'acoes':[act('Claw','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 slashing e 2d6 psychic.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'slashing'},{'dados':'2d6','tipo':'psychic'}]), act('Draining Touch (Recharge 5–6)','Ataque mágico corpo a corpo +7, alcance 5 ft.; 4d10 psychic. Reduz o máximo de PV do alvo pelo dano causado até ele terminar descanso longo e o Tyskri recupera PV iguais ao dano. Além disso, o alvo faz salvaguarda de Carisma CD 15; em falha, ganha um nível de Strife.',uso='Recharge 5–6',ataque='+7',alcance='5 ft.',dano=[{'dados':'4d10','tipo':'psychic'}],salvaguarda='Charisma DC 15'), act('Charm','Um humanoide no mesmo plano a até 30 ft. faz salvaguarda de Sabedoria CD 15; falha: fica Charmed magicamente por 1 hora ou até o Tyskri encantar outra criatura e obedece comandos. Repete o teste quando sofre dano ou recebe comando suicida. Sucesso ou encerramento concede imunidade à habilidade Charm de qualquer Tyskri por 24 horas.',salvaguarda='Wisdom DC 15',duracao='1 hour; imunidade 24 hours'), act('Etherealness','Viaja magicamente ao Ethereal Plane; de lá vê e ouve o Material Plane e pode se tornar audível e vagamente visível. Se um humanoide no Material Plane o convidar, o Tyskri pode usar uma ação para voltar ao Material Plane.')],
 'acoes_bonus':[act('Shapeshift','Muda entre forma verdadeira e forma humanoide Medium ou Small. Só pode voar na forma verdadeira. Na forma alterada, suas estatísticas permanecem iguais, exceto tamanho e deslocamento; equipamento não se transforma e a morte encerra a mudança.')],
 'reacoes':[act('Living Sacrifice','Quando uma criatura visível acerta o Tyskri, ele pode ordenar que uma criatura Charmed visível use a reação disponível para mover-se até seu deslocamento. Se após o movimento puder trocar de lugar com o Tyskri, o ataque acerta a criatura Charmed.')],
 'efeitos_dependentes':[tr('Strife','Rastreamento A5E: nível 1 dá desvantagem em testes de INT, WIS e CHA; nível 2, em testes de concentração; nível 3 impede usar ação e ação bônus no mesmo turno; nível 4 dá desvantagem em ataques e salvaguardas que usem INT, WIS ou CHA; nível 5 aplica efeito de estresse mental de curto prazo; nível 6 impede conjurar magias, exceto truques; nível 7 produz efeito permanente definido pelo Narrador ou aleatório. Um descanso longo em local seguro com Supply reduz um nível; para o primeiro nível basta descanso longo.',fonte_url='https://a5e.tools/rules/conditions')],
 'fontes_adicionais':[{'titulo':'Conditions — Strife','url':'https://a5e.tools/rules/conditions','citation':'turn104view0'}],
 'secoes_nao_listadas':['salvaguardas','imunidades e vulnerabilidades além das resistências listadas','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/3301', 'citation':'turn96view0'
},
'TF-498': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'fey', 'alinhamento':'', 'nd_fonte':'12', 'ca':16, 'ca_base':'mithral scale', 'pv':330, 'formula_pv':'44d8 + 132; bloodied 165',
 'deslocamento':{'walk_ft':35,'fly_ft':60}, 'terreno_fonte':['Forest','Swamp','The Dreaming'], 'tags':['Elite'], 'scores':[16,20,16,16,20,20],
 'salvaguardas':{'DEX':9,'WIS':9,'CHA':9}, 'pericias':{'Arcana':7,'History':7,'Insight':9,'Nature':7,'Perception':9,'Persuasion':9},
 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','paralyzed','poisoned','unconscious'],
 'sentidos':['truesight 60 ft.'], 'percepcao_passiva':19, 'idiomas':['Common','Elvish','Sylvan','two more'], 'bonus_proficiencia':4, 'maneuver_dc':15,
 'tracos':[tr('Faerie Form','Como ação, muda magicamente de tamanho entre Large, Medium e Tiny. Tiny: dano de ataques bludgeoning, piercing e slashing é reduzido à metade, tem desvantagem em testes de Força e vantagem em testes de Destreza. Large: vantagem em testes de Força. As demais estatísticas não mudam.'), tr('Faerie Light','Como ação bônus, emite dim light em 30 ft. ou extingue o brilho.'), tr('Innate Spellcasting','Atributo Carisma, CD 17; não requer componentes materiais. À vontade: animal messenger, detect evil and good, detect magic, disguise self. 3/dia cada: charm person, scrying, zone of truth. 1/dia cada: dream, geas, heroes’ feast, magic circle, polymorph (somente self).',cd=17), tr('Magic Resistance','Vantagem em salvaguardas contra magias e efeitos mágicos.'), tr('Elite Recovery','Ao fim de cada turno próprio, encerra uma condição ou efeito sobre si, inclusive se estiver unconscious ou incapacitated.'), tr('Expanded Spell List','Pode conjurar wish sem componentes materiais três vezes por ano e weird uma vez por dia.'), tr('Fey Madness','Enquanto Bloodied, pode usar uma reação em cada turno de criatura e Faerie Step recarrega em cada turno próprio.'), tr('Mass Darkvision','Ela e criaturas escolhidas a até 120 ft. recebem darkvision de 120 ft.')],
 'acoes':[act('Multiattack','Faz dois ataques de Glittering Scimitar.'), act('Glittering Scimitar','Ataque corpo a corpo +9, alcance 5 ft.; 1d6+5 slashing e 3d6 de dano cold, fire, lightning ou psychic à escolha.',ataque='+9',alcance='5 ft.',dano=[{'dados':'1d6+5','tipo':'slashing'},{'dados':'3d6','tipo':'cold, fire, lightning ou psychic (escolha)'}]), act('Gleaming Longbow','Ataque à distância +9, alcance 150/600 ft.; ignora meia cobertura e cobertura de três quartos; 1d8+5 piercing e 4d6 de dano cold, fire, lightning ou psychic à escolha.',ataque='+9',alcance='150/600 ft.',dano=[{'dados':'1d8+5','tipo':'piercing'},{'dados':'4d6','tipo':'cold, fire, lightning ou psychic (escolha)'}]), act('Evil Eye (Gaze)','Escolhe uma criatura a até 60 ft. que não esteja sob efeito de Evil Eye de uma faerie; salvaguarda de Sabedoria CD 17. Em falha, a archfey escolhe um efeito por 1 minuto: adormecida (encerra ao sofrer dano ou se alguém usar ação para despertá-la); Frightened (encerra quando estiver a pelo menos 60 ft. da archfey); ou Poisoned (repete a salvaguarda ao fim de cada turno, encerrando em sucesso).',salvaguarda='Wisdom DC 17',duracao='1 minute'), act('Summon Midnight (1/day)','A noite cai magicamente sobre uma área de 5 milhas de diâmetro por 1 hora. A archfey pode encerrar o efeito usando uma ação.',uso='1/day',duracao='1 hour'), act('Weird (9th-level; V, S; concentration)','Afeta criaturas num raio de 30 ft. de um ponto a até 120 ft.; cada alvo faz salvaguarda de Sabedoria CD 17. Em falha fica Frightened por 1 minuto. Ao fim de cada turno afetado, sofre 4d10 psychic e repete o teste, encerrando o efeito em sucesso.',salvaguarda='Wisdom DC 17',duracao='1 minute; concentration')],
 'acoes_bonus':[act('Faerie Step (Recharge 5–6)','Teleporta magicamente até 60 ft. para um espaço que possa ver.',uso='Recharge 5–6')],
 'reacoes':[act('Riposte','Quando é atingida por ataque corpo a corpo feito por criatura que possa ver, faz um ataque Glittering Scimitar contra o atacante.'), act('Vengeful Eye','Quando é atingida por ataque à distância ou alvo de magia de criatura a até 60 ft., usa Evil Eye contra o atacante se puderem ver um ao outro.')],
 'conjuracao':{'atributo':'CHA','cd':17,'sem_componentes':['material'],'at_will':['animal messenger','detect evil and good','detect magic','disguise self'],'3/day each':['charm person','scrying','zone of truth'],'1/day each':['dream','geas','heroes’ feast','magic circle','polymorph (self only)'],'detalhes_adicionais':'wish sem componentes materiais 3 vezes por ano; weird uma vez por dia, 9º nível, V, S e concentração'},
 'secoes_nao_listadas':['resistências, imunidades e vulnerabilidades a dano','ações míticas','ações de covil'],
 'nota_tatica':'A página recomenda combate corpo a corpo, Vengeful Eye contra atacantes à distância, Faerie Step para afastar-se de ameaças fortes e fuga com 55 PV ou menos; ao desaparecer, usa disguise self.',
 'url':'https://www.a5e.tools/node/1606', 'citation':'turn93view0'
},
'TF-502': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Tiny', 'tipo_fonte':'undead', 'alinhamento':'', 'nd_fonte':'2', 'ca':13, 'ca_base':'natural armor', 'pv':31, 'formula_pv':'7d4 + 14; bloodied 15',
 'deslocamento':{'walk_ft':10,'fly_ft':30}, 'terreno_fonte':['The Bleak Gate','The Dreaming'], 'scores':[2,16,14,6,14,10],
 'salvaguardas':{'CON':4,'WIS':4}, 'pericias':{'Stealth':4}, 'resistencias_dano':['necrotic'], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','exhaustion','poisoned'],
 'sentidos':['darkvision 30 ft.'], 'percepcao_passiva':10, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Despair Aura','Uma criatura que não seja undead e use uma ação ou ação bônus a até 10 ft. de um ghasthopper não pode usar outra ação, ação bônus ou reação até o início do próximo turno. A fonte menciona que um teste de resistência concede imunidade à aura de qualquer ghasthopper por 24 horas, mas não informa o gatilho, atributo ou CD do teste.'), tr('Incorporeal Movement','Move através de criaturas e objetos como se fossem terreno difícil; sofre 1d10 force se terminar o turno dentro de objeto.'), tr('Smoky Signals','Fica Invisible, exceto enquanto voa, ataca ou se alimenta de um hospedeiro; nessas situações parece uma mecha de fumaça em forma de inseto.')],
 'acoes':[act('Bleak Vibrations','Ataque corpo a corpo +5, alcance 5 ft.; 1d4+2 thunder e 1d6 psychic.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d4+2','tipo':'thunder'},{'dados':'1d6','tipo':'psychic'}]), act('Drain Health','Ataque corpo a corpo +5, alcance 5 ft.; 3d4 necrotic; recebe pontos de vida temporários iguais ao dano causado.',ataque='+5',alcance='5 ft.',dano=[{'dados':'3d4','tipo':'necrotic'}])],
 'secoes_nao_listadas':['ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'completa':False, 'nota_fonte':'A descrição de combate menciona um ataque Hungry Strike, ausente na seção ACTIONS. Despair Aura refere-se a um saving throw, mas a página não fornece seu gatilho, atributo ou CD. As ações não foram inferidas.',
 'url':'https://www.a5e.tools/node/4001', 'citation':'turn95view0'
},
'TF-508': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Medium', 'tipo_fonte':'undead', 'alinhamento':'', 'nd_fonte':'1/4', 'ca':8, 'ca_base':'', 'pv':15, 'formula_pv':'2d8 + 6; bloodied 7',
 'deslocamento':{'walk_ft':20,'swim_ft':20}, 'terreno_fonte':['Ruin','Swamp'], 'scores':[12,6,16,3,6,4],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':8, 'idiomas':['understands languages known in life; cannot speak'], 'bonus_proficiencia':2, 'maneuver_dc':11,
 'tracos':[tr('Undead Fortitude (1/day)','Se reduzido a 0 PV por dano que não seja radiant nem acerto crítico, fica com 1 PV, cai Prone e Stunned até o fim do próximo turno, parecendo morto.',uso='1/day'), tr('Undead Nature','Não precisa respirar, alimentar-se ou dormir.'), tr('Fogwalk','Ignora terreno difícil e efeitos danosos de terreno se mover em trajetória horizontal direta e terminar em espaço desocupado capaz de sustentá-lo. Ao entrar ou sair de cada quadrado, deixa neblina que o obscurece levemente até o início do próximo turno.'), tr('Water Walker','Recebe deslocamento de natação igual ao seu deslocamento e pode mover-se sobre a água como se fosse chão sólido.')],
 'acoes':[act('Grab','Ataque corpo a corpo +3, alcance 5 ft.; 1d6+1 bludgeoning. Alvo Medium ou menor fica Grappled (escape DC 11); enquanto o agarrão durar, o zombie não pode agarrar outro alvo.',ataque='+3',alcance='5 ft.',dano=[{'dados':'1d6+1','tipo':'bludgeoning'}],salvaguarda='escape DC 11'), act('Bite','Ataque corpo a corpo +3, alcance 5 ft., contra alvo Grappled; 1d10+1 piercing e recupera PV iguais ao dano causado.',ataque='+3',alcance='5 ft.',dano=[{'dados':'1d10+1','tipo':'piercing'}])],
 'secoes_nao_listadas':['salvaguardas','perícias','resistências e vulnerabilidades','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/3461', 'citation':'turn96view1'
},
 'TF-295': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'celestial', 'alinhamento':'good', 'nd_fonte':'3', 'ca':16, 'ca_base':'natural armor', 'pv':52, 'formula_pv':'7d10+14; bloodied 26',
 'deslocamento':{'walk_ft':55}, 'terreno_fonte':['Astral Plane','Ethereal Plane'], 'tags':['NPC'], 'scores':[17,15,15,10,15,11],
 'salvaguardas':{}, 'pericias':{'Perception':4,'Stealth':4}, 'resistencias_dano':['poison','radiant'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['fatigue','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Celestial','Common'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Good','Emana uma aura Good.'),tr('Pack Tactics','Tem vantagem em ataques contra criatura se ao menos um aliado não incapacitado estiver a até 5 ft. dela.')],
 'acoes':[act('Holy Blade','Ataque corpo a corpo +5, alcance 5 ft.; 10 (2d6+3) slashing e 7 (2d6) radiant. Se o alvo for criatura, salvaguarda de Força CD 12 ou fica Prone.',ataque='+5',alcance='5 ft.',dano=[{'dados':'2d6+3','tipo':'slashing'},{'dados':'2d6','tipo':'radiant'}],salvaguarda='Strength DC 12')],
 'acoes_bonus':[act('Celestial Step','Teleporta para espaço desocupado visível a até 20 ft.')],
 'secoes_nao_listadas':['salvaguardas','imunidades e vulnerabilidades adicionais','ações bônus adicionais','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/3433', 'citation':'turn107view1'
},
'TF-469': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'monstrosity', 'alinhamento':'lawful', 'nd_fonte':'13', 'ca':17, 'ca_base':'natural armor', 'pv':210, 'formula_pv':'20d10 + 100; bloodied 105',
 'deslocamento':{'walk_ft':40,'climb_ft':40}, 'terreno_fonte':['Ethereal Plane','Forest','Jungle'], 'tags':['Legendary'], 'scores':[18,20,20,16,20,18],
 'salvaguardas':{}, 'pericias':{'Deception':9,'Insight':10,'Intimidation':9,'Perception':10,'Stealth':10}, 'resistencias_dano':[], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['paralyzed','poisoned'],
 'sentidos':['truesight 30 ft.','darkvision 120 ft.'], 'percepcao_passiva':20, 'idiomas':['Common','Undercommon','telepathy 30 ft.'], 'bonus_proficiencia':5, 'maneuver_dc':18,
 'tracos':[tr('Ethereal Sight','Enxerga simultaneamente o Waking e o Ethereal Plane.'),
 tr('Innate Spellcasting','Atributo Sabedoria, CD 18; sem componentes materiais; 3/dia cada: alarm, detect thoughts, legend lore, mirage arcane, misty step, scrying.',cd=18),
 tr('Lawful','Emana uma aura Lawful.'),
 tr('Legendary Resistance (3/day)','Quando falha em salvaguarda, escolhe obter sucesso. Um dos oito olhos fica opaco; role 1d8 na lista de efeitos secundários de Eye Beam. Alvos obtêm sucesso automaticamente nas salvaguardas contra esse efeito.',uso='3/day'),
 tr('Psionic Awareness','Quando uma criatura a até 1 milha usa habilidade psíquica, sabe sua direção, mas não a distância.'),
 tr('Spider Climb','Pode usar o deslocamento de escalada em superfícies difíceis e de cabeça para baixo no teto.'),
 tr('Web Walker','Ignora restrições de movimento impostas por teias.')],
 'acoes':[act('Multiattack','Faz quatro ataques Claw; pode substituir qualquer Claw por Eye Beam.'),
 act('Claw','Ataque corpo a corpo +10, alcance 10 ft.; 9 (1d8+5) slashing e o alvo fica Grappled (escape DC 18).',ataque='+10',alcance='10 ft.',dano=[{'dados':'1d8+5','tipo':'slashing'}],salvaguarda='escape DC 18'),
 act('Bite','Ataque corpo a corpo +10, alcance 5 ft., contra alvo Grappled por Fateholder; 12 (2d6+5) slashing e 21 (6d6) poison. Alvo faz salvaguarda de Constituição CD 15; em falha, é infectado com pastrasites (T&T p. 163), que se manifestam no próximo descanso.',ataque='+10',alcance='5 ft.',dano=[{'dados':'2d6+5','tipo':'slashing'},{'dados':'6d6','tipo':'poison'}],salvaguarda='Constitution DC 15',duracao='manifestação no próximo descanso'),
 act('Eye Beam','Ataque mágico à distância +10, alcance 120 ft.; 9 (2d8) psychic. Alvo faz salvaguarda de Constituição CD 17; em falha, sofre um efeito secundário escolhido aleatoriamente entre os oito abaixo.',ataque='+10',alcance='120 ft.',dano=[{'dados':'2d8','tipo':'psychic'}],salvaguarda='Constitution DC 17'),
 act('Eye Beam — Alter Fate','Alvo fica Doomed e sabe que morrerá devido a uma cadeia bizarra de coincidências em 13 (2d12) horas. Além dos meios normais de remover a condição, o efeito pode ser evitado se Fateholder morrer ou o encerrar com uma ação. Alternativamente, Fateholder substitui permanentemente a Destiny do alvo por uma que escolher; quem desbloqueou fulfillment da Destiny anterior já considera desbloqueado o da nova.',duracao='13 (2d12) horas até a morte prevista; substituição de Destiny permanente'),
 act('Eye Beam — Cut Strand','Alvo sofre 13 (3d8) necrotic adicional. Se isso o reduzir a 0 PV, morre e seu corpo desaparece; criaturas a mais de 100 ft. quando ele morre esquecem sua existência até serem lembradas. Só wish ou true resurrection desfaz esse efeito.',dano=[{'dados':'3d8','tipo':'necrotic'}]),
 act('Eye Beam — Foreshadow','O próximo acerto contra o alvo antes do fim do próximo turno de Fateholder é acerto crítico.',duracao='até o fim do próximo turno de Fateholder'),
 act('Eye Beam — Seal Spells','Alvo não pode conjurar magias nem usar habilidades psíquicas até o fim do próximo turno.',duracao='até o fim do próximo turno'),
 act('Eye Beam — Shift Reality','Fateholder teleporta o alvo para espaço desocupado a até 120 ft. dela, em superfície sólida; não precisa ver o espaço.'),
 act('Eye Beam — Tangle Psyches','Alvo fica Confused até o fim do próximo turno.',duracao='até o fim do próximo turno'),
 act('Eye Beam — Terrify','Alvo fica Frightened até o fim do próximo turno e seu Speed fica 0.',duracao='até o fim do próximo turno'),
 act('Eye Beam — Twist History','Altera objeto não mágico de porte Large ou menor, ou cubo de 10 ft. de objeto não mágico Huge ou maior, a até 5 ft. do alvo, substituindo-o por objeto similar de outra realidade. Pode criar, destruir ou mudar sua natureza, mas a mudança não pode causar imediatamente dano ou queda a criatura ou objeto.'),
 act('Ethereal Web (Recharge 5–6)','Libera seda etérea em cone de 60 ft.; a área fica preenchida por teias etéreas. Consulte os efeitos dependentes abaixo.',uso='Recharge 5–6')],
 'acoes_lendarias':[act('Eye Beam','Usa Eye Beam.'),act('Focused Eye Beam (Costs 2 Actions)','Usa Eye Beam e escolhe o efeito secundário em vez de determinar aleatoriamente.')],
 'economia_lendaria':'Dispõe de 4 ações lendárias; usa no máximo uma por vez, somente ao fim do turno de outra criatura, e recupera as gastas no início do próprio turno.',
 'efeitos_dependentes':[tr('Ethereal Web','As teias existem simultaneamente no Waking e Ethereal Plane e somem de ambos se destruídas em um. São translúcidas; em luz fraca, são percebidas passivamente com CD 13, mas qualquer busca ativa as encontra. Quem começa o turno na área ou entra nela durante o turno é transportado magicamente ao Ethereal Plane como alvo involuntário de etherealness, salvo se já estiver lá, e deve superar DC 14 de Destreza para evitar ficar Restrained; a página não especifica se é salvaguarda ou teste de atributo. Para escapar de Restrained, usa ação e teste de Athletics CD 14. Criaturas com Web Walker são imunes a ficar Restrained. Cada cubo de 10 ft. tem CA 14, 15 PV e imunidade a todos os tipos de dano, exceto fire e force; se sofrer fire, tudo no cubo sofre o mesmo dano. Ao sair da teia, a criatura escolhe viajar magicamente ao Waking ou permanecer no Ethereal Plane.',fonte_url='https://a5e.tools/node/2505'),
 tr('Doomed','Uma criatura Doomed morre em momento escolhido pelo Narrador ou em até 13 (2d12) horas; permanece Doomed após morrer. Magia equivalente a magia de 7º nível ou superior pode remover a condição.',fonte_url='https://a5e.tools/rules/conditions'),
 tr('Confused','Não pode usar reações; em seu turno rola 1d8: 1–4 não faz nada; 5–6 não usa ação nem ação bônus e move-se toda a distância em direção aleatória; 7–8 faz ataque corpo a corpo contra criatura aleatória ao alcance, ou nada se não puder.',fonte_url='https://a5e.tools/rules/conditions')],
 'fontes_adicionais':[{'titulo':'Ethereal Web — Level Up','url':'https://a5e.tools/node/2505','citation':'turn11view1'},{'titulo':'Conditions — Level Up','url':'https://a5e.tools/rules/conditions','citation':'turn112search0'}],
 'secoes_nao_listadas':['salvaguardas','resistências e vulnerabilidades além das imunidades a poison','ações bônus','reações','ações míticas','ações de covil','conjuração de slots'],
 'completa':False,
 'nota_fonte':'A página oficial do Fateholder e a regra complementar oficial Ethereal Web foram reabertas. Ambas registram DC 14 Dexterity para evitar Restrained sem especificar se é salvaguarda ou teste de atributo. A categoria não foi inferida; a ficha permanece parcial.',
 'url':'https://a5e.tools/node/2194','citation':'turn11view0'
},
'TF-513': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'celestial', 'alinhamento':'good', 'nd_fonte':'2', 'ca':15, 'ca_base':'natural armor', 'pv':37, 'formula_pv':'5d10+10; bloodied 18',
 'deslocamento':{'walk_ft':50}, 'terreno_fonte':['Astral Plane','Ethereal Plane'], 'tags':['NPC'], 'scores':[17,15,15,10,14,11],
 'salvaguardas':{}, 'pericias':{'Perception':4,'Religion':4,'Stealth':4}, 'resistencias_dano':['poison','radiant'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Celestial','Common'], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Good','Emana uma aura Good.'),tr('Pack Tactics','Tem vantagem em ataques contra criatura se ao menos um aliado não incapacitado estiver a até 5 ft. dela.')],
 'acoes':[act('Holy Blade','Ataque corpo a corpo +4, alcance 5 ft.; 10 (2d6+3) slashing e 5 (2d4) radiant. Se o alvo for criatura, salvaguarda de Força CD 13 ou fica Prone.',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d6+3','tipo':'slashing'},{'dados':'2d4','tipo':'radiant'}],salvaguarda='Strength DC 13')],
 'acoes_bonus':[act('Celestial Step','Teleporta para espaço desocupado visível a até 15 ft.')],
 'secoes_nao_listadas':['salvaguardas','imunidades e vulnerabilidades adicionais','ações bônus adicionais','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/3432', 'citation':'turn111view0'
},
'TF-520': {
 'fonte_publicacao':"Voidrunner's Codex", 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Gargantuan', 'tipo_fonte':'aberration', 'alinhamento':'', 'nd_fonte':'4', 'ca':14, 'ca_base':'natural armor', 'pv':300, 'formula_pv':'24d20 + 48; bloodied 150',
 'deslocamento':{'walk_ft':0,'fly_ft':80,'fly_qualifier':'spacefaring average'}, 'terreno_fonte':['Astral Plane'], 'scores':[18,14,18,6,14,8],
 'iniciativa_fonte':'Dex +2 (12), Insight +2 (12), Perception +2 (12)',
 'salvaguardas':{'STR':4,'DEX':2,'CON':4,'INT':-2,'WIS':2,'CHA':-1}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':[], 'percepcao_passiva':12, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':14,
 'tracos':[tr('Communicator','Pode escutar e replicar perfeitamente qualquer comunicação eletrônica, mas não altera a mensagem nem cria comunicação original.'),
 tr('False Appearance','Enquanto imóvel, é indistinguível de objeto inanimado, como uma nave espacial.'),
 tr('Sticky','Criatura ou objeto que toca Mayday fica preso. Uma criatura ou nave pode usar ação para fazer teste de Força CD 24; sucesso encerra o efeito. Mayday também pode encerrá-lo voluntariamente ou o efeito termina quando morre.')],
 'acoes':[act('Multiattack','Faz um ataque Pseudopod e um ataque Bite.'),
 act('Bite','Ataque corpo a corpo +6, alcance corpo a corpo conforme termo da fonte; um alvo preso a Mayday; 46 (4d20+4) piercing.',ataque='+6',alcance='melee range (termo da fonte)',dano=[{'dados':'4d20+4','tipo':'piercing'}]),
 act('Pseudopod','Ataque corpo a corpo +6, alcance “short” conforme termo da fonte; um alvo que não esteja preso; 22 (4d8+4) bludgeoning. Alvo fica sujeito a Sticky e é puxado para alcance corpo a corpo.',ataque='+6',alcance='short (termo da fonte)',dano=[{'dados':'4d8+4','tipo':'bludgeoning'}])],
 'acoes_bonus':[act('Shapeshift','Muda para forma aproximada de objeto que tenha visto, como nave, destroços ou asteroide, ou retorna à forma verdadeira de massa prateada. Objetos que carrega ou criaturas/objetos presos não se transformam; estatísticas não mudam; reverte ao morrer.')],
 'secoes_nao_listadas':['resistências e vulnerabilidades a dano','imunidades a dano e condições','perícias','ações bônus adicionais','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/5326', 'citation':'turn107view0'
},
'TF-460': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Huge', 'tipo_fonte':'monstrosity', 'alinhamento':'', 'nd_fonte':'3', 'ca':14, 'ca_base':'natural armor; 10 while prone', 'pv':59, 'formula_pv':'7d12 + 14; bloodied 29',
 'deslocamento':{'walk_ft':30,'burrow_ft':15}, 'terreno_fonte':['Desert','Grassland','Hills','Settlement'], 'tags':['Legendary'], 'scores':[16,10,14,2,14,8],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['acid'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['tremorsense 30 ft.'], 'percepcao_passiva':12, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'acoes':[act('Claws','Ataque corpo a corpo +5, alcance 5 ft.; 2d8+3 slashing. Alvo Medium ou menor fica Grappled (escape DC 13) e Restrained; enquanto o agarrão durar, Ankheg Queen não pode usar Claws contra outra criatura.',ataque='+5',alcance='5 ft.',dano=[{'dados':'2d8+3','tipo':'slashing'}],salvaguarda='escape DC 13'), act('Bite','Ataque corpo a corpo +5, alcance 5 ft., contra criatura Grappled pela Ankheg Queen; 3d8+3 slashing. Se o dano matar o alvo, ela decepa sua cabeça.',ataque='+5',alcance='5 ft.',dano=[{'dados':'3d8+3','tipo':'slashing'}]), act('Acid Spray (Recharge 6)','Jato de ácido com 30 ft. de comprimento e 5 ft. de largura; cada criatura na área faz salvaguarda de Destreza CD 13, sofrendo 4d6 acid em falha ou metade em sucesso. Se a Queen estiver agarrando um alvo, pode banhá-lo em ácido: 4d6 acid sem teste, somente nesse alvo.',uso='Recharge 6',salvaguarda='Dexterity DC 13',dano=[{'dados':'4d6','tipo':'acid'}])],
 'acoes_lendarias':[act('Acid Glob','Ataque à distância +5, alcance 30/90 ft.; 1d8+3 acid.',ataque='+5',alcance='30/90 ft.',dano=[{'dados':'1d8+3','tipo':'acid'}]), act('Burrowing Ambush (1/day)','Escava até seu deslocamento de burrow sem provocar ataques de oportunidade e reaparece; se estiver em alcance corpo a corpo de inimigo, faz Claws com vantagem.',uso='1/day')],
 'economia_lendaria':'Dispõe de 1 ação lendária ao fim do turno de outra criatura; recupera a ação gasta no início do próprio turno.',
 'secoes_nao_listadas':['salvaguardas','perícias','imunidades e vulnerabilidades adicionais','ações bônus','reações','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/1463', 'citation':'turn99view3'
},
'TF-475': {
 'fonte_publicacao':'Monstrous Menagerie', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'monstrosity', 'alinhamento':'chaotic evil', 'nd_fonte':'4', 'ca':13, 'ca_base':'', 'pv':85, 'formula_pv':'10d10 + 30; bloodied 42',
 'deslocamento':{'walk_ft':30,'swim_ft':30}, 'terreno_fonte':['Plane of Water','Water'], 'scores':[16,16,16,14,16,18],
 'salvaguardas':{}, 'pericias':{'Deception':6,'Perception':5,'Stealth':5}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':15, 'idiomas':['Abyssal','Common'], 'bonus_proficiencia':2, 'maneuver_dc':13,
'tracos':[tr('Chaotic Evil','Emana uma aura Chaotic e Evil.'), tr('Innate Spellcasting','Atributo Carisma, CD 14; não requer componentes materiais. À vontade: charm person, disguise self (forma humanoide), major image, misty step. 1/dia cada: geas, hallucinatory terrain, scrying.',cd=14)],
 'acoes':[act('Dizzying Touch','Ataque mágico corpo a corpo +6, alcance 5 ft.; alvo fica Charmed magicamente por 1 hora ou até sofrer dano. Enquanto Charmed dessa forma, tem desvantagem em salvaguardas de Sabedoria e testes de atributo.',ataque='+6',alcance='5 ft.',duracao='1 hour or until damaged'), act('Claws','Ataque corpo a corpo +5, alcance 5 ft.; 4d6+3 slashing.',ataque='+5',alcance='5 ft.',dano=[{'dados':'4d6+3','tipo':'slashing'}]), act('Dagger','Ataque +5 corpo a corpo (alcance 5 ft.) ou à distância (20/60 ft.); 1d4+3 piercing. O alvo faz salvaguarda de Constituição CD 13; falha causa mais 3d6 poison e condição Poisoned por 1 hora.',ataque='+5',alcance='5 ft. ou 20/60 ft.',dano=[{'dados':'1d4+3','tipo':'piercing'}],salvaguarda='Constitution DC 13'), act('Hypnotic Pattern (3rd-level; S; concentration)','Cria padrão luminoso num ponto a até 120 ft.; criaturas que o veem num raio de 10 ft. fazem salvaguarda de Sabedoria CD 14. Falha: Charmed por 1 minuto, Incapacitated e Speed 0; dano ou ação de outra criatura para sacudi-la encerra o efeito.',salvaguarda='Wisdom DC 14',duracao='1 minute; concentration')],
 'acoes_bonus':[act('Misty Step (2nd-level; V)','Teleporta para espaço desocupado visível a até 30 ft.; não pode conjurar esta magia e outra magia de 1º nível ou superior no mesmo turno.')],
 'conjuracao':{'atributo':'CHA','cd':14,'sem_componentes':['material'],'at_will':['charm person','disguise self (humanoid form)','major image','misty step'],'1/day each':['geas','hallucinatory terrain','scrying']},
 'secoes_nao_listadas':['salvaguardas','resistências e imunidades','reações','ações lendárias','ações míticas','ações de covil'],
 'nota_tatica':'Evita combate corpo a corpo, usando aliados para lutar enquanto lança Hypnotic Pattern e arremessa adagas; quando encurralado, ataca com Claws e tenta escapar com Misty Step.',
 'url':'https://a5e.tools/node/1712', 'citation':'turn99view0'
},
'TF-480': {
 'fonte_publicacao':'Gate Pass Gazette', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'plant', 'alinhamento':'', 'nd_fonte':'6', 'ca':15, 'ca_base':'natural armor', 'pv':123, 'formula_pv':'13d10 + 52; bloodied 61',
 'deslocamento':{'walk_ft':20,'swim_ft':20}, 'terreno_fonte':['Sewer'], 'scores':[18,10,18,6,12,6],
 'salvaguardas':{}, 'pericias':{'Stealth':3}, 'resistencias_dano':['cold','fire','piercing'], 'imunidades_dano':['lightning'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','deafened','fatigue'],
 'sentidos':['blindsight 60 ft. (blind beyond this radius)'], 'percepcao_passiva':11, 'idiomas':[], 'bonus_proficiencia':3, 'maneuver_dc':15,
 'tracos':[tr('Acid Absorption','Quando sofre dano acid, em vez disso recupera PV iguais ao dano acid causado.')],
 'acoes':[act('Multiattack','Faz dois ataques Lash. Se ambos atingirem uma criatura Medium ou menor, ela fica Grappled (escape DC 15) e o Sewer Walker usa Drown contra ela.'), act('Lash','Ataque corpo a corpo +7, alcance 10 ft.; 2d8+4 bludgeoning.',ataque='+7',alcance='10 ft.',dano=[{'dados':'2d8+4','tipo':'bludgeoning'}]), act('Drown','Arrasta criatura Medium ou menor Grappled para baixo do próprio corpo. Ela fica Restrained e Rattled, não pode respirar e se move junto com o Sewer Walker; no início de cada turno do monstro sofre 2d6+4 acid. Quando o agarrão termina, o afogamento termina. O Sewer Walker só pode manter uma criatura afogada por vez.',dano=[{'dados':'2d6+4','tipo':'acid'}],duracao='enquanto o agarrão durar')],
 'efeitos_dependentes':[tr('Rattled','A criatura não pode beneficiar-se de expertise dice e não pode usar reações; criaturas imunes a Stunned também são imunes a Rattled.',fonte_url='https://a5e.tools/rules/conditions'), tr('Restrained','Speed 0 e não recebe bônus a deslocamento; ataques contra ela têm vantagem, seus ataques têm desvantagem e faz salvaguardas de Destreza com desvantagem.',fonte_url='https://a5e.tools/rules/conditions')],
 'fontes_adicionais':[{'titulo':'Conditions — Level Up','url':'https://a5e.tools/rules/conditions','citation':'turn104view0'}],
 'secoes_nao_listadas':['salvaguardas','imunidades e vulnerabilidades adicionais','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/2208', 'citation':'turn101view0'
},
'TF-491': {
 'fonte_publicacao':"Dungeon Delver's Guide", 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'ooze', 'alinhamento':'', 'nd_fonte':'4', 'ca':7, 'ca_base':'', 'pv':85, 'formula_pv':'10d10 + 30; bloodied 42',
 'deslocamento':{'walk_ft':20,'climb_ft':20,'swim_ft':20}, 'terreno_fonte':['Caverns','Ruin','Sewer','Water'], 'scores':[16,4,16,1,6,1],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['acid','cold','fire','lightning','slashing'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','deafened','fatigue','frightened','prone'],
 'sentidos':['blindsight 60 ft. (blind beyond this radius)'], 'percepcao_passiva':8, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':13,
 'tracos':[tr('Amorphous','Passa por abertura de até 1 inch sem precisar se espremer.'), tr('Corrosive Body','Criatura que toque o pudding ou o acerte corpo a corpo a até 5 ft. sofre 2d8 acid. Armas não mágicas de madeira ou metal que o atingem recebem penalidade cumulativa permanente de −1 no dano por acerto, sendo destruídas em −5; munição não mágica de madeira ou metal é destruída depois de causar dano. Outros objetos metálicos ou orgânicos que o toquem sofrem 2d8 acid.'), tr('Spider Climb','Usa seu deslocamento de climb inclusive em superfícies difíceis e tetos de cabeça para baixo.'), tr('Sunlight Sensitivity','Enquanto sob luz solar, tem desvantagem em jogadas de ataque.'), tr('Ooze Nature','Não precisa respirar nem dormir.'), tr('Blazing Form','Ao sofrer dano fire, incendeia-se até o fim do próximo turno. Enquanto em chamas, é imune a fire, emite bright light em 30 ft. e dim light por mais 30 ft., dobra o deslocamento, pode fazer Pseudopod como ação bônus e criaturas adjacentes que o toquem ou acertem corpo a corpo sofrem 1d4 fire.')],
 'acoes':[act('Pseudopod','Ataque corpo a corpo +5, alcance 5 ft.; 1d6+3 bludgeoning e 2d8 acid. Armadura não mágica vestida pelo alvo recebe penalidade cumulativa permanente de −1 na proteção de CA por acerto; se a proteção cair a 10, é destruída.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'bludgeoning'},{'dados':'2d8','tipo':'acid'}])],
 'acoes_bonus':[act('Pseudopod (while ablaze)','Enquanto Blazing Form estiver ativa, pode fazer um ataque Pseudopod como ação bônus.',ataque='+5',alcance='5 ft.')],
 'reacoes':[act('Split','Quando um pudding Medium ou maior com pelo menos 10 PV é submetido a dano lightning ou slashing, divide-se em dois puddings de um porte menor; cada um tem metade dos PV originais, arredondada para baixo.')],
 'secoes_nao_listadas':['salvaguardas','perícias','vulnerabilidades','multiataque','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://www.a5e.tools/node/2866', 'citation':'turn100view0'
},
'TF-492': {
 'fonte_publicacao':"Dungeon Delver's Guide", 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'ooze', 'alinhamento':'', 'nd_fonte':'6', 'ca':9, 'ca_base':'', 'pv':104, 'formula_pv':'11d10 + 44; bloodied 52',
 'deslocamento':{'walk_ft':15,'climb_ft':15,'swim_ft':15}, 'terreno_fonte':['Ruin','Tomb'], 'scores':[16,8,18,3,10,4],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['damage from nonmagical weapons'], 'imunidades_dano':['acid'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','deafened','fatigue','frightened','prone'],
 'sentidos':['blindsight 120 ft. (blind beyond this radius)'], 'percepcao_passiva':10, 'idiomas':[], 'bonus_proficiencia':3, 'maneuver_dc':14,
 'tracos':[tr('Amorphous','Passa por abertura de até 1 inch sem precisar se espremer e pode ocupar o mesmo espaço que criatura do próprio porte ou menor.'), tr('Corrosive','Armas não mágicas de madeira ou metal que o atingem recebem penalidade cumulativa permanente de −1 no dano por acerto e são destruídas quando chegam a −5. Munição não mágica de madeira ou metal é destruída após causar dano. O slime mold corrói 2-inch de madeira ou metal não mágico em 1 rodada.'), tr('Damage Transfer','Enquanto uma criatura estiver Engulfed dentro dele, o slime mold sofre metade do dano; a outra metade é dividida igualmente entre as criaturas engolidas.'), tr('False Appearance','Imóvel, é indistinguível de mofo ou líquen comum.'), tr('Spider Climb','Escala superfícies difíceis e tetos de cabeça para baixo.'), tr('Sticky','Criatura que toque o slime mold fica Stuck, Speed 0, e sofre 2d8 acid no início de cada turno. Pode usar ação e teste de Força CD 13 para se libertar. Criatura que o acerte corpo a corpo faz salvaguarda de Força CD 13 ou sua arma fica presa; pode usar ação e teste de Força CD 13 para soltá-la. No início de cada turno do slime mold, arma presa é submetida a Corrosive.')],
 'acoes':[act('Pseudopod','Ataque corpo a corpo +6, alcance 5 ft.; 2d8+3 bludgeoning e 6d6 acid; alvo fica sujeito a Sticky.',ataque='+6',alcance='5 ft.',dano=[{'dados':'2d8+3','tipo':'bludgeoning'},{'dados':'6d6','tipo':'acid'}]), act('Engulf','Tenta engolir criaturas Stuck. Cada uma faz salvaguarda de Força CD 15; falha: fica Engulfed e Stuck. Criatura engolida fica Restrained, não pode respirar e sofre 6d6 acid no início de cada turno do slime mold, movendo-se com ele. Se deixar de estar Stuck, também deixa de estar Engulfed. Pode engolir uma criatura do seu porte ou duas menores.',salvaguarda='Strength DC 15',dano=[{'dados':'6d6','tipo':'acid'}])],
 'acoes_bonus':[act('Merge','Une-se a outro slime mold do mesmo porte; o novo slime mold tem PV iguais à soma dos dois e aumenta um porte.'), act('Split','Se Medium ou maior e com pelo menos 10 PV, divide-se em dois slime molds um porte menor, cada um com metade dos PV originais arredondada para baixo. Criaturas engolidas deixam de estar Engulfed, mas continuam Stuck a um dos novos slime molds.')],
 'secoes_nao_listadas':['salvaguardas','perícias','vulnerabilidades','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/2869', 'citation':'turn101view1'
},
'TF-512': {
 'fonte_publicacao':'Mythological Figures & Maleficent Monsters', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Huge', 'tipo_fonte':'celestial', 'alinhamento':'', 'nd_fonte':'14', 'ca':18, 'ca_base':'natural armor', 'pv':230, 'formula_pv':'20d12 + 100; bloodied 115',
 'deslocamento':{'walk_ft':40,'fly_ft':80,'fly_hover':True}, 'terreno_fonte':['Hills'], 'tags':['NPC','Unique'], 'scores':[23,21,20,18,19,20],
 'salvaguardas':{}, 'pericias':{'Acrobatics':10,'Arcana':9,'History':9,'Nature':9,'Perception':9,'Religion':9}, 'pericias_bonus_dado':{'Nature':'1d6','Perception':'1d6'},
 'resistencias_dano':['psychic','bludgeoning, piercing, and slashing from nonmagical weapons'], 'imunidades_dano':['lightning','necrotic','radiant','thunder'], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 120 ft.'], 'percepcao_passiva':24, 'idiomas':['Common','telepathy 200 ft.'], 'bonus_proficiencia':5, 'maneuver_dc':19,
 'tracos':[tr('Innate Spellcasting','Atributo Carisma, CD 18, +10 para ataques mágicos; sem componentes materiais. Constante: tongues. À vontade: detect evil and good, detect magic, fog cloud, gust of wind, thunderwave. 3/dia cada: lightning bolt, shatter. 1/dia cada: conjure elemental (somente air elemental), control weather.',cd=18), tr('Magic Resistance','Vantagem em salvaguardas contra efeitos mágicos e magias.'), tr('Shapechanger','Como ação, assume forma de humanoide que tenha visto ou retorna à forma verdadeira. Estatísticas permanecem iguais salvo tamanho; equipamento não se transforma; volta à forma verdadeira ao morrer.'), tr('Tornado Aura','Ataques com armas à distância contra Anzû têm desvantagem. Um atacante pode anular isso para um único ataque se usar ação bônus para mirar imediatamente antes.')],
 'acoes':[act('Multiattack','Faz dois ataques Claw, dois Talon e um Bite.'), act('Bite','Ataque corpo a corpo mágico +11, alcance 5 ft.; 2d10+6 piercing.',ataque='+11',alcance='5 ft.',dano=[{'dados':'2d10+6','tipo':'piercing mágico'}]), act('Claw','Ataque corpo a corpo mágico +11, alcance 10 ft.; 2d6+6 slashing.',ataque='+11',alcance='10 ft.',dano=[{'dados':'2d6+6','tipo':'slashing mágico'}]), act('Talon','Ataque corpo a corpo mágico +11, alcance 15 ft.; 2d8+6 slashing.',ataque='+11',alcance='15 ft.',dano=[{'dados':'2d8+6','tipo':'slashing mágico'}]), act('Create Whirlwind','Cria cilindro mágico de ar rodopiante com raio 15 ft. e altura 50 ft., num ponto visível até 200 ft.; dura até Anzû encerrá-lo no próprio turno ou criar outro. Criaturas que entrem fazem salvaguarda de Força CD 18 ou ficam Restrained. Se Anzû perder o ponto de vista, o redemoinho termina. Uma criatura pode usar ação e teste de Força CD 17 para libertar uma criatura presa, inclusive a si, que então vai ao espaço mais próximo fora do redemoinho.',salvaguarda='Strength DC 18; Strength check DC 17 to free',duracao='até ser encerrado ou perder de vista'), act('Tempest (Recharge 5–6)','Criaturas a até 15 ft. fazem salvaguarda de Força CD 18; falha: 3d8+6 bludgeoning e Prone. Falha por 5 ou mais também arremessa a criatura 10 ft. por cada 5 pontos de falha. Colisão com objeto causa 1d6 bludgeoning por 10 ft. arremessados. Se lançada contra outra criatura, esta faz salvaguarda de Destreza CD 18 para evitar dano e Prone. A fonte não deixa claro a que alvo se aplica a sentença subsequente sobre sucesso da salvaguarda; efeito não foi inferido.',uso='Recharge 5–6',salvaguarda='Strength DC 18; Dexterity DC 18 for creature struck',dano=[{'dados':'3d8+6','tipo':'bludgeoning'},{'dados':'1d6 por 10 ft. de colisão','tipo':'bludgeoning'}])],
 'acoes_bonus':[act('Move Whirlwind','Move um redemoinho criado por Create Whirlwind até 60 ft.; criaturas Restrained por ele movem-se junto.')],
 'conjuracao':{'atributo':'CHA','cd':18,'ataque_magia':'+10','sem_componentes':['material'],'constant':['tongues'],'at_will':['detect evil and good','detect magic','fog cloud','gust of wind','thunderwave'],'3/day each':['lightning bolt','shatter'],'1/day each':['conjure elemental (air elemental only)','control weather']},
 'secoes_nao_listadas':['salvaguardas','vulnerabilidades','reações','ações lendárias','ações míticas','ações de covil'],
 'completa':False, 'nota_fonte':'A ação Tempest tem uma ambiguidade textual no trecho final: após descrever a salvaguarda de Destreza da criatura atingida pelo arremesso, a página diz que, se a salvaguarda for bem-sucedida, “the target” sofre metade do dano e não é arremessado nem derrubado, sem deixar claro a qual criatura se refere. Valores e efeitos recuperáveis foram mantidos, sem escolher um alvo para essa cláusula. A fonte identifica a publicação como Mythological Figures & Maleficent Monsters, enquanto o catálogo original registra “A5E — diversos suplementos”; ambos os valores foram preservados separadamente.',
 'url':'https://www.a5e.tools/node/2393', 'citation':'turn12view0'
},
'TF-519': {
 'fonte_publicacao':'To Save A Kingdom', 'editora_fonte':'EN Publishing', 'sistema':'Level Up Advanced 5th Edition (página de ferramenta; não é o A5ESRD)',
 'porte':'Large', 'tipo_fonte':'beast', 'alinhamento':'', 'nd_fonte':'2', 'ca':14, 'ca_base':'natural armor', 'pv':52, 'formula_pv':'8d10 + 8; bloodied 26',
 'deslocamento':{'walk_ft':30,'climb_ft':30}, 'terreno_fonte':['Swamp'], 'scores':[14,12,12,2,10,4],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 30 ft.'], 'percepcao_passiva':10, 'idiomas':[], 'bonus_proficiencia':2, 'maneuver_dc':12,
 'tracos':[tr('Spider Climb','Usa deslocamento de escalada inclusive em superfícies difíceis e de cabeça para baixo no teto.')],
 'acoes':[act('Bite','Ataque corpo a corpo +4, alcance 5 ft.; 1d4+2 piercing.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d4+2','tipo':'piercing'}])],
 'secoes_nao_listadas':['salvaguardas','perícias adicionais','resistências e imunidades','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'url':'https://a5e.tools/node/3265', 'citation':'turn97view2'
},
'KP-S002': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e; bloco mecânico conferido em referência secundária que reproduz a página 155 de Tome of Beasts 2',
 'porte':'Huge', 'tipo_fonte':'aberration', 'alinhamento':'neutral evil', 'nd_fonte':'15', 'ca':18, 'ca_base':'natural armor', 'pv':161, 'formula_pv':'14d12 + 70',
 'deslocamento':{'walk_ft':30,'climb_ft':30,'fly_ft':60}, 'scores':[23,12,21,12,20,8],
 'salvaguardas':{'CON':10,'WIS':10}, 'pericias':{'Nature':6,'Perception':10,'Stealth':6},
 'resistencias_dano':[], 'imunidades_dano':['acid','cold','bludgeoning de ataques não mágicos'], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':20, 'idiomas':['Common','Giant'], 'bonus_proficiencia':5,
 'bonus_proficiencia_origem':'derivado do ND 15 pela progressão de D&D 5e; não aparece como campo separado na referência consultada',
 'tracos':[tr('Forest Camouflage','Tem vantagem em testes de Destreza (Furtividade) para se esconder em terreno de floresta.'),
           tr('Keen Smell','Tem vantagem em testes de Sabedoria (Percepção) baseados no olfato.'),
           tr('Rattle','No início do turno de cada criatura que possa ouvi-lo e esteja a até 60 ft., ela faz salvaguarda de Sabedoria CD 18; falha causa medo até o início do próximo turno dela. Após duas salvaguardas bem-sucedidas, a criatura fica imune ao Rattle por 24 horas.',salvaguarda='Wisdom DC 18',alcance='60 ft.',duracao='até o início do próximo turno; imunidade por 24 horas após duas salvaguardas bem-sucedidas')],
 'acoes':[act('Multiattack','Faz dois ataques Acidic Claw e um Tail. Se as duas garras acertarem a mesma criatura, ela faz salvaguarda de Constituição CD 18; em falha, seu máximo de PV diminui em 7 (2d6), e o Forest Emperor recupera a mesma quantidade. A redução termina após descanso longo; a criatura morre se seu máximo chegar a 0.',salvaguarda='Constitution DC 18'),
          act('Acidic Claw','Ataque corpo a corpo +11, alcance 5 ft.; 16 (3d6+6) cortante e 7 (2d6) ácido.',ataque='+11',alcance='5 ft.',dano=[{'dados':'3d6+6','tipo':'slashing'},{'dados':'2d6','tipo':'acid'}]),
          act('Tail','Ataque corpo a corpo +11, alcance 15 ft.; 17 (2d10+6) contundente.',ataque='+11',alcance='15 ft.',dano=[{'dados':'2d10+6','tipo':'bludgeoning'}]),
          act('Toxic Nectar Spray (Recharge 5–6)','Projeta ácido em cone de 60 ft.; salvaguarda de Destreza CD 18, 42 (12d6) ácido em falha ou metade em sucesso.',uso='Recharge 5–6',salvaguarda='Dexterity DC 18',alcance='cone de 60 ft.',dano=[{'dados':'12d6','tipo':'acid'}])],
 'secoes_nao_listadas':['ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros 5e da Kobold Press (identidade, ND, porte, tipo e publicação)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},
                      {'titulo':'Página individual 5eSRD (bloqueada para leitura direta por exigência de JavaScript)','url':'https://www.5esrd.com/database/creature/forest-emperor/'},
                      {'titulo':'Referência secundária: réplica digital de Tome of Beasts 2, página impressa 155','url':'https://anyflip.com/dhfzu/umbm/basic/151-200'}],
 'classe_fonte':'Metadados validados no índice oficial da Kobold Press; estatísticas completas conferidas em referência secundária que reproduz a página 155 de Tome of Beasts 2. O texto da ficha não foi reproduzido.',
 'completa':True, 'url':'https://www.5esrd.com/database/creature/forest-emperor/', 'citation':'turn1view0; turn2view2; turn5view1'
},
'KP-S004': {
 'fonte_publicacao':'Tome of Beasts 1', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e; ficha de 5eSRD com atribuição explícita a Tome of Beasts',
 'porte':'Gargantuan', 'tipo_fonte':'beast', 'alinhamento':'unaligned', 'nd_fonte':'11', 'ca':17, 'ca_base':'natural armor', 'pv':186, 'formula_pv':'12d20 + 60',
 'deslocamento':{'walk_ft':50}, 'scores':[28,10,21,3,12,10],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['bludgeoning'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['exhaustion'],
 'sentidos':[], 'percepcao_passiva':11, 'idiomas':[], 'bonus_proficiencia':4, 'bonus_proficiencia_origem':'listado explicitamente pela página 5eSRD',
 'tracos':[tr('Siege Monster','Causa dano dobrado a objetos e estruturas.')],
 'acoes':[act('Multiattack','Faz um ataque Gore e dois ataques Stomp.'),
          act('Gore','Ataque corpo a corpo +13, alcance 15 ft.; 25 (3d10+9) perfurante. Em acerto crítico, rola os dados de dano três vezes em vez de duas.',ataque='+13',alcance='15 ft.',dano=[{'dados':'3d10+9','tipo':'piercing'}]),
          act('Stomp','Ataque corpo a corpo +13, alcance 10 ft.; 22 (3d8+9) contundente. Criatura atingida faz salvaguarda de Força CD 17 ou fica caída.',ataque='+13',alcance='10 ft.',salvaguarda='Strength DC 17',dano=[{'dados':'3d8+9','tipo':'bludgeoning'}]),
          act('Deafening Bellow (Recharge 5–6)','Emite um bramido em cone de 60 ft., audível a até 1 milha. Salvaguarda de Constituição CD 17; em falha causa 44 (8d10) trovejante e ensurdece por 1 hora; em sucesso causa metade e não ensurdece. Criaturas de material inorgânico fazem a salvaguarda com desvantagem.',uso='Recharge 5–6',salvaguarda='Constitution DC 17',alcance='cone de 60 ft.; audível a 1 mile',dano=[{'dados':'8d10','tipo':'thunder'}]),
          act('Overrun (Recharge 6)','Move até 30 ft. em linha reta, atravessando o espaço de criaturas Grandes ou menores sem provocar ataques de oportunidade. A primeira criatura atravessada faz salvaguarda de Destreza CD 17; em falha sofre 54 (12d8) contundente e cai; em sucesso sofre metade e não cai.',uso='Recharge 6',salvaguarda='Dexterity DC 17',alcance='movimento em linha reta até 30 ft.',dano=[{'dados':'12d8','tipo':'bludgeoning'}])],
 'secoes_nao_listadas':['salvaguardas','perícias','sentidos especiais','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros 5e da Kobold Press (identidade, ND, porte, tipo e publicação)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},
                      {'titulo':'Referência secundária 5eSRD; ficha atribuída a Tome of Beasts (copyright notice na página)','url':'https://www.5esrd.com/database/creature/ychen-bannog-3pp/'},
                      {'titulo':'Variante antiga oficial de Pathfinder 3.5, rejeitada para este registro 5e','url':'https://koboldpress.com/monday-monster-ychen-bannog/'},
                      {'titulo':'Variante Ychen Bannog de Robinloft, com regras diferentes, não usada como ficha-base','url':'https://www.robinloft.com/monsters/ychen-bannog/tome-of-beasts'}],
 'classe_fonte':'Índice oficial da Kobold Press confirma Ychen Bannog, Tome of Beasts 1, ND 11, Gargantuan beast. A ficha completa foi conferida em página secundária 5eSRD com atribuição de copyright a Tome of Beasts. Foram rejeitadas a ficha Pathfinder 3.5 CR 12 e uma variante secundária com mecânicas distintas.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 1; não usar a versão Pathfinder 3.5 CR 12 nem variantes expandidas',
 'url':'https://www.5esrd.com/database/creature/ychen-bannog-3pp/', 'citation':'turn1view1; turn2view1; turn2view3'
},
'TF-007': {
 'fonte_publicacao':'Creature Codex', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e; bloco mecânico recuperado em referência secundária D&D Grove e conferido com a entrada 5eSRD indexada',
 'porte':'Huge', 'tipo_fonte':'aberration', 'alinhamento':'neutral', 'nd_fonte':'2', 'ca':12, 'ca_base':'natural armor', 'pv':47, 'formula_pv':'5d12 + 15',
 'deslocamento':{'walk_ft':30,'swim_ft':40}, 'scores':[15,11,17,8,14,7],
 'salvaguardas':{}, 'pericias':{'Perception':4,'Stealth':2}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['blindsight 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Aquan','telepathy 120 ft.'], 'bonus_proficiencia':2,
 'bonus_proficiencia_origem':'derivado do ND 2 pela progressão de D&D 5e; não aparece separado na referência D&D Grove',
 'tracos':[tr('Amphibious','Respira ar e água.'),tr('Underwater Camouflage','Tem vantagem em testes de Destreza (Furtividade) realizados debaixo d’água.')],
 'acoes':[act('Bite','Ataque corpo a corpo +4, alcance 5 ft.; 11 (2d8+2) perfurante.',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d8+2','tipo':'piercing'}]),
          act('Tentacles','Ataque corpo a corpo +4, alcance 15 ft.; 7 (2d4+2) contundente. Alvo Grande ou menor fica agarrado (escape CD 12) e contido enquanto o agarrão durar; o Yann-An-Oed mantém até dois alvos agarrados.',ataque='+4',alcance='15 ft.',salvaguarda='escape DC 12',dano=[{'dados':'2d4+2','tipo':'bludgeoning'}]),
          act('Swallow','Faz um ataque Bite contra criatura Grande ou menor que esteja agarrando; ao acertar, engole o alvo e encerra o agarrão. A vítima fica cega, contida e com cobertura total, sofre 7 (2d6) ácido no início do turno da criatura; só uma vítima pode ser engolida. Se a vítima causar pelo menos 10 de dano em um turno, no fim daquele turno o Yann-An-Oed faz salvaguarda de Constituição CD 11 ou a regurgita caída a até 10 ft. Se a criatura morrer, a vítima deixa de estar contida e pode escapar gastando 10 ft. de movimento, saindo caída.',salvaguarda='Constitution DC 11',alcance='alvo agarrado Grande ou menor',dano=[{'dados':'2d6','tipo':'acid'}]),
          act('Hoot (Recharges after a Short or Long Rest)','Cada criatura a até 120 ft. que possa ouvir faz salvaguarda de Sabedoria CD 12; em falha responde ao chamado se puder produzir som. O Yann-An-Oed rastreia por 1 hora qualquer criatura que responder, mesmo se ela estiver escondida por magia ou em outro plano.',uso='recarrega após descanso curto ou longo',salvaguarda='Wisdom DC 12',alcance='120 ft.',duracao='rastreamento por 1 hora')],
 'secoes_nao_listadas':['salvaguardas','resistências e imunidades','vulnerabilidades','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros 5e da Kobold Press (identidade, ND, porte, tipo e publicação)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},
                      {'titulo':'Página individual 5eSRD (renderização bloqueada por exigência de JavaScript)','url':'https://www.5esrd.com/database/creature/yann-an-oed/'},
                      {'titulo':'Referência secundária D&D Grove; ficha identificada como Creature Codex','url':'https://www.dndgrove.com/bestiary/2/yann-an-oed'}],
 'classe_fonte':'Índice oficial da Kobold Press confirma Yann-An-Oed, Creature Codex, ND 2, Huge aberration. Estatísticas e regras foram conferidas em resumo secundário D&D Grove; página individual 5eSRD continuou bloqueada para leitura automatizada.',
 'completa':True, 'url':'https://www.dndgrove.com/bestiary/2/yann-an-oed', 'citation':'turn1view2; turn2view0; turn2view4'
},
'TF-008': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e; metadados de identidade conferidos no índice oficial da Kobold Press; bloco mecânico consultado em transcrição secundária comunitária de conteúdo OGL.',
 'porte':'Large', 'tipo_fonte':'aberration', 'alinhamento':'neutral evil', 'nd_fonte':'8', 'ca':17, 'ca_base':'clockwork armor', 'pv':135, 'formula_pv':'18d10 + 36',
 'deslocamento':{'walk_ft':30,'fly_ft':30,'fly_hover':True,'swim_ft':30}, 'scores':[20,8,14,19,13,10],
 'salvaguardas':{}, 'pericias':{'Perception':4}, 'resistencias_dano':[], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','exhaustion','frightened','paralyzed','petrified','poisoned','prone'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Deep Speech','Void Speech'], 'bonus_proficiencia':3,
 'bonus_proficiencia_origem':'derivado do ND 8 pela progressão de D&D 5e; a transcrição secundária não lista um bônus separado',
 'tracos':[tr('Clockwork Encasement','A armadura permite atacar e interagir por meio de manipuladores. Ao chegar a 0 PV, quebra e o ahu-nixta sai. Sem armadura: CA 12, 37 PV (5d10 + 10), Força 9 (-1), todos os deslocamentos 20 ft. e sem ações de ataque; ainda pode conjurar. Apêndices podem manipular objetos, mas não servem para combate. Abrir ou fechar visores não exige ação; entrar ou sair da armadura exige ação bônus.'),
          tr('Immutable Form','A armadura é imune a magias e efeitos que alterem sua forma; o ahu-nixta também recebe essa proteção enquanto permanecer nela.'),
          tr('Innate Spellcasting','Usa Inteligência; CD 15 para suas magias e +7 para ataques mágicos. À vontade: fear, fire bolt (2d10) e telekinesis. Não requer componentes materiais.')],
 'acoes':[act('Multiattack','Faz três ataques corpo a corpo; pode substituir dois deles por uma magia à vontade. Alternativamente, usa Arcane Cannon duas vezes.'),
          act('Whirring Blades','Ataque corpo a corpo +8, alcance 5 ft.; 12 (3d4 + 5) slashing. O alvo faz salvaguarda de Destreza CD 15 ou sofre 5 (2d4) slashing no início do próximo turno.',ataque='+8',alcance='5 ft.',dano=[{'dados':'3d4 + 5','tipo':'slashing'},{'dados':'2d4','tipo':'slashing; salvaguarda de Destreza CD 15 falha'}],salvaguarda='Dexterity DC 15'),
          act('Pronged Scepter','Ataque corpo a corpo +8, alcance 10 ft.; 12 (2d6 + 5) piercing.',ataque='+8',alcance='10 ft.',dano=[{'dados':'2d6 + 5','tipo':'piercing'}]),
          act('Bashing Rod','Ataque corpo a corpo +8, alcance 5 ft.; 16 (2d10 + 5) bludgeoning.',ataque='+8',alcance='5 ft.',dano=[{'dados':'2d10 + 5','tipo':'bludgeoning'}]),
          act('Arcane Cannon','Ataque mágico à distância +7, alcance 100 ft.; 18 (4d8) force. O alvo faz salvaguarda de Força CD 15 ou cai Prone.',ataque='+7',alcance='100 ft.',dano=[{'dados':'4d8','tipo':'force'}],salvaguarda='Strength DC 15')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'nota_tatica':'',
 'secoes_nao_listadas':['salvaguardas','resistências de dano','vulnerabilidades de dano','ações bônus','reações','ações lendárias','ações míticas','ações de covil'],
 'fontes_adicionais':[{'titulo':'Índice oficial Kobold Press 5e (nome, variante, Tome of Beasts 2, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},
                      {'titulo':'D&D Grove (transcrição secundária; omite natação no campo Speed)','url':'https://www.dndgrove.com/bestiary/8/ahu-nixta-cataphract'},
                      {'titulo':'Robinloft (transcrição secundária; indica AC natural armor e omite natação)','url':'https://www.robinloft.com/monsters/ahu-nixta-cataphact/tome-of-beasts-2'},
                      {'titulo':'KPOGL, wiki comunitária não endossada pela editora; transcrição secundária com deslocamento de natação','url':'https://kpogl.wikidot.com/monster:ahu-nixta-cataphact'}],
 'classe_fonte':'O índice oficial confirma nome, variante, edição, publicação, porte, tipo e ND. A página 5eSRD associada exige JavaScript; a mecânica foi resumida da wiki comunitária KPOGL, que declara não ser endossada pela Kobold Press. D&D Grove e Robinloft omitem natação; Robinloft também diverge na descrição da CA (natural armor versus clockwork armor). O índice oficial não resolve essas diferenças mecânicas.',
 'completa':True, 'variante':'Ahu-Nixta Cataphract, D&D 5e, Tome of Beasts 2; não confundir com Ahu-Nixta nem Ahu-Nixta Drudge.',
 'url':'https://kpogl.wikidot.com/monster:ahu-nixta-cataphact', 'url_ficha_individual':'https://www.5esrd.com/database/creature/ahu-nixta-cataphract/', 'citation':'turn17view2; turn18view0; turn17view0; turn17view1'
},
'TF-009': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e; metadados confirmados no índice oficial Kobold Press; bloco mecânico consultado em transcrições secundárias.',
 'terreno_fonte':['Badlands','Planar'],
 'porte':'Medium', 'tipo_fonte':'swarm of Tiny aberrations', 'alinhamento':'chaotic evil', 'nd_fonte':'8', 'ca':16, 'ca_base':'natural armor', 'pv':90, 'formula_pv':'12d8 + 36',
 'deslocamento':{'walk_ft':30,'fly_ft':30,'fly_hover':True,'swim_ft':30}, 'scores':[13,16,17,14,16,12],
 'salvaguardas':{'DEX':6,'INT':5}, 'pericias':{'Perception':6,'Stealth':6}, 'resistencias_dano':['bludgeoning','piercing','slashing'], 'imunidades_dano':['poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['grappled','paralyzed','petrified','poisoned','prone','restrained','stunned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':16, 'idiomas':['Deep Speech','Void Speech'], 'bonus_proficiencia':3,
 'bonus_proficiencia_origem':'derivado do ND 8 pela progressão de D&D 5e; não aparece como campo separado nas transcrições consultadas',
 'tracos':[tr('Collective Mind','Os indivíduos que formam o enxame compartilham uma mente. Pode comunicar-se telepaticamente com qualquer serpente individual a até 1 mile e não pode ser surpreendido.'),
          tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e outros efeitos mágicos.'),
          tr('Swarm','Pode ocupar o espaço de outra criatura, e vice-versa, e atravessar qualquer abertura que caiba uma serpente Tiny. Não recupera PV nem recebe PV temporários, exceto por Serpent Spray e Recombine.')],
 'acoes':[act('Multiattack','Faz dois ataques corpo a corpo.'),
          act('Hungering Serpents','Ataque corpo a corpo +7, alcance 0 ft., contra um alvo no espaço do enxame; causa 8 (2d8) piercing e 14 (4d6) poison. Com metade dos PV ou menos, o dano piercing passa a 4 (1d8). A transcrição da página impressa registra média 8 para 2d8; Robinloft calcula 9.',ataque='+7',alcance='0 ft.',dano=[{'dados':'2d8 (ou 1d8 com metade dos PV ou menos)','tipo':'piercing; média impressa 8'},{'dados':'4d6','tipo':'poison'}]),
          act('Serpent Spray (Recharge 6)','Arremessa serpentes astrais. Cada criatura a até 20 ft. faz salvaguarda de Destreza CD 16; sofre 14 (4d6) piercing e 14 (4d6) poison em falha, ou metade do dano em sucesso. Recupera PV iguais ao maior valor individual de dano piercing causado pelo spray.',uso='Recharge 6',salvaguarda='Dexterity DC 16',alcance='20 ft.',dano=[{'dados':'4d6','tipo':'piercing'},{'dados':'4d6','tipo':'poison'}])],
 'acoes_bonus':[],
 'reacoes':[act('Divide','Quando sofre dano bludgeoning, piercing ou slashing e tem ao menos 10 PV, se for Small ou maior pode dividir-se em dois devourers novos. Cada um recebe metade dos PV originais (arredondada para baixo), fica uma categoria de tamanho menor e compartilha mente coletiva com o outro enquanto separados por até 1 mile.'),
             act('Recombine','Quando um ou mais devourers Small ou menores da mesma mente coletiva estão a até 5 ft. entre si, podem combinar-se. A nova criatura fica uma categoria de tamanho maior que a maior forma original e soma os PV; o total não pode exceder o máximo normal de PV de um devourer Medium.')],
 'conjuracao':None,
 'secoes_nao_listadas':['vulnerabilidades de dano','ações bônus','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial Kobold Press 5e','url':'https://koboldpress.com/tools/kobold-press-monsters/'},
                      {'titulo':'Produto oficial Tome of Beasts 2 (5e)','url':'https://koboldpress.com/kpstore/product/tome-of-beasts-2-for-5th-edition-hardcover-pdf/'},
                      {'titulo':'Cópia secundária da página impressa A29','url':'https://fliphtml5.com/rboli/yddi/kobold-press-tome-of-beasts-2-5e2020pdf_compress/32/'},
                      {'titulo':'5eSRD (página individual exige JavaScript)','url':'https://www.5esrd.com/database/creature/astral-devourer/'},
                      {'titulo':'Robinloft (secundária; divergências mecânicas)','url':'https://www.robinloft.com/monsters/astral-devourer/tome-of-beasts-2'}],
 'classe_fonte':'O índice oficial confirma D&D 5e, Tome of Beasts 2, Medium Aberration e ND 8. A mecânica vem de D&D Grove e de cópia secundária da página impressa A29; 5eSRD exige JavaScript. A impressão registra Challenge 8, dano médio 8 e resistências B/P/S sem qualificador; Robinloft diverge (CR 5 próprio, média 9 para 2d8 e resistência só contra ataques não mágicos). Natação 30 ft. aparece na impressão e no resultado indexado 5eSRD, mas é omitida por Grove/Robinloft.',
 'completa':True, 'variante':'Medium swarm of Tiny aberrations, D&D 5e, Tome of Beasts 2; não confundir com outras criaturas chamadas Astral Devourer.',
 'url':'https://www.dndgrove.com/bestiary/8/astral-devourer', 'url_ficha_individual':'https://www.5esrd.com/database/creature/astral-devourer/', 'citation':'turn21view1; turn21view0; turn22view0; turn22view1; turn22search0; turn23view0; turn24view1'
},
'KP-A001': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo KPOGL/5eSRD)',
 'porte':'Huge', 'tipo_fonte':'aberration', 'alinhamento':'lawful neutral', 'nd_fonte':'7', 'ca':15, 'ca_base':'natural armor', 'pv':123, 'formula_pv':'13d12 + 39',
 'deslocamento':{'walk_ft':0,'fly_ft':30,'fly_hover':True}, 'scores':[14,10,16,19,17,17],
 'salvaguardas':{}, 'pericias':{'Arcana':7,'History':7,'Insight':6,'Nature':7,'Perception':6}, 'resistencias_dano':['cold','fire'], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','paralyzed','petrified','poisoned','prone'],
 'sentidos':['blindsight 120 ft. (blind beyond this radius)'], 'percepcao_passiva':16, 'idiomas':['Deep Speech','Undercommon','telepathy 120 ft.'], 'bonus_proficiencia':3,
 'tracos':[tr('False Appearance','Enquanto imóvel, é indistinguível de um cristal gigante.'), tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e outros efeitos mágicos.'), tr('Powerful Mind','Tem vantagem em salvaguardas e testes de Inteligência.'), tr('Innate Spellcasting (Psionics)','Usa Inteligência, CD 15, sem componentes; à vontade detect magic, detect thoughts, mage hand e silent image; 3/dia clairvoyance, hypnotic pattern, stinking cloud e telekinesis; 1/dia confusion, dominate person e suggestion.')],
 'acoes':[act('Multiattack','Faz dois ataques Slam ou dois ataques Mind Spear. Se os dois Slam acertarem uma criatura Grande ou menor, o alvo faz salvaguarda de Constituição CD 14; em falha fica Restrained e depois Petrified até o efeito terminar.'), act('Slam','Ataque corpo a corpo +5, alcance 10 ft.; 11 (2d8+2) bludgeoning.',ataque='+5',alcance='10 ft.',dano=[{'dados':'2d8+2','tipo':'bludgeoning'}]), act('Mind Spear','Ataque mágico à distância +7, alcance 30 ft.; 14 (4d6) psychic.',ataque='+7',alcance='30 ft.',dano=[{'dados':'4d6','tipo':'psychic'}]), act('Psychic Burst (Recharge 5-6)','Cone de 30 ft.; cada criatura faz salvaguarda de Inteligência CD 15. Em falha sofre 28 (8d6) psychic e fica Stunned por 1 minuto; repete a salvaguarda no fim de cada turno.',uso='Recharge 5–6',salvaguarda='Intelligence DC 15',alcance='30-ft. cone',dano=[{'dados':'8d6','tipo':'psychic'}])],
 'acoes_bonus':[], 'reacoes':[],
 'acoes_lendarias':[act('Detect','Faz um teste de Wisdom (Perception).'), act('Teleport','Teleporta-se até 120 ft. para um espaço desocupado que possa ver.',custo='2 legendary actions',alcance='120 ft.'), act('Cast a Spell','Conjura uma magia da lista de Innate Spellcasting, gastando o uso correspondente.',custo='3 legendary actions')],
 'caracteristicas_de_covil':[act('Illusory Duplicate','Na iniciativa 20, cria uma duplicata ilusória; ataques contra ela acertam apenas com resultado 11 ou mais no d20. Uma investigação CD 15 identifica a ilusão. Dura 1 minuto ou até usar esta ação novamente.'), act('Tremor','Na iniciativa 20, criaturas no solo a até 60 ft. fazem salvaguarda de Destreza CD 15 ou ficam Prone; o monólito é imune.'), act('Charged Shards','Na iniciativa 20, até duas criaturas a até 60 ft. são alvo de fragmentos; ataque +3 causa 1d4 piercing e 1d4 psychic.')],
 'conjuracao':None, 'nota_tatica':'',
 'secoes_nao_listadas':['salvaguardas','vulnerabilidades de dano','ações bônus','reações','ações míticas'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'KPOGL, transcrição secundária explicitamente não endossada pela Kobold Press (mecânica)','url':'https://kpogl.wikidot.com/monster:crystalline-monolith'},{'titulo':'Robinloft, transcrição secundária de conferência','url':'https://robinloft.com/monsters/crystalline-monolith'}],
 'classe_fonte':'O índice oficial confirma identidade, Tome of Beasts 2, porte Huge, tipo Aberration e ND 7. A mecânica foi resumida da transcrição KPOGL, que declara não ser publicada, endossada ou aprovada pela Kobold Press; não foi reproduzida integralmente.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 2',
 'url':'https://kpogl.wikidot.com/monster:crystalline-monolith', 'url_ficha_individual':'https://www.5esrd.com/database/creature/crystalline-monolith/', 'citation':'turn5view0; turn10view1; turn7view5'
},
'KP-A002': {
 'fonte_publicacao':'Tome of Beasts 3', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Medium', 'tipo_fonte':'beast', 'alinhamento':'lawful neutral', 'nd_fonte':'6', 'ca':16, 'ca_base':'natural armor', 'pv':105, 'formula_pv':'14d8 + 42',
 'deslocamento':{'walk_ft':30,'swim_ft':30}, 'scores':[18,10,16,6,14,10],
 'salvaguardas':{'STR':7}, 'pericias':{'Athletics':7,'Perception':5,'Stealth':3}, 'resistencias_dano':['bludgeoning, piercing e slashing de ataques não mágicos'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','frightened'],
 'sentidos':['blindsight 30 ft.'], 'percepcao_passiva':15, 'idiomas':["Common (entende, mas não fala)"], 'bonus_proficiencia':3,
 'tracos':[tr('Amphibious','Respira ar e água.')],
 'acoes':[act('Multiattack','Faz três ataques corpo a corpo. Enquanto estiver agarrando uma criatura com duas garras, não pode usar Crustaceous Sword.'), act('Crustaceous Sword','Ataque corpo a corpo +7, alcance 5 ft.; 13 (2d8+4) slashing.',ataque='+7',alcance='5 ft.',dano=[{'dados':'2d8+4','tipo':'slashing'}]), act('Claw','Ataque corpo a corpo +7, alcance 5 ft.; 11 (2d6+4) bludgeoning. O alvo Médio ou menor fica Grappled, escape CD 15. Pode usar cada garra contra apenas um alvo.',ataque='+7',alcance='5 ft.',salvaguarda='escape DC 15',dano=[{'dados':'2d6+4','tipo':'bludgeoning'}])],
 'acoes_bonus':[act('Fighting Stance','Assume uma postura como ação bônus: Banded Claw causa 1d6 bludgeoning a cada criatura agarrada no início do turno do caranguejo; Hard Shell concede +2 CA; Soft Shell dá vantagem ao primeiro ataque de Crustaceous Sword em cada turno.')], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade e catálogo)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha secundária atribuída a Tome of Beasts 3 (mecânica)','url':'https://www.5esrd.com/database/creature/crab-samurai/'}],
 'classe_fonte':'O índice oficial confirma Crab, Samurai, Tome of Beasts 3, Medium Beast e ND 6. A mecânica foi resumida da ficha secundária 5eSRD, que atribui o conteúdo à publicação de 2022.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 3',
 'url':'https://www.5esrd.com/database/creature/crab-samurai/', 'citation':'turn7view0; turn5view0'
},
'KP-A003': {
 'fonte_publicacao':'Tome of Beasts 3', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo D&D Grove)',
 'porte':'Medium', 'tipo_fonte':'celestial', 'alinhamento':'chaotic good', 'nd_fonte':'8', 'ca':16, 'ca_base':'natural armor', 'pv':117, 'formula_pv':'18d8 + 36',
 'deslocamento':{'walk_ft':50,'swim_ft':20}, 'scores':[15,22,14,10,15,19],
 'salvaguardas':{'WIS':5,'CHA':7}, 'pericias':{'Perception':2}, 'resistencias_dano':['poison','radiant'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['paralyzed','poisoned','stunned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':12, 'idiomas':['Celestial','Common'], 'bonus_proficiencia':3,
 'tracos':[tr('Blur of Motion','Se se mover pelo menos 30 ft. no turno, ataques à distância contra ele têm desvantagem até o início do próximo turno.'), tr('Chain Breaker','Causa dano dobrado a objetos que estejam prendendo ou restringindo criaturas.'), tr('Evasion','Se passar em salvaguarda de Destreza que normalmente causaria metade do dano, não sofre dano; se falhar, sofre metade.'), tr('Freedom of Movement','Ignora terreno difícil; magia não reduz seu deslocamento nem o deixa Restrained; gasta apenas 5 ft. para escapar de restraints não mágicos ou Grappled.'), tr('Keen Smell','Tem vantagem em testes de Perception baseados em olfato.'), tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e efeitos mágicos.'), tr('Magic Weapons','Seus ataques são mágicos.'), tr('Pounce','Se mover pelo menos 20 ft. em linha reta até uma criatura e acertar Claw no mesmo turno, o alvo faz salvaguarda de Força CD 15 ou fica Prone; se cair, o Cyonaxin pode fazer Bite como ação bônus.')],
 'acoes':[act('Multiattack','Faz um ataque Bite e dois ataques Claw.'), act('Bite','Ataque corpo a corpo +9, alcance 5 ft.; 16 (3d6+6) piercing mais 10 (3d6) radiant.',ataque='+9',alcance='5 ft.',dano=[{'dados':'3d6+6','tipo':'piercing'},{'dados':'3d6','tipo':'radiant'}]), act('Claw','Ataque corpo a corpo +9, alcance 5 ft.; 13 (3d4+6) slashing.',ataque='+9',alcance='5 ft.',dano=[{'dados':'3d4+6','tipo':'slashing'}]), act('Frightful Yowl (Recharge 6)','Criaturas hostis a até 60 ft. que possam ouvir fazem salvaguarda de Sabedoria CD 15; em falha ficam Frightened por 1 minuto e repetem o teste no fim de cada turno.' ,uso='Recharge 6',salvaguarda='Wisdom DC 15',alcance='60 ft.'), act('Liberating Churr (Recharge 5-6)','Aliados a até 90 ft. que possam ouvir recebem Freedom of Movement e podem usar garras que causam 1d6 + modificador de Força slashing até o início do próximo turno.',uso='Recharge 5–6',alcance='90 ft.')],
 'acoes_bonus':[act('Free Runner','Usa a ação bônus para Dash.')], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'D&D Grove, ficha secundária identificada como Tome of Beasts 3 (mecânica)','url':'https://www.dndgrove.com/bestiary/8/cyonaxin'}],
 'classe_fonte':'O índice oficial confirma Cyonaxin, Tome of Beasts 3, Medium Celestial e ND 8. A mecânica foi resumida da ficha secundária D&D Grove, rotulada como Tome of Beasts 3; não foi reproduzida integralmente.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 3',
 'url':'https://www.dndgrove.com/bestiary/8/cyonaxin', 'citation':'turn7view1; turn5view1'
},
'KP-A004': {
 'fonte_publicacao':'Tome of Beasts 1 (2023 Edition)', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e 2014 (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Huge', 'tipo_fonte':'construct', 'alinhamento':'neutral evil', 'nd_fonte':'8', 'ca':16, 'ca_base':'natural armor', 'pv':161, 'formula_pv':'14d12 + 70',
 'deslocamento':{'walk_ft':30}, 'scores':[21,10,20,6,10,10],
 'salvaguardas':{'STR':8,'CON':8,'DEX':3}, 'pericias':{'Perception':3}, 'resistencias_dano':['cold'], 'imunidades_dano':['fire','poison','psychic'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','exhaustion','frightened','paralyzed','petrified','poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':13, 'idiomas':["entende os idiomas de seu criador; não fala"], 'bonus_proficiencia':3,
 'tracos':[tr('Burning Heart','Emite luz plena em 30 ft. e meia-luz por mais 30 ft.; criaturas dentro da luz plena têm resistência a cold. O efeito está ativo no início de cada turno.'), tr('Construct Nature','Não precisa comer, beber, dormir ou respirar.'), tr('Heated Body','Uma criatura que o toque ou acerte em ataque corpo a corpo a até 5 ft. sofre 1d6 fire.')],
 'acoes':[act('Multiattack','Faz dois ataques Slam; pode substituir um deles por Burning Belly.'), act('Slam','Ataque corpo a corpo +8, alcance 5 ft.; 16 (2d10+5) bludgeoning mais 7 (2d6) fire, e o alvo Grande ou menor fica Grappled, escape CD 16.',ataque='+8',alcance='5 ft.',salvaguarda='escape DC 16',dano=[{'dados':'2d10+5','tipo':'bludgeoning'},{'dados':'2d6','tipo':'fire'}]), act('Burning Belly','Usa um Slam contra criatura que esteja Grappled. Ao acertar, puxa o alvo para dentro do corpo, encerra o Grappled e o deixa Restrained com cobertura de três quartos; sofre 14 (4d6) fire no início de cada turno. Uma criatura pode usar uma ação para sair com teste de Força CD 16; uma criatura que a ajude sofre 2d6 fire.',salvaguarda='escape Strength DC 16',dano=[{'dados':'4d6','tipo':'fire'}]), act('Gout of Flame (Recharge 5-6)','Escolhe ponto a até 100 ft.; criaturas num raio de 10 ft. fazem salvaguarda de Destreza CD 16, sofrendo 35 (10d6) fire em falha ou metade em sucesso.',uso='Recharge 5–6',salvaguarda='Dexterity DC 16',alcance='100 ft.; 10-ft. radius',dano=[{'dados':'10d6','tipo':'fire'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'secoes_nao_listadas':['ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade e catálogo)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atualizada atribuída a Tome of Beasts 1 2023 (mecânica)','url':'https://www.5esrd.com/database/creature/tophet-3pp/'},{'titulo':'Página oficial antiga da Kobold Press, usada apenas para confirmar a arte e não para misturar a mecânica revisada','url':'https://koboldpress.com/tome-of-beasts-tophet/'}],
 'classe_fonte':'O índice oficial confirma Tophet, Tome of Beasts 1, Huge Construct e ND 8. Foi usada a ficha revisada de 2023 hospedada pelo 5eSRD, compatível com os 161 PV do catálogo; a página editorial de 2019 contém um bloco antigo com valores diferentes e não foi misturada.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 1 (2023 Edition)',
 'url':'https://www.5esrd.com/database/creature/tophet-3pp/', 'citation':'turn7view2; turn5view4; turn8view3'
},
'KP-A005': {
 'fonte_publicacao':'Tome of Beasts 1 (2023 Edition)', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e 2014 (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Large', 'tipo_fonte':'dragon', 'alinhamento':'chaotic neutral', 'nd_fonte':'6', 'ca':16, 'ca_base':'natural armor', 'pv':123, 'formula_pv':'13d10 + 52',
 'deslocamento':{'walk_ft':30,'fly_ft':90,'fly_hover':True}, 'scores':[20,16,18,14,13,16],
 'salvaguardas':{'DEX':6,'CON':7,'WIS':4,'CHA':6}, 'pericias':{'Acrobatics':9,'Intimidation':6,'Perception':7,'Stealth':6}, 'resistencias_dano':['cold'], 'imunidades_dano':['lightning'], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['blindsight 30 ft.','darkvision 120 ft.'], 'percepcao_passiva':17, 'idiomas':['Common','Draconic','Primordial'], 'bonus_proficiencia':3,
 'tracos':[tr('Elusive','Tem vantagem em testes e salvaguardas para evitar ou escapar de efeitos que reduzam o deslocamento, causem Grappled ou deixem Restrained.'), tr('Storm Sight','Enxerga através de névoa, nuvens, chuva e outras precipitações sem penalidade.')],
 'acoes':[act('Multiattack','Faz um ataque Bite e dois ataques Claw.'), act('Bite','Ataque corpo a corpo +8, alcance 10 ft.; 16 (2d10+5) piercing.',ataque='+8',alcance='10 ft.',dano=[{'dados':'2d10+5','tipo':'piercing'}]), act('Claw','Ataque corpo a corpo +8, alcance 5 ft.; 12 (2d6+5) slashing.',ataque='+8',alcance='5 ft.',dano=[{'dados':'2d6+5','tipo':'slashing'}]), act('Tempest Breath (Recharge 5-6)','Cone de 30 ft.; cada criatura faz salvaguarda de Força CD 15. Em falha sofre 27 (6d8) bludgeoning, é empurrada 15 ft. e fica Prone; em sucesso sofre metade e não é empurrada nem derrubada. Extingue chamas desprotegidas e pode apagar chamas protegidas com 50% de chance.',uso='Recharge 5–6',salvaguarda='Strength DC 15',alcance='30-ft. cone',dano=[{'dados':'6d8','tipo':'bludgeoning'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'observacao_resolucao':'A API V2 do Open5e retornou 200 para o registro atual, mas seus campos estruturados de deslocamento vieram invertidos (walk 90/fly 30) em relação ao texto da ficha indexada e ao índice oficial; por isso foi usado walk 30/fly 90, sem ocultar a divergência.',
 'secoes_nao_listadas':['ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atualizada atribuída a Tome of Beasts 1 2023 (mecânica e texto de deslocamento)','url':'https://www.5esrd.com/database/creature/dragon-wind-young-3pp/'},{'titulo':'Open5e API v2, conferência estruturada do registro e metadados de publicação','url':'https://open5e.com/api-docs'}],
 'classe_fonte':'O índice oficial confirma Young Wind Dragon, Tome of Beasts 1, Large Dragon e ND 6. A mecânica foi resumida da ficha atualizada 5eSRD e conferida com o registro estruturado Open5e; a divergência de campos de deslocamento da API foi registrada e o texto da ficha prevaleceu.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 1 (2023 Edition)',
 'url':'https://www.5esrd.com/database/creature/dragon-wind-young-3pp/', 'citation':'turn9search0; turn4view0; turn20search0'
},
'KP-A006': {
 'fonte_publicacao':'Tome of Beasts 3', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro; ficha 5eSRD e referência secundária KPOGL)',
 'porte':'Large', 'tipo_fonte':'elemental', 'alinhamento':'neutral', 'nd_fonte':'3', 'ca':14, 'ca_base':'natural armor', 'pv':65, 'formula_pv':'10d10 + 10',
 'deslocamento':{'walk_ft':20,'swim_ft':40,'burrow_ft':20}, 'scores':[17,13,13,13,14,10],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['acid','fire','bludgeoning, piercing e slashing de ataques não mágicos'], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['exhaustion','grappled','paralyzed','petrified','poisoned','prone','restrained','unconscious'],
 'sentidos':['blindsight 30 ft.'], 'percepcao_passiva':12, 'idiomas':['Aquan'], 'bonus_proficiencia':2,
 'tracos':[tr('Elemental Nature','Não precisa de ar, comida, bebida ou sono.'), tr('Invisible in Water','Fica invisível enquanto está totalmente imerso em água.'), tr('Swim in Sand','Pode escavar através de areia usando metade do deslocamento de natação; não pode atacar enquanto está imerso na areia.'), tr('Tidepool Bound','Morre se se afastar mais de 100 ft. das poças de maré às quais está vinculado ou se elas permanecerem sem água por mais de 24 horas.')],
 'acoes':[act('Slam','Ataque corpo a corpo +5, alcance 10 ft.; 16 (3d8 + 3) bludgeoning; o alvo faz salvaguarda de Força CD 13 ou é empurrado até 10 ft.',ataque='+5',alcance='10 ft.',dano=[{'dados':'3d8+3','tipo':'bludgeoning'}],salvaguarda='Strength DC 13'), act('Create Quicksand (3/Day)','Cria uma área de areia movediça de raio 10 ft. e profundidade 5 ft. centrada em ponto visível a até 30 ft. Criatura que começa o turno na área ou entra nela pela primeira vez faz salvaguarda de Força CD 13; em falha fica Grappled. Criatura agarrada repete a salvaguarda no início de cada turno ou afunda 1 ft.; uma criatura Small que afunde 2 ft. ou uma Medium que afunde 3 ft. fica Restrained.',uso='3/day',alcance='30 ft.; 10-ft. radius',salvaguarda='Strength DC 13')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'nota_fonte':'A página 5eSRD consultada expõe identidade, estatísticas e traços, mas omite a seção Actions. A referência KPOGL expõe Slam e Create Quicksand, porém a reabertura direta da página secundária falhou nesta execução; regras posteriores de escape, afundamento completo ou recuperação não foram inferidas. O registro permanece parcial.',
 'secoes_nao_listadas':['ações completas e regras de escape da areia movediça','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 3 (estatísticas e traços)','url':'https://www.5esrd.com/database/creature/beach-weird/'},{'titulo':'KPOGL, transcrição secundária com ações recuperáveis','url':'https://kpogl.wikidot.com/monster%3Abeach-weird'}],
 'classe_fonte':'O índice oficial confirma Beach Weird, Tome of Beasts 3, Large Elemental e ND 3. Estatísticas e traços foram registrados da página 5eSRD; ações recuperáveis foram separadas como referência secundária KPOGL e não elevam o registro a ficha completa.',
 'completa':False, 'variante':'D&D 5e, Tome of Beasts 3',
  'url_ficha_individual':'https://kpogl.wikidot.com/monster%3Abeach-weird', 'url':'https://www.5esrd.com/database/creature/beach-weird/', 'citation':'Kobold Press index; 5eSRD Beach Weird; KPOGL secondary action reference'
},
'KP-A007': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Medium', 'tipo_fonte':'fey', 'alinhamento':'neutral', 'nd_fonte':'2', 'ca':13, 'ca_base':'', 'pv':44, 'formula_pv':'8d8 + 8',
 'deslocamento':{'walk_ft':30,'swim_ft':60}, 'scores':[11,16,12,14,12,17],
 'salvaguardas':{}, 'pericias':{'Perception':3,'Stealth':5}, 'resistencias_dano':['fire'], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['poisoned'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':13, 'idiomas':['Common','Sylvan'], 'bonus_proficiencia':2,
 'tracos':[tr('Crinaea’s Curse','Sente água a até 300 ft. que tenha vindo de sua fonte vinculada nas últimas 24 horas. Como ação bônus, pode envenenar até 1 galão dessa água, inclusive se usada em sopa, chá ou já ingerida nos últimos 30 minutos. A criatura exposta faz salvaguarda de Constituição CD 13; falha causa 18 (4d8) poison e Poisoned por 1 hora, sucesso causa metade sem Poisoned.'), tr('Water-bound Form','Se ficar mais de 24 horas separada da fonte, ganha um nível de Exhaustion e outro a cada dia até se vincular a nova fonte ou morrer. Pode remover os níveis ao terminar um descanso longo submersa na nova fonte.'), tr('Watery Form','Totalmente imersa, fica invisível e pode passar por espaço de até 1 inch sem se espremer.'), tr('Innate Spellcasting','Usa Carisma, CD 13, sem componentes materiais: à vontade poison spray; 3/dia create food and water e purify food and drink apenas para água; 1/dia disguise self, fog cloud e protection from poison.')],
 'acoes':[act('Dagger','Ataque corpo a corpo +5, alcance 5 ft.; 5 (1d4 + 3) piercing mais 7 (2d6) cold.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d4+3','tipo':'piercing'},{'dados':'2d6','tipo':'cold'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':{'atributo':'CHA','cd':13,'ataque_magia':None,'sem_componentes':['material'],'at_will':['poison spray'],'3/day':['create food and water','purify food and drink (water only)'],'1/day':['disguise self','fog cloud','protection from poison']},
 'secoes_nao_listadas':['ações bônus separadas','reações','ações lendárias','ações míticas','ações de covil'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 2','url':'https://www.5esrd.com/database/creature/crinaea/'}],
 'classe_fonte':'O índice oficial confirma Crinaea, Tome of Beasts 2, Medium Fey e ND 2. A página 5eSRD contém traços, conjuração e ação necessários ao resumo mecânico; não foi reproduzida integralmente.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 2',
 'url':'https://www.5esrd.com/database/creature/crinaea/', 'citation':'turn4view7; turn6view1'
},
'KP-A008': {
 'fonte_publicacao':'Tome of Beasts 3', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Large', 'tipo_fonte':'giant', 'alinhamento':'lawful neutral', 'nd_fonte':'4', 'ca':15, 'ca_base':'natural armor', 'pv':90, 'formula_pv':'12d10 + 24',
 'deslocamento':{'walk_ft':40}, 'scores':[18,8,14,17,11,9],
 'salvaguardas':{}, 'pericias':{'Perception':2,'Medicine':2,'Nature':5}, 'resistencias_dano':['cold','fire'], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['poisoned'],
 'sentidos':['darkvision 60 ft.','tremorsense 60 ft.'], 'percepcao_passiva':12, 'idiomas':['Giant'], 'bonus_proficiencia':2,
 'tracos':[tr('False Appearance','Enquanto imóvel, é indistinguível de uma grande geoda.'), tr('Final Form','Ao morrer, o corpo se transforma em cristal e vira um objeto Large atacável e destrutível, CA 17 e 45 PV, imune a poison e psychic; deixa de ser afetado por magias e efeitos que tenham criaturas como alvo.')],
 'acoes':[act('Multiattack','Faz dois ataques Crystal Limb e pode substituir um deles por Biomineralize.'), act('Crystal Limb','Ataque corpo a corpo +6, alcance 10 ft.; 13 (2d8 + 4) piercing. Se o alvo for Medium ou menor, fica impalado e Grappled, escape CD 14; quando a condição termina, sofre 9 (2d8) slashing. Cada um dos dois membros pode agarrar apenas um alvo.',ataque='+6',alcance='10 ft.',dano=[{'dados':'2d8+4','tipo':'piercing'},{'dados':'2d8','tipo':'slashing'}],salvaguarda='escape DC 14'), act('Biomineralize','Uma criatura agarrada faz salvaguarda de Constituição CD 14; sofre 14 (4d6) necrotic em falha ou metade em sucesso. O máximo de PV é reduzido pelo dano e o crystallite recupera a mesma quantidade; a redução dura até descanso longo e mata se reduzir o máximo a 0.',salvaguarda='Constitution DC 14',dano=[{'dados':'4d6','tipo':'necrotic'}]),],
 'acoes_bonus':[], 'reacoes':[act('Calcify','Quando sofre pelo menos 5 de dano em um turno, reduz seu máximo de PV pelo dano sofrido e recebe +1 CA até terminar um descanso longo; não pode elevar a CA acima de 20 com esta reação.')], 'conjuracao':None,
 'secoes_nao_listadas':['ações bônus','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 3','url':'https://www.5esrd.com/database/creature/crystallite/'}],
 'classe_fonte':'O índice oficial confirma Crystallite, Tome of Beasts 3, Large Giant e ND 4. A página 5eSRD contém traits, ações e reação; o conteúdo foi resumido sem transcrição integral.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 3',
 'url':'https://www.5esrd.com/database/creature/crystallite/', 'citation':'turn4view8; turn6view2'
},
'KP-A009': {
 'fonte_publicacao':'Tome of Beasts 1', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro; PDF oficial e ficha 5eSRD)',
 'porte':'Large', 'tipo_fonte':'giant', 'alinhamento':'chaotic evil', 'nd_fonte':'4', 'ca':14, 'ca_base':'natural armor', 'pv':110, 'formula_pv':'13d10 + 39',
 'deslocamento':{'walk_ft':20}, 'scores':[20,6,16,9,13,8],
 'salvaguardas':{'CON':5}, 'pericias':{'Perception':3}, 'resistencias_dano':[], 'imunidades_dano':['poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['poisoned'],
 'sentidos':['passive Perception 13'], 'percepcao_passiva':13, 'idiomas':['Giant','Dwarvish'], 'bonus_proficiencia':2,
 'tracos':[tr('Massive','Não pode usar Dash; ataques e testes para empurrar, derrubar ou agarrar o gigante têm desvantagem contra ele.')],
 'acoes':[act('Multiattack','Faz dois ataques Slam. Se ambos acertarem o alvo, ele fica Grappled, escape CD 15, e o gigante usa Squatting Pin como ação bônus.'), act('Slam','Ataque corpo a corpo +7, alcance 5 ft.; 12 (2d6 + 5) bludgeoning.',ataque='+7',alcance='5 ft.',dano=[{'dados':'2d6+5','tipo':'bludgeoning'}])],
 'acoes_bonus':[act('Squatting Pin','Senta sobre uma criatura agarrada, deixando-a Grappled e Restrained, escape CD 17. Pode atacar outros alvos; as criaturas são libertadas se o gigante se mover. Mantém até duas criaturas Medium ou menores e cada criatura sofre 9 (1d8 + 5) bludgeoning no início de seus turnos enquanto presa.')],
 'reacoes':[], 'conjuracao':None,
 'observacao_resolucao':'A variante do PDF oficial de Tome of Beasts 1 lista Squatting Pin como ação bônus e não limita o alvo por tamanho no Multiattack; a ficha 5eSRD apresenta uma redação revisada que o lista em Actions e explicita Medium ou menor. A variante oficial em PDF foi priorizada. O PDF lista os idiomas Giant e Dwarvish, enquanto a ficha 5eSRD acrescenta Common; o bloco primário foi priorizado. A errata oficial da Kobold Press acrescenta imunidade a dano poison, já incorporada neste resumo.',
 'secoes_nao_listadas':['reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'PDF oficial Kobold Press, trecho de Giant, Flab','url':'https://koboldpress.com/wp-content/uploads/2016/07/Tome-of-Beasts-Flab-Giants.pdf'},{'titulo':'Errata oficial Kobold Press (Giant, Flab)','url':'https://koboldpress.com/errata/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 1','url':'https://www.5esrd.com/database/creature/giant-flab-3pp/'}],
 'classe_fonte':'O índice oficial e o PDF da Kobold Press confirmam Giant, Flab, Tome of Beasts 1, Large Giant e ND 4. A errata editorial foi aplicada para poison; a diferença de idiomas entre o PDF primário e a ficha 5eSRD foi preservada na observação.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 1',
 'url':'https://koboldpress.com/wp-content/uploads/2016/07/Tome-of-Beasts-Flab-Giants.pdf', 'url_ficha_individual':'https://www.5esrd.com/database/creature/giant-flab-3pp/', 'citation':'turn4view9; turn3view5; turn3view6; turn4view1'
},
'KP-A010': {
 'fonte_publicacao':'Tome of Beasts 1', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro; ficha 5eSRD com errata editorial Kobold Press)',
 'porte':'Large', 'tipo_fonte':'giant', 'alinhamento':'neutral evil (50%) ou lawful evil (50%)', 'nd_fonte':'3', 'ca':13, 'ca_base':'chain shirt', 'pv':114, 'formula_pv':'12d10 + 48',
 'deslocamento':{'walk_ft':40}, 'scores':[19,10,18,13,15,11],
 'salvaguardas':{'CON':6}, 'pericias':{'Athletics':6,'Perception':4}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Common','Dwarven','Giant'], 'bonus_proficiencia':2,
 'tracos':[tr('Cast Iron Stomach','Tem vantagem em salvaguardas contra a condição Poisoned.')],
 'acoes':[act('Warhammer','Ataque corpo a corpo +6, alcance 10 ft.; 13 (2d8 + 4) bludgeoning, ou 15 (2d10 + 4) se usado com duas mãos.',ataque='+6',alcance='10 ft.',dano=[{'dados':'2d8+4','tipo':'bludgeoning'},{'dados':'2d10+4 (duas mãos)','tipo':'bludgeoning'}]), act('Rock','Ataque à distância +6, alcance 60/240 ft.; 15 (2d10 + 4) bludgeoning.',ataque='+6',alcance='60/240 ft.',dano=[{'dados':'2d10+4','tipo':'bludgeoning'}]), act('Runic Blood (3/Day)','A errata oficial move esta habilidade para Actions: inscreve a runa thurs em uma arma. Uma criatura atingida sofre 1d8 lightning adicional e não pode usar reações até o início do próximo turno; a runa dura 1 hora ou três acertos, o que ocorrer primeiro.',uso='3/day',dano=[{'dados':'1d8','tipo':'lightning'}])],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'observacao_resolucao':'A página 5eSRD consultada mostra Rock 60/240 e uma versão antiga de Runic Blood como ação bônus, 2d8 e duração de 1 minuto. A errata oficial da Kobold Press substitui essa habilidade: ela fica em Actions, causa 1d8 adicional, impede reações e dura 1 hora ou três acertos; essa versão editorial foi aplicada. Não foi misturada com outras edições.',
 'secoes_nao_listadas':['ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 1','url':'https://www.5esrd.com/database/creature/giant-thursir-3pp/'},{'titulo':'Errata oficial Kobold Press (Giant, Thursir)','url':'https://koboldpress.com/errata/'}],
 'classe_fonte':'O índice oficial confirma Giant, Thursir, Tome of Beasts 1, Large Giant e ND 3. A ficha 5eSRD fornece o bloco base; a errata oficial é a fonte primária para a correção de Runic Blood.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 1 com errata oficial',
 'url':'https://www.5esrd.com/database/creature/giant-thursir-3pp/', 'citation':'turn4view10; turn4view2; turn3view6'
},
'KP-A011': {
 'fonte_publicacao':'Tome of Beasts 3', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Huge', 'tipo_fonte':'ooze', 'alinhamento':'unaligned', 'nd_fonte':'8', 'ca':10, 'ca_base':'', 'pv':142, 'formula_pv':'15d12 + 45',
 'deslocamento':{'walk_ft':20,'climb_ft':20}, 'scores':[18,10,17,4,8,2],
 'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':['piercing','slashing'], 'imunidades_dano':['acid','poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','charmed','deafened','exhaustion','frightened','prone'],
 'sentidos':['blindsight 60 ft. (blind beyond this radius)'], 'percepcao_passiva':9, 'idiomas':[], 'bonus_proficiencia':3,
 'tracos':[tr('Amorphous','Pode atravessar um espaço de apenas 1 inch sem se espremer.'), tr('Ooze Nature','Não precisa dormir.'), tr('Patinated Appearance','Imóvel, parece parte do objeto ou estrutura coberta por tinta verde ou verdete.'), tr('Spider Climb','Pode escalar superfícies difíceis, inclusive tetos, sem teste.')],
 'acoes':[act('Multiattack','Faz três ataques Pseudopod. Ao acertar a mesma criatura com dois, pode deixá-la Grappled (escape CD 15), Restrained e sofrendo 9 (2d8) poison no início de cada turno; só mantém um alvo assim.'), act('Pseudopod','Ataque corpo a corpo +7, alcance 5 ft.; 7 (1d6+4) bludgeoning e 9 (2d8) poison.',ataque='+7',alcance='5 ft.',dano=[{'dados':'1d6+4','tipo':'bludgeoning'},{'dados':'2d8','tipo':'poison'}]), act('Poisonous Snap (somente com Stretch Body; Recharge 5–6)','Ao desfazer o corpo esticado, criaturas a até 10 ft. de qualquer espaço ocupado fazem salvaguarda de Destreza CD 15; falha sofre 27 (6d8) poison e fica coberta de veneno, sucesso sofre metade sem a cobertura. A criatura coberta sofre 9 (2d8) poison no início de cada turno e pode usar uma ação para limpar o veneno.',uso='Recharge 5–6',salvaguarda='Dexterity DC 15',dano=[{'dados':'6d8','tipo':'poison'}])],
 'acoes_bonus':[act('Stretch Body','Estende o corpo pela superfície de objeto Gargantuan ou menor, ou parede, pilar ou estrutura semelhante de até 20 ft. quadrados a até 5 ft.; compartilha o espaço. Pode encerrar a forma como ação bônus e ocupar o espaço livre mais próximo.')],
 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Embosca a partir de paredes, pilares ou objetos cobertos por sua coloração verde e usa Poisonous Snap ao retornar à forma normal.',
 'secoes_nao_listadas':['salvaguardas','perícias','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, publicação, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 3','url':'https://www.5esrd.com/database/creature/copperkill-slime/'}],
 'classe_fonte':'O índice oficial confirma Copperkill Slime, Tome of Beasts 3, Huge Ooze e ND 8. A mecânica foi resumida da ficha hospedada pelo 5eSRD, sem transcrição integral.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 3',
 'url':'https://www.5esrd.com/database/creature/copperkill-slime/', 'citation':'Kobold Press index; 5eSRD Copperkill Slime'
},
'KP-A012': {
 'fonte_publicacao':'Creature Codex', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD; errata oficial aplicada)',
 'porte':'Medium', 'tipo_fonte':'humanoid (bearfolk)', 'alinhamento':'chaotic good', 'nd_fonte':'6', 'ca':17, 'ca_base':'chain shirt, shield', 'pv':130, 'formula_pv':'20d8 + 40',
 'deslocamento':{'walk_ft':40}, 'scores':[21,14,16,9,14,12],
 'salvaguardas':{'DEX':5,'WIS':5}, 'pericias':{'Athletics':11,'Insight':5,'Intimidation':7,'Persuasion':4,'Survival':5}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':12, 'idiomas':['Common','Giant'], 'bonus_proficiencia':3,
 'tracos':[tr('Brute','Ataques com armas corpo a corpo causam um dado adicional de dano quando acertam, já incluído nos ataques.'), tr('Frenzy (1/rest)','Como ação bônus, entra em frenesi por 1 minuto; ganha resistência a bludgeoning, piercing e slashing de ataques não mágicos, tem vantagem em ataques e ataques contra ele têm vantagem.'), tr('Keen Smell','Tem vantagem em testes de Wisdom (Perception) baseados em olfato.')],
 'acoes':[act('Multiattack','Faz dois ataques Battleaxe e um ataque Bite.'), act('Battleaxe','Ataque corpo a corpo +8, alcance 5 ft.; 14 (2d8+5) slashing, ou 16 (2d10+5) se usado com duas mãos.',ataque='+8',alcance='5 ft.',dano=[{'dados':'2d8+5 (ou 2d10+5 com duas mãos)','tipo':'slashing'}]), act('Bite','Ataque corpo a corpo +8, alcance 5 ft.; 12 (2d6+5) piercing.',ataque='+8',alcance='5 ft.',dano=[{'dados':'2d6+5','tipo':'piercing'}]), act('Leadership (recharges after a Short or Long Rest)','Por 1 minuto, usa reação quando uma criatura não hostil a até 30 ft. faz uma jogada de ataque ou salvaguarda; se ouvir e entender, soma 1d4. Uma criatura só recebe um dado de Leadership por vez e o efeito termina se o chieftain ficar incapacitado.',uso='Recharges after a Short or Long Rest'), act('Savage Charge','Depois de mover pelo menos 20 ft. em linha reta e acertar com Battleaxe, o alvo faz salvaguarda de Força CD 15 ou cai Prone; se já estiver Prone, pode fazer Bite como ação bônus.',salvaguarda='Strength DC 15')],
 'acoes_especiais':[act('Alternate Critical','Regra alternativa publicada na ficha: em crítico de Bite, em vez de dano extra, o alvo fica Grappled (escape CD 16); enquanto o mantiver assim, o chieftain não pode usar Leadership.')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
 'observacao_resolucao':'A página 5eSRD exibe salvaguarda de Destreza +4; a errata oficial da Kobold Press altera esse valor para +5, aplicado aqui. A regra Alternate Critical foi preservada como seção separada da ficha.',
 'secoes_nao_listadas':['ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, publicação, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Creature Codex','url':'https://www.5esrd.com/database/creature/bearfolk-chieftain/'},{'titulo':'Errata oficial Kobold Press (Bearfolk Chieftain)','url':'https://koboldpress.com/errata/'}],
 'classe_fonte':'O índice oficial confirma Bearfolk Chieftain, Creature Codex, Medium Humanoid (bearfolk) e ND 6. O bloco mecânico foi resumido da ficha 5eSRD; a errata editorial de Destreza foi aplicada sem misturar outra variante.',
 'completa':True, 'variante':'D&D 5e, Creature Codex com errata oficial',
 'url':'https://www.5esrd.com/database/creature/bearfolk-chieftain/', 'citation':'Kobold Press index; 5eSRD Bearfolk Chieftain; official errata'
},
'KP-A013': {
 'fonte_publicacao':'Tome of Beasts 3', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Medium', 'tipo_fonte':'humanoid (any)', 'alinhamento':'any non-good', 'nd_fonte':'9', 'ca':15, 'ca_base':'Impenetrable Ego', 'pv':149, 'formula_pv':'23d8 + 46',
 'deslocamento':{'walk_ft':30}, 'scores':[10,12,14,12,15,18],
 'salvaguardas':{}, 'pericias':{'Deception':8,'Intimidation':8,'Performance':8,'Persuasion':8}, 'resistencias_dano':['psychic'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':[], 'percepcao_passiva':12, 'idiomas':['any two languages'], 'bonus_proficiencia':4,
 'tracos':[tr('Impenetrable Ego','Enquanto consciente, sem armadura e sem escudo, soma o modificador de Carisma à CA e às salvaguardas; tem vantagem contra Charmed e Frightened.')],
 'acoes':[act('Multiattack','Faz três ataques Psychic Strike; se acertar a mesma criatura com dois, ela faz salvaguarda de Inteligência CD 16 ou fica Stunned até o fim do próximo turno do psychophant.',salvaguarda='Intelligence DC 16'), act('Psychic Strike','Ataque mágico corpo a corpo ou à distância +8, alcance 5 ft. ou alcance 60 ft.; 18 (4d6+4) psychic.',ataque='+8',alcance='5 ft. ou 60 ft.',dano=[{'dados':'4d6+4','tipo':'psychic'}]), act('Brain Storm (Recharge 6)','Cada criatura a até 30 ft. faz salvaguarda de Inteligência CD 16; falha sofre 31 (9d6) psychic e fica Poisoned por 1 minuto, sucesso sofre metade e não fica Poisoned. Repete a salvaguarda ao fim dos turnos.',uso='Recharge 6',salvaguarda='Intelligence DC 16',dano=[{'dados':'9d6','tipo':'psychic'}])],
 'acoes_bonus':[act('Bend the Spoon','Escolhe arma não mágica a até 30 ft. e a entorta magicamente. Se estiver sendo portada, o portador pode impedir com salvaguarda de Wisdom CD 16; caso contrário a arma causa metade do dano e seus ataques têm desvantagem. Mending ou um descanso curto com ferramentas repara a arma.',salvaguarda='Wisdom DC 16')],
 'reacoes':[act('Appeal to the Fervent','Quando uma criatura visível o escolhe como alvo de ataque, troca de lugar com uma criatura aliada a até 5 ft.; a criatura amiga passa a ser o alvo.')],
 'conjuracao':{'atributo':'CHA','cd':16,'ataque_magia':None,'sem_componentes':['material'],'at_will':['detect thoughts','mage hand (invisible hand)','thaumaturgy'],'3/day':['charm person','suggestion'],'1/day':['levitate','telekinesis']},
 'nota_tatica':'Controla o campo pela pressão psíquica, pela manipulação de armas e pela troca defensiva com seguidores.',
 'secoes_nao_listadas':['salvaguardas','ações lendárias','ações míticas','ações de covil'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, publicação, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 3','url':'https://www.5esrd.com/database/creature/npc-psychophant-cultist/'},{'titulo':'Kobold Press — referência narrativa ao Psychophant Cultist','url':'https://koboldpress.com/dark-souls-x-5e-invaders-and-humanity/'}],
 'classe_fonte':'O índice oficial confirma Cultist, Psychophant, Tome of Beasts 3, Medium Humanoid e ND 9. O bloco completo foi recuperado no conteúdo indexado do 5eSRD e resumido em redação própria; a abertura direta da página exigiu JavaScript e essa limitação fica registrada no relatório.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 3',
 'url':'https://www.5esrd.com/database/creature/npc-psychophant-cultist/', 'citation':'Kobold Press index; indexed 5eSRD Psychophant Cultist; Kobold Press article'
},
'KP-A014': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Medium', 'tipo_fonte':'fiend', 'alinhamento':'chaotic evil', 'nd_fonte':'2', 'ca':13, 'ca_base':'', 'pv':38, 'formula_pv':'7d8 + 7',
 'deslocamento':{'walk_ft':30}, 'scores':[10,16,13,14,15,18],
 'salvaguardas':{}, 'pericias':{'Perception':4,'Stealth':7}, 'resistencias_dano':['bludgeoning, piercing e slashing de ataques não mágicos que não sejam de armas prateadas'], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed'],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Abyssal','Elvish','Infernal','Sylvan'], 'bonus_proficiencia':2,
 'tracos':[tr('False Appearance (somente forma de árvore)','Imóvel, parece uma árvore normal.'), tr('Inhabit Tree','Como ação bônus, entra em uma árvore Medium ou maior que não seja criatura. Dentro, tem tremorsense 30 ft., CA 15, deslocamento 0 e vulnerabilidade a fire; ao chegar a 15 PV, a árvore morre e ele aparece a até 5 ft. Pode sair como ação bônus, permanecer no máximo 3 dias e então precisa de outra árvore.'), tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e outros efeitos mágicos.')],
 'acoes':[act('Claw','Ataque corpo a corpo +5, alcance 5 ft.; 6 (1d6+3) slashing; o alvo faz salvaguarda de Constituição CD 13 ou sofre 7 (2d6) poison e fica Poisoned até o fim do próximo turno.',ataque='+5',alcance='5 ft.',dano=[{'dados':'1d6+3','tipo':'slashing'},{'dados':'2d6','tipo':'poison'}],salvaguarda='Constitution DC 13'), act('Vine Whip (somente forma de árvore)','Ataque corpo a corpo +5, alcance 20 ft.; 10 (2d6+3) bludgeoning; alvo Large ou menor fica Grappled (escape CD 13). Pode manter até dois alvos.',ataque='+5',alcance='20 ft.',dano=[{'dados':'2d6+3','tipo':'bludgeoning'}],salvaguarda='escape DC 13'), act('Squeeze (somente forma de árvore)','Faz um ataque Vine Whip contra uma criatura agarrada; se acertar, ela também não respira nem conjura magias com componentes verbais enquanto o grapple durar.')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':None, 'nota_tatica':'Alterna a forma de árvore para emboscada e controle por Vine Whip, usando Claw fora da árvore.',
 'secoes_nao_listadas':['salvaguardas','ações bônus separadas','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, publicação, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 2','url':'https://www.5esrd.com/database/creature/tree-skinner/'}],
 'classe_fonte':'O índice oficial confirma Tree Skinner, Tome of Beasts 2, Medium Fiend e ND 2. A mecânica foi resumida da ficha hospedada pelo 5eSRD, sem transcrição integral.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 2',
 'url':'https://www.5esrd.com/database/creature/tree-skinner/', 'citation':'Kobold Press index; 5eSRD Tree Skinner'
},
'KP-A015': {
 'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
 'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
 'porte':'Tiny', 'tipo_fonte':'fiend', 'alinhamento':'chaotic evil', 'nd_fonte':'1/2', 'ca':15, 'ca_base':'', 'pv':5, 'formula_pv':'2d4',
 'deslocamento':{'walk_ft':10,'fly_ft':30}, 'scores':[2,20,10,12,14,15],
 'salvaguardas':{}, 'pericias':{'Perception':4,'Stealth':7}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
 'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':['Abyssal','Infernal','Primordial','Sylvan'], 'bonus_proficiencia':2,
 'tracos':[tr('Magic Resistance','Tem vantagem em salvaguardas contra magias e outros efeitos mágicos.'), tr('Innate Spellcasting','Usa Carisma, CD 12, +4 para ataques mágicos e não precisa de componentes materiais; à vontade: Vicious Mockery; 1/dia cada: Bestow Curse, Charm Person, Confusion, Detect Thoughts, Dispel Magic, Fire Bolt, Hideous Laughter, Ray of Enfeeblement e Suggestion.')],
 'acoes':[act('Confusion Touch','Toca uma criatura; ela faz salvaguarda de Wisdom CD 12 ou usa a reação para fazer um ataque corpo a corpo contra aliado a até 5 ft.; sem aliado no alcance, ataca a si mesma.',salvaguarda='Wisdom DC 12'), act('Superior Invisibility','Fica invisível até perder a concentração, como se concentrasse em uma magia; o equipamento carregado também fica invisível.')],
 'acoes_bonus':[], 'reacoes':[], 'conjuracao':{'atributo':'CHA','cd':12,'ataque_magia':'+4','sem_componentes':['material'],'at_will':['vicious mockery'],'1/day':['bestow curse','charm person','confusion','detect thoughts','dispel magic','fire bolt','hideous laughter','ray of enfeeblement','suggestion']},
 'nota_tatica':'Usa invisibilidade e magia para induzir ataques entre aliados, preservando a mobilidade aérea.',
 'secoes_nao_listadas':['salvaguardas','ações bônus','reações','ações lendárias','ações míticas','ações de covil'],
 'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, publicação, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 2','url':'https://www.5esrd.com/database/creature/corrupted-pixie/'}],
 'classe_fonte':'O índice oficial confirma Corrupted Pixie, Tome of Beasts 2, Tiny Fiend e ND 1/2. A mecânica foi resumida da ficha hospedada pelo 5eSRD, sem transcrição integral.',
 'completa':True, 'variante':'D&D 5e, Tome of Beasts 2',
 'url':'https://www.5esrd.com/database/creature/corrupted-pixie/', 'citation':'Kobold Press index; 5eSRD Corrupted Pixie'
  },
 'KP-A016': {
  'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
  'sistema':'D&D 5e (conteúdo de terceiro; bloco mecânico consultado em reprodução secundária)',
  'porte':'Huge', 'tipo_fonte':'monstrosity', 'alinhamento':'unaligned', 'nd_fonte':'6', 'ca':15, 'ca_base':'natural armor', 'pv':133, 'formula_pv':'14d10 + 56',
  'deslocamento':{'walk_ft':20,'swim_ft':40}, 'scores':[19,14,18,5,12,5],
  'salvaguardas':{}, 'pericias':{'Perception':4,'Stealth':5}, 'resistencias_dano':[], 'imunidades_dano':[], 'vulnerabilidades_dano':[], 'imunidades_condicao':[],
  'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':14, 'idiomas':[], 'bonus_proficiencia':3,
  'tracos':[tr('Amphibious','Respira ar e água.'), tr('Net Maker','Produz uma rede durante 1 minuto; normalmente mantém duas redes prontas.'), tr('Underwater Camouflage','Tem vantagem em testes de Destreza (Stealth) feitos debaixo d’água.')],
  'acoes':[act('Multiattack','Faz três ataques, escolhendo entre Claw e Net; só pode usar uma Net no Multiattack. Pode substituir dois ataques Claw por Reel.'), act('Claw','Ataque corpo a corpo +7, alcance 10 ft.; 13 (2d8 + 4) bludgeoning e o alvo fica Grappled; escape DC 15.',ataque='+7',alcance='10 ft.',dano=[{'dados':'2d8+4','tipo':'bludgeoning'}],salvaguarda='escape DC 15'), act('Net','Ataque à distância +7, alcance 20/60 ft.; alvo Large ou menor fica Restrained. Pode escapar com teste de Strength DC 15 ou destruir a rede (CA 13; 15 slashing).',ataque='+7',alcance='20/60 ft.',salvaguarda='Strength DC 15'), act('Reel','Puxa até 20 ft. uma criatura Restrained pela própria rede; se terminar a até 10 ft., pode fazer um ataque Claw como ação bônus.')],
  'acoes_bonus':[], 'reacoes':[act('Entangle Weapon','Quando uma criatura o atinge com ataque corpo a corpo enquanto ele tem uma rede livre, ela faz salvaguarda de Destreza CD 16; em falha, o ataque erra.')], 'conjuracao':None,
  'nota_tatica':'A rede é o eixo de controle: o alvo pode ficar Restrained, ser puxado por Reel e receber Claw quando se aproxima.',
  'secoes_nao_listadas':['salvaguardas','ações bônus separadas','ações lendárias','ações míticas','ações de covil','conjuração'],
  'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'Reprodução secundária de Tome of Beasts 2, bloco mecânico de Tidehunter','url':'https://pdfcoffee.com/kobold-press-tome-of-beasts-2-5e2020pdf-pdf-free.html'}],
  'classe_fonte':'O índice oficial confirma Tidehunter, Tome of Beasts 2, Huge Monstrosity e ND 6. O bloco mecânico foi resumido de uma reprodução secundária do livro; a fonte não foi tratada como publicação editorial primária.',
  'completa':True, 'variante':'D&D 5e, Tome of Beasts 2',
  'url_ficha_individual':'https://pdfcoffee.com/kobold-press-tome-of-beasts-2-5e2020pdf-pdf-free.html', 'url':'https://pdfcoffee.com/kobold-press-tome-of-beasts-2-5e2020pdf-pdf-free.html', 'citation':'Kobold Press official monster index; secondary Tome of Beasts 2 reproduction'
 },
 'KP-A017': {
  'fonte_publicacao':'Creature Codex', 'editora_fonte':'Kobold Press / Open Design LLC',
  'sistema':'D&D 5e (conteúdo de terceiro; artigo oficial e bloco mecânico secundário)',
  'porte':'Medium', 'tipo_fonte':'undead', 'alinhamento':'', 'nd_fonte':'6', 'ca':15, 'ca_base':'natural armor', 'pv':68, 'formula_pv':'8d8 + 32',
  'deslocamento':{'walk_ft':0,'fly_ft':60,'fly_hover':True}, 'scores':[17,15,18,3,20,18],
  'salvaguardas':{'DEX':8,'WIS':4,'CHA':2}, 'pericias':{'Perception':1,'Stealth':5}, 'resistencias_dano':['acid','lightning','thunder','bludgeoning, piercing e slashing de ataques não mágicos'], 'imunidades_dano':['cold','necrotic','poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['charmed','exhaustion','frightened','grappled','paralyzed','petrified','poisoned','prone','restrained'],
  'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':11, 'idiomas':['Compreende os idiomas que conhecia em vida; não fala'], 'bonus_proficiencia':3,
  'tracos':[tr('Blood Drinker','Depois de matar uma criatura, fica engorged; se for destruído nesse estado, retorna após uma semana. Se passar um mês sem sangue, fica deprived.'), tr('Pseudocorporeal','A forma de névoa atravessa espaços e objetos conforme a regra da fonte.'), tr('Sanguine Feast','Dano causado pela alimentação reduz o máximo de PV do alvo e cura a névoa pela metade do dano.'), tr('Vampire Weaknesses','A fonte lista forbiddance, running water e sunlight como fraquezas específicas.')],
  'acoes':[act('Engulf','Move-se sobre uma criatura Medium ou menor; ela faz salvaguarda de Destreza CD 15, sofrendo 4d6 necrotic em falha e ficando Restrained dentro da névoa. A criatura não respira enquanto envolvida; pode escapar ou ser removida por força conforme a CD publicada pela fonte.',salvaguarda='Dexterity DC 15',dano=[{'dados':'4d6','tipo':'necrotic'}])],
  'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
  'nota_fonte':'Os valores de atributos e salvaguardas são preservados como apresentados nas referências consultadas, sem recalcular bônus publicados ou converter médias de dano em novos valores.',
  'secoes_nao_listadas':['salvaguardas adicionais além das listadas','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
  'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'Kobold Press, Hungry Undead #5 (identidade e regras centrais)','url':'https://koboldpress.com/hungry-undead-number-5/'},{'titulo':'Bloco mecânico secundário de Crimson Mist','url':'https://www.herebetaverns.com/srd/dnd-5e/monsters/crimson-mist'}],
  'classe_fonte':'O índice e o artigo oficiais da Kobold Press confirmam Crimson Mist, Creature Codex, Medium Undead e ND 6. O artigo oficial fornece a identidade e as regras centrais; os valores estruturados e a ação foram conferidos na referência secundária e resumidos em redação própria.',
  'completa':True, 'variante':'D&D 5e, Creature Codex',
  'url_ficha_individual':'https://www.herebetaverns.com/srd/dnd-5e/monsters/crimson-mist', 'url':'https://koboldpress.com/hungry-undead-number-5/', 'citation':'Kobold Press monster index; Kobold Press Hungry Undead #5; HereBeTaverns secondary block'
 },
 'KP-A018': {
  'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
  'sistema':'D&D 5e (conteúdo de terceiro; bloco mecânico consultado em reprodução secundária)',
  'porte':'Medium', 'tipo_fonte':'undead', 'alinhamento':'lawful evil', 'nd_fonte':'1', 'ca':15, 'ca_base':'natural armor', 'pv':34, 'formula_pv':'4d8 + 16',
  'deslocamento':{'walk_ft':30}, 'scores':[14,13,18,6,8,5],
  'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['cold','poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['exhaustion','poisoned','petrified'],
  'sentidos':['darkvision 60 ft.'], 'percepcao_passiva':9, 'idiomas':['Compreende os idiomas que conhecia em vida; não fala'], 'bonus_proficiencia':2,
  'tracos':[tr('Undead Reanimation','Um humanoide morto pelo corrupter pode levantar-se como outro corrupter após uma semana, salvo se for restaurado ou destruído conforme a regra publicada.')],
  'acoes':[act('Longsword','Ataque corpo a corpo +4, alcance 5 ft.; 6 (1d8 + 2) slashing, ou 7 (1d10 + 2) se usada com duas mãos.',ataque='+4',alcance='5 ft.',dano=[{'dados':'1d8+2','tipo':'slashing'}]), act('Glacial Touch (Recharge 5–6)','Ataque corpo a corpo +4, alcance 5 ft.; 9 (2d6 + 2) cold. Em acerto, o alvo faz salvaguarda de Constituição CD 13; em falha, recebe 1d4 cold no início de cada turno até remover o shard com ação e Medicine DC 12 ou receber cura mágica.',uso='Recharge 5–6',ataque='+4',alcance='5 ft.',dano=[{'dados':'2d6+2','tipo':'cold'}],salvaguarda='Constitution DC 13')],
  'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
  'nota_tatica':'O ataque Glacial Touch cria uma condição persistente; a remoção exige a ação e o teste publicados, salvo cura mágica.',
  'secoes_nao_listadas':['salvaguardas','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
  'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'Reprodução secundária de Tome of Beasts 2, bloco mecânico de Glacial Corrupter','url':'https://pdfcoffee.com/kobold-press-tome-of-beasts-2-5e2020pdf-pdf-free.html'}],
  'classe_fonte':'O índice oficial confirma Glacial Corrupter, Tome of Beasts 2, Medium Undead e ND 1. O bloco mecânico foi resumido de uma reprodução secundária do livro; não foi inventada uma ação ou CD além das regras publicadas ali.',
  'completa':True, 'variante':'D&D 5e, Tome of Beasts 2',
  'url_ficha_individual':'https://pdfcoffee.com/kobold-press-tome-of-beasts-2-5e2020pdf-pdf-free.html', 'url':'https://pdfcoffee.com/kobold-press-tome-of-beasts-2-5e2020pdf-pdf-free.html', 'citation':'Kobold Press official monster index; secondary Tome of Beasts 2 reproduction'
 },
 'KP-A019': {
  'fonte_publicacao':'Tome of Beasts 2', 'editora_fonte':'Kobold Press / Open Design LLC',
  'sistema':'D&D 5e (conteúdo de terceiro hospedado pelo 5eSRD)',
  'porte':'Medium', 'tipo_fonte':'plant', 'alinhamento':'unaligned', 'nd_fonte':'1/2', 'ca':12, 'ca_base':'natural armor', 'pv':32, 'formula_pv':'5d8 + 10',
  'deslocamento':{'walk_ft':20}, 'scores':[12,10,14,1,11,5],
  'salvaguardas':{}, 'pericias':{}, 'resistencias_dano':[], 'imunidades_dano':['acid','poison'], 'vulnerabilidades_dano':[], 'imunidades_condicao':['blinded','deafened','poisoned'],
  'sentidos':['blindsight 60 ft.'], 'percepcao_passiva':10, 'idiomas':[], 'bonus_proficiencia':2,
  'tracos':[tr('Eerie Resemblance','A semelhança com um humanoide pode ser percebida com teste de Nature ou Religion CD 14.'), tr('Spores','Um toque ou ataque que acerte libera esporos; criaturas na área fazem salvaguarda de Constituição CD 10 ou ficam expostas à doença descrita pela fonte.')],
  'acoes':[act('Slam','Ataque corpo a corpo +3, alcance 5 ft.; 3 (1d6 + 1) bludgeoning e 3 (1d6) acid.',ataque='+3',alcance='5 ft.',dano=[{'dados':'1d6+1','tipo':'bludgeoning'},{'dados':'1d6','tipo':'acid'}]), act('Slime Glob','Ataque à distância +2, alcance 20/60 ft.; 3 (1d6) acid. O alvo faz salvaguarda de Constituição CD 12 ou fica infectado conforme a regra da fonte.',ataque='+2',alcance='20/60 ft.',dano=[{'dados':'1d6','tipo':'acid'}],salvaguarda='Constitution DC 12')],
  'acoes_bonus':[], 'reacoes':[], 'conjuracao':None,
  'nota_tatica':'Spores e Slime Glob transmitem a doença/infecção da fonte; a ficha não foi ampliada com efeitos não publicados.',
  'secoes_nao_listadas':['salvaguardas','ações bônus','reações','ações lendárias','ações míticas','ações de covil','conjuração'],
  'fontes_adicionais':[{'titulo':'Índice oficial de monstros da Kobold Press (identidade, edição, porte, tipo e ND)','url':'https://koboldpress.com/tools/kobold-press-monsters/'},{'titulo':'5eSRD, ficha atribuída a Tome of Beasts 2','url':'https://www.5esrd.com/database/creature/crimson-shambler/'},{'titulo':'Reprodução secundária de Tome of Beasts 2','url':'https://pdfcoffee.com/kobold-press-tome-of-beasts-2-5e2020pdf-pdf-free.html'}],
  'classe_fonte':'O índice oficial confirma Crimson Shambler, Tome of Beasts 2, Medium Plant e ND 1/2. As estatísticas, traços e ações foram resumidos da ficha 5eSRD e conferidos com a reprodução secundária, sem transcrição integral.',
  'completa':True, 'variante':'D&D 5e, Tome of Beasts 2',
  'url_ficha_individual':'https://www.5esrd.com/database/creature/crimson-shambler/', 'url':'https://www.5esrd.com/database/creature/crimson-shambler/', 'citation':'Kobold Press official monster index; 5eSRD Crimson Shambler; secondary Tome of Beasts 2 reproduction'
 }
}

CURRENT_BATCH_IDS = ['KP-A006','KP-A016','KP-A017','KP-A018','KP-A019']
CURRENT_REVIEWED_PENDING_IDS = ['KP-A006']
CURRENT_PARTIAL_IDS = ['KP-A006']
CURRENT_COMPLETE_IDS = ['KP-A016','KP-A017','KP-A018','KP-A019']
BLOCKED_PAGES = {
 'TF-010': 'A página individual 5eSRD retornou somente uma mensagem exigindo JavaScript. O índice oficial da Kobold Press confirma Chelicerae, Tome of Beasts 1, ND 7, Large aberration; o bloco mecânico não pôde ser lido. Índice: https://koboldpress.com/tools/kobold-press-monsters/.',
 'TF-011': 'A página individual 5eSRD retornou somente uma mensagem exigindo JavaScript. O índice oficial da Kobold Press confirma Child of Yggdrasil, Creature Codex, ND 6, Large aberration; o bloco mecânico não pôde ser lido. Índice: https://koboldpress.com/tools/kobold-press-monsters/.',
 'TF-024': 'A página individual 5eSRD retornou somente uma mensagem exigindo JavaScript. O índice oficial da Kobold Press confirma Beetle, Lantern, Tome of Beasts 2, ND 0, Tiny beast; o bloco mecânico não pôde ser lido. Índice: https://koboldpress.com/tools/kobold-press-monsters/.',
 'TF-285': 'A página individual 5eSRD retornou somente uma mensagem exigindo JavaScript. O índice oficial da Kobold Press confirma Snallygaster, Tome of Beasts 3, ND 15, Huge aberration, compatível com o catálogo; o bloco mecânico não pôde ser lido. Há outra criatura homônima em Tome of Beasts 1 (ND 10, Large dragon), que não foi usada. Índice: https://koboldpress.com/tools/kobold-press-monsters/.'
}
MISMATCHED_PAGES = {
 'TF-473': 'A página intitulada Flying Lion chama repetidamente a criatura de griffon no Multiattack e no texto de combate; como a identificação das ações é inconsistente, a ficha não foi integrada até haver confirmação da variante correta.',
 'TF-504': "A página intitulada Warlord's Ghost referencia banshee e Baleful Wail como pertencente a banshee no texto de ações e combate; como a identificação/variante fica ambígua, a ficha não foi integrada até confirmação editorial."
}
IMAGE_VERIFIED = {
 'AT-001': {'url':'https://www.dndbeyond.com/avatars/thumbnails/47138/894/1000/1000/638741964160332846.png','page':'https://www.dndbeyond.com/monsters/5195034-gibbering-mouther','publisher':'D&D Beyond; artista não identificado','format':'PNG','dimensions':'1000×799','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'A página da criatura incorpora este mesmo arquivo; a imagem mostra uma massa aberrante de bocas e olhos, compatível com Gibbering Mouther.'},
 'AT-002': {'url':'https://www.dndbeyond.com/avatars/thumbnails/30834/993/1000/1000/638063901980029135.png','page':'https://www.dndbeyond.com/monsters/16999-roper','publisher':'D&D Beyond; artista não identificado','format':'PNG','dimensions':'1000×838','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'A página Roper incorpora este mesmo arquivo; a imagem mostra a criatura cavernosa de múltiplos tentáculos, compatível com Roper.'},
 'AT-124': {'url':'https://www.dndbeyond.com/avatars/thumbnails/30784/568/1000/1000/638062046654629903.png','page':'https://www.dndbeyond.com/monsters/16913-griffon','publisher':'D&D Beyond; artista não identificado','format':'PNG','dimensions':'956×1000','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'A página Griffon incorpora este mesmo arquivo; a figura combina corpo leonino e cabeça e asas de ave.'},
 'TF-015': {'url':'https://a5e.tools/sites/default/files/monsters/Aboleth%20-%20Kim%20Van%20Deun%20copy.jpg','page':'https://a5e.tools/node/2819','publisher':'EN Publishing; Kim Van Deun (identificado no nome do arquivo)','format':'JPEG','dimensions':'650×807','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'A página Aboleth Brute incorpora este mesmo arquivo; a imagem mostra criatura aquática tentaculada, compatível com aboleth.'},
 'TF-088': {'url':'https://a5e.tools/sites/default/files/monsters/dragon%2C%20amethyst%20-%20Gui%20Sommer_0.png','page':'https://a5e.tools/node/1565','publisher':'EN Publishing; Gui Sommer (identificado no nome do arquivo)','format':'PNG','dimensions':'650×460','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'A página Amethyst Dragon Wyrmling incorpora este mesmo arquivo; o dragão roxo corresponde à espécie ametista e à fase wyrmling indicadas.'},
 'TF-095': {'url':'https://a5e.tools/sites/default/files/monsters/dragon%2C%20saphire%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1571','publisher':'EN Publishing; Gui Sommer (identificado no nome do arquivo)','format':'PNG','dimensions':'650×460','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'A página Adult Sapphire Dragon incorpora este mesmo arquivo; o dragão azul em voo corresponde à espécie e à fase adulta indicadas.'},
 'TF-207': {'url':'https://a5e.tools/sites/default/files/monsters/yeti.jpg','page':'https://a5e.tools/node/1826','publisher':'EN Publishing; artista não identificado','format':'JPEG','dimensions':'595×842','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'A página Abominable Snowman incorpora este mesmo arquivo; a criatura branca e peluda no ambiente nevado corresponde ao yeti.'},
 'TF-092': {'url':'https://a5e.tools/sites/default/files/monsters/dragon-earth%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1551','publisher':'EN Publishing; Gui Sommer (identificado no nome do arquivo)','format':'PNG','dimensions':'650×460','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'A página Adult Earth Dragon aponta para este arquivo; a criatura rochosa e quadrúpede corresponde visualmente ao dragão terrestre adulto.'},
 'TF-093': {'url':'https://a5e.tools/sites/default/files/monsters/dragon%2C%20emerald%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1567','publisher':'EN Publishing; Gui Sommer (identificado no nome do arquivo)','format':'PNG','dimensions':'650×460','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'Arquivo da página Adult Emerald Dragon; espécie e variante são estabelecidas pela própria página e pelo nome do arquivo.'},
 'TF-094': {'url':'https://a5e.tools/sites/default/files/monsters/Dragon%2C%20river%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1555','publisher':'EN Publishing; Gui Sommer (identificado no nome do arquivo)','format':'PNG','dimensions':'650×919','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'Arquivo ligado pela página Adult River Dragon; a associação de espécie e variante é feita pela página de origem e pelo nome do arquivo.'},
 'TF-096': {'url':'https://a5e.tools/sites/default/files/monsters/Dragon%2C%20shadow%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1559','publisher':'EN Publishing; Gui Sommer (identificado no nome do arquivo)','format':'PNG','dimensions':'650×856','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'Arquivo ligado pela página Adult Shadow Dragon; a associação de espécie e variante é feita pela página de origem e pelo nome do arquivo.'},
 'TF-098': {'url':'https://a5e.tools/sites/default/files/monsters/dragon-earth%20-%20Gui%20Sommer_0.png','page':'https://a5e.tools/node/1550','publisher':'EN Publishing; Gui Sommer (identificado no nome do arquivo)','format':'PNG','dimensions':'650×460','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'Arquivo da página Ancient Earth Dragon; a associação de espécie e idade vem da página original e do nome do arquivo.'},
 'TF-460': {'url':'https://a5e.tools/sites/default/files/monsters/Ankheg%20copy_0.jpg','page':'https://a5e.tools/node/1463','publisher':'EN Publishing; artista não identificado','format':'JPEG','dimensions':'618×800','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'A página Ankheg Queen liga esta arte de ankheg; a imagem mostra uma criatura insetoide compatível, e a identificação de Queen vem da ficha de origem.'},
 'TF-498': {'url':'https://www.a5e.tools/sites/default/files/monsters/Egil%20Thompson-archfey.jpg','page':'https://www.a5e.tools/node/1606','publisher':'EN Publishing; Egil Thompson (identificado no nome do arquivo)','format':'JPEG','dimensions':'650×841','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'A página Archfey liga a imagem de uma figura feérica alada, compatível com a criatura.'},
 'TF-512': {'url':'https://a5e.tools/sites/default/files/monsters/anzu_0.jpg','page':'https://www.a5e.tools/node/2393','publisher':'EN Publishing; artista não identificado','format':'JPEG','dimensions':'637×471','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'A página Anzû liga este arquivo; a imagem mostra uma grande criatura aviforme compatível com Anzû.'},
 'TF-520': {'url':'https://a5e.tools/sites/default/files/monsters/AliParlagi_Mayday.png','page':'https://a5e.tools/node/5326','publisher':'EN Publishing; Ali Parlagi (nome no arquivo)','format':'PNG','dimensions':'650×488','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/png','visual':'A página Mayday liga a imagem; tentáculos prateados prendem uma nave espacial, correspondendo à criatura e à descrição da ficha.'},
 'TF-016': {'url':'https://a5e.tools/sites/default/files/monsters/Aboleth%20-%20Kim%20Van%20Deun_0.jpg','page':'https://a5e.tools/node/2820','publisher':'EN Publishing; Kim Van Deun (identificado no nome do arquivo)','format':'JPEG','dimensions':'650×807','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'A página Aboleth Fallen Ascendant liga o arquivo; a arte mostra um aboleth aquático. A variante vem da ficha de origem, não de uma diferença visual exclusiva.'},
 'TF-183': {'url':'https://a5e.tools/sites/default/files/monsters/Envious%20-%20Tamara%20Cvetkovic_0.jpg','page':'https://a5e.tools/node/1435','publisher':'EN Publishing; Tamara Cvetkovic (identificado no nome do arquivo)','format':'JPEG','dimensions':'650×919','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'A página Aboleth Thrall liga este arquivo; a arte mostra figura humanoide encapuzada compatível com um thrall humanoide, não um aboleth.'},
 'TF-484': {'url':'https://www.dndbeyond.com/attachments/11/363/goblin.jpg','page':'https://www.dndbeyond.com/posts/1729-creature-roles-how-flee-mortals-helps-you','publisher':'D&D Beyond / MCDM; artista não identificado','format':'JPEG','dimensions':'400×529','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'O artigo oficial que identifica Goblin Assassin acompanha este arquivo; a imagem mostra goblin armado com lâmina, compatível com a variante.'},
 'TF-487': {'url':'https://shop.mcdmproductions.com/cdn/shop/files/Flee_Mortals__Page_138_dab20393-e475-4775-a5e1-3a02b64d661c_2000x.png?v=1773874693','page':'https://shop.mcdmproductions.com/products/flee-mortals-the-mcdm-monster-book-hardcover-pdf','publisher':'MCDM Productions; artista não identificado','format':'WEBP','dimensions':'2000×2637','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/webp','visual':'Prévia oficial de página inteira de Flee, Mortals! que mostra Queen Bargnot, seu bloco e ilustração. É uma página impressa como imagem, não arte isolada.'},
 'TF-488': {'url':'https://pbs.twimg.com/media/GKbfK6-bYAA5dQ7.jpg','page':'https://x.com/ffutureghost/status/1776353497648341411','publisher':'@ffutureghost (atribuição da publicação)','format':'JPEG','dimensions':'1200×861','http':'Carregamento concluído no navegador; código HTTP numérico não exposto','mime':'image/jpeg','visual':'A publicação do artista atribui a arte a War Spider; a imagem mostra uma aranha de guerra com goblins a bordo, compatível com a variante MCDM.'},
 'KP-A002': {'url':'https://koboldpress.com/wp-content/uploads/2022/11/Samurai-Crab.png','page':'https://koboldpress.com/wp-content/uploads/2022/11/','publisher':'Kobold Press; artista não identificado','format':'PNG','dimensions':'1800×2400','date':'2026-10-10','http':'HTTP 200 observado por Invoke-WebRequest em 2026-10-10','mime':'image/png','visual':'Arquivo direto listado no diretório oficial de uploads da Kobold Press; inspeção visual mostra um caranguejo com espada e equipamento samurai, compatível com Crab, Samurai.'},
 'KP-A004': {'url':'https://koboldpress.com/wp-content/uploads/2019/03/tophet-220x300.jpg','page':'https://koboldpress.com/tome-of-beasts-tophet/','publisher':'Kobold Press; artista não identificado','format':'JPEG','dimensions':'220×300','date':'2026-10-10','http':'HTTP 200 observado por Invoke-WebRequest em 2026-10-10','mime':'image/jpeg','visual':'Arquivo direto exposto pela página oficial do Tophet; inspeção visual mostra um constructo metálico/bronzeado com ventre incandescente, compatível com Tophet.'}
}
IMAGE_CANDIDATES = {
 'TF-093': {'url':'https://a5e.tools/sites/default/files/monsters/dragon%2C%20emerald%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1567','artist':'EN Publishing / Gui Sommer','note':'Arquivo exibido no link de imagem da página Adult Emerald Dragon; a URL abre como imagem, mas resposta HTTP, MIME, dimensões e inspeção visual independente não foram verificadas; não promovida a direta confirmada.'},
 'TF-094': {'url':'https://a5e.tools/sites/default/files/monsters/Dragon%2C%20river%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1555','artist':'EN Publishing / Gui Sommer','note':'Arquivo exibido no link de imagem da página Adult River Dragon; a URL abre como imagem, mas resposta HTTP, MIME, dimensões e inspeção visual independente não foram verificadas; não promovida a direta confirmada.'},
 'TF-092': {'url':'https://a5e.tools/sites/default/files/monsters/dragon-earth%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1551','artist':'EN Publishing / Gui Sommer','note':'Link de imagem da ficha Adult Earth Dragon; o visualizador web abriu o arquivo como imagem, mas não forneceu status HTTP, MIME nem dimensões para validação; mantido como candidata.'},
 'TF-096': {'url':'https://a5e.tools/sites/default/files/monsters/Dragon%2C%20shadow%20-%20Gui%20Sommer.png','page':'https://a5e.tools/node/1559','artist':'EN Publishing / Gui Sommer','note':'Link de imagem da ficha Adult Shadow Dragon; o visualizador web abriu o arquivo como imagem, mas não forneceu status HTTP, MIME nem dimensões para validação; mantido como candidata.'},
 'TF-098': {'url':'https://a5e.tools/sites/default/files/monsters/dragon-earth%20-%20Gui%20Sommer_0.png','page':'https://a5e.tools/node/1550','artist':'EN Publishing / Gui Sommer','note':'Link de imagem da ficha Ancient Earth Dragon; o visualizador web abriu o arquivo como imagem, mas não forneceu status HTTP, MIME nem dimensões para validação; mantido como candidata.'},
 'TF-183': {'url':'https://a5e.tools/sites/default/files/monsters/Envious%20-%20Tamara%20Cvetkovic_0.jpg','page':'https://a5e.tools/node/1435','artist':'EN Publishing / Tamara Cvetkovic','note':'A página Aboleth Thrall vincula este arquivo; a tentativa de busca web não conseguiu abri-lo. URL permanece candidata, sem confirmação de acesso, MIME, dimensões ou correspondência visual.'},
 'TF-484': {'url':'https://www.dndbeyond.com/attachments/11/363/goblin.jpg','page':'https://www.dndbeyond.com/posts/1729-creature-roles-how-flee-mortals-helps-you','artist':'D&D Beyond; artista não identificado','note':'Artigo oficial sobre papéis de criaturas MCDM identifica Goblin Assassin junto à arte. A imagem parece representar um goblin, mas falta confirmar acesso HTTP, MIME, dimensões e que a imagem retrata precisamente esta variante; candidata apenas.'},
 'TF-487': {'url':'https://shop.mcdmproductions.com/cdn/shop/files/Flee_Mortals__Page_138_dab20393-e475-4775-a5e1-3a02b64d661c_2000x.png?v=1773874693','page':'https://shop.mcdmproductions.com/products/flee-mortals-the-mcdm-monster-book-hardcover-pdf','artist':'MCDM Productions; artista não identificado','note':'Prévia de página oficial do produto que inclui a seção de Queen Bargnot; URL é candidata a arquivo direto, mas não é arte isolada e requer validação HTTP, MIME, dimensões e correspondência visual.'},
 'TF-488': {'url':'https://pbs.twimg.com/media/GKbfK6-bYAA5dQ7.jpg','page':'https://x.com/ffutureghost/status/1776353497648341411','artist':'@ffutureghost (atribuição da publicação)','note':'Publicação do artista identifica a arte como War Spider MCDM; falta validar status HTTP, MIME, dimensões e abrir o arquivo para confirmar a correspondência visual. Candidata apenas.'},
 'TF-498': {'url':'https://www.a5e.tools/sites/default/files/monsters/Egil%20Thompson-archfey.jpg','page':'https://www.a5e.tools/node/1606','artist':'EN Publishing / Egil Thompson','note':'Link direto de imagem oferecido na página original Archfey; o visualizador exibiu uma fada alada, mas não há confirmação conjunta de HTTP, MIME e dimensões. Mantido como candidata até a validação técnica.'},
 'TF-460': {'url':'https://a5e.tools/sites/default/files/monsters/Ankheg%20copy_0.jpg','page':'https://a5e.tools/node/1463','artist':'EN Publishing; artista não identificado','note':'Imagem direta ligada pela página Ankheg Queen, mas a inspeção preliminar não comprova que a arte distingue visualmente a variante Queen; sem validação de HTTP, MIME ou dimensões, permanece candidata.'},
 'TF-512': {'url':'https://a5e.tools/sites/default/files/monsters/anzu_0.jpg','page':'https://www.a5e.tools/node/2393','artist':'EN Publishing; artista não identificado','note':'Imagem direta ligada pela página oficial de Anzû; o visualizador mostra criatura alada compatível, mas faltam confirmação independente de HTTP, MIME e dimensões.'}
}
IMAGE_CANDIDATES = {k:v for k,v in IMAGE_CANDIDATES.items() if k not in IMAGE_VERIFIED}

# Load and audit the attached package's indices.
data = json.loads(BASE_JSON.read_text(encoding='utf-8-sig'))
base = read_csv(BASE_CSV)
sources = read_csv(SOURCES_CSV)
images = read_csv(IMAGES_CSV)
by_id = {x['id']:x for x in data['fichas']}
base_by_id = {x['ID']:x for x in base}
source_by_id = {x['id']:x for x in sources}
image_by_id = {x['ID']:x for x in images}
assert len(data['fichas']) == 607 and len(by_id) == 607
assert len(base) == len(base_by_id) == 607 and set(by_id) == set(base_by_id)
assert len(images) == len(image_by_id) == 607 and set(by_id) == set(image_by_id)
assert len(sources) == 607 and set(by_id) == set(source_by_id)

# Merge all known references without discarding original rows.
for r in data['fichas']:
    ident = r['id']; b = base_by_id[ident]; s = source_by_id[ident]
    r['status_ficha_pacote'] = r.get('status_ficha','')
    r['url_ficha_individual_conhecida'] = b.get('URL_ficha_individual','') or s.get('url_ficha_individual_verificada','')
    r['url_referencia_catalogo'] = b.get('URL_referencia_ou_candidata','') or s.get('url_referencia','')
    r['source_verification_date'] = DATE if ident in EXTERNAL else ''
    if ident in EXTERNAL:
        m = EXTERNAL[ident]
        r['url_ficha_individual_conhecida'] = m.get('url_ficha_individual',m['url'])
        # Keep catalog stats intact; source-specific facts remain separately labeled.
        r['mecanica_externa_integrada'] = strip_internal_citations({k:v for k,v in m.items() if k not in ('url','url_ficha_individual','citation')})
        r['mecanica_externa_integrada']['atributos'] = ab_scores(m['scores'])
        r['mecanica_externa_integrada'].pop('scores', None)
        dex_mod = mod(m['scores'][1])
        if m.get('iniciativa_fonte'):
            r['mecanica_externa_integrada']['iniciativa'] = {'valor_formatado':m['iniciativa_fonte'],'origem':'listada explicitamente pela fonte'}
        else:
            r['mecanica_externa_integrada']['iniciativa'] = {'modificador_base_des':dex_mod,'valor_formatado':signed(dex_mod),'origem':'derivada do modificador de Destreza; fonte não informa bônus adicional'}
        r['mecanica_externa_integrada']['fonte_url'] = m['url']
        r['mecanica_externa_integrada']['variante'] = m.get('variante') or ('Drudge' if ident == 'TF-002' else 'Não indicada na fonte')
        if m.get('classe_fonte'):
            r['mecanica_externa_integrada']['classe_fonte'] = m['classe_fonte']
        elif m['editora_fonte']=='EN Publishing':
            r['mecanica_externa_integrada']['classe_fonte'] = 'Página de ferramenta da editora; a própria página declara que não é o A5E SRD.'
        elif m['editora_fonte'].startswith('Kobold Press'):
            r['mecanica_externa_integrada']['classe_fonte'] = 'Referência hospedada pelo 5eSRD; bloco atribuído à Kobold Press/Open Design LLC.'
        else:
            r['mecanica_externa_integrada']['classe_fonte'] = 'Prévia oficial publicada pela MCDM Productions.'
        r['mecanica_externa_integrada']['data_verificacao'] = DATE
        covered_sections = ['identidade','porte','tipo','ND','CA','PV e fórmula','deslocamento','atributos e modificadores','salvaguardas','perícias','sentidos','idiomas','defesas','traços','ações','recursos e recargas','CDs e condições']
        for key,label in [('acoes_bonus','ações bônus'),('reacoes','reações'),('acoes_especiais','ações especiais da ficha'),('acoes_de_vilao','ações de vilão'),('acoes_lendarias','ações lendárias'),('acoes_miticas','ações míticas'),('acoes_de_covil','ações de covil'),('caracteristicas_de_covil','características de covil')]:
            if m.get(key): covered_sections.append(label)
        if m.get('conjuracao'): covered_sections.append('conjuração')
        if m.get('equipamento_fonte'): covered_sections.append('equipamento associado descrito na fonte')
        if m.get('efeitos_dependentes'): covered_sections.append('efeitos dependentes e condições referenciadas')
        r['mecanica_externa_integrada']['secoes_cobertas'] = covered_sections
        r['mecanica_externa_integrada']['secoes_nao_listadas_na_fonte'] = m['secoes_nao_listadas']
        r['mecanica_externa_integrada']['transcricao_integral'] = False
        r['mecanica_externa_integrada']['observacao_direitos'] = 'Fatos mecânicos e resumo próprio; sem reprodução integral da redação externa.'
        r['ficha_mecanica_completa'] = m.get('completa', True)
        r['status_ficha'] = 'MECÂNICA INTEGRADA; RESUMO PRÓPRIO DA FONTE' if r['ficha_mecanica_completa'] else 'MECÂNICA PARCIAL; AMBIGUIDADE NA FONTE'
        if m.get('nota_fonte'):
            r['pendencia_ficha_detalhe'] = m['nota_fonte']
        else:
            r.pop('pendencia_ficha_detalhe', None)
        if m.get('observacao_resolucao'):
            r['observacao'] = m['observacao_resolucao']
        r['url_referencia'] = m['url']
        r['nd_fonte_web'] = m['nd_fonte']
        citation = m.get('citation','')
        if re.search(r'\bturn\d+(?:search|view)\d+\b', citation):
            citation = '; '.join(f"{item.get('titulo','Fonte')}: {item.get('url','')}" for item in m.get('fontes_adicionais',[]) if item.get('url')) or m.get('url','')
        r['fonte_citacao_web'] = citation
    else:
        r['ficha_mecanica_completa'] = r.get('status_ficha') == 'FICHA INTEGRAL LOCAL' and bool(r.get('ficha_integral_texto_local'))
        if r['ficha_mecanica_completa']:
            r['status_ficha'] = 'FICHA INTEGRAL LOCAL'
        elif r['url_ficha_individual_conhecida']:
            r['status_ficha'] = 'PÁGINA INDIVIDUAL LOCALIZADA; MECÂNICA A INTEGRAR'
        else:
            r['status_ficha'] = 'PÁGINA INDIVIDUAL NÃO CONFIRMADA; FICHA PENDENTE'
for ident, issue in BLOCKED_PAGES.items():
    by_id[ident]['status_ficha'] = 'PÁGINA INDIVIDUAL LOCALIZADA; LEITURA BLOQUEADA'
    by_id[ident]['pendencia_ficha_detalhe'] = issue
for ident, issue in MISMATCHED_PAGES.items():
    by_id[ident]['status_ficha'] = 'PÁGINA LOCALIZADA; IDENTIDADE/VARIANTE INCONSISTENTE'
    by_id[ident]['pendencia_ficha_detalhe'] = issue

# Preserve original catalog/source fields, then update explicit source facts in the web source index.
for ident,m in EXTERNAL.items():
    s=source_by_id[ident]
    s['CA']=str(m['ca']); s['PV']=str(m['pv']); s['nd_fonte_web']=m['nd_fonte']
    s['url_ficha_individual_verificada']=m.get('url_ficha_individual',m['url'])
    s['status_pesquisa_atualizado']='MECÂNICA INTEGRADA; RESUMO PRÓPRIO DA FONTE' if m.get('completa',True) else 'MECÂNICA PARCIAL; AMBIGUIDADE NA FONTE'
    if m.get('nota_fonte'):
        s['observacao']=m['nota_fonte']
    elif m.get('observacao_resolucao'):
        s['observacao']=m['observacao_resolucao']
    if ident=='TF-442':
        s['observacao']='Fonte A5E indica 66 PV; CSV anterior registrava 76. Valor corrigido na coluna PV e divergência registrada no relatório.'
for ident, issue in BLOCKED_PAGES.items():
    source_by_id[ident]['status_pesquisa_atualizado']='PÁGINA INDIVIDUAL CONHECIDA; LEITURA BLOQUEADA'
    source_by_id[ident]['observacao']=issue
for ident, issue in MISMATCHED_PAGES.items():
    source_by_id[ident]['status_pesquisa_atualizado']='PÁGINA INDIVIDUAL CONHECIDA; IDENTIDADE/VARIANTE INCONSISTENTE'
    source_by_id[ident]['observacao']=issue

# Normalize image status. Promote only candidates with direct-response and visual evidence.
image_rows=[]
for old in images:
    row=dict(old); ident=row['ID']
    candidate_info=IMAGE_CANDIDATES.get(ident,{})
    candidate=(row.get('URL_imagem_candidata','') or candidate_info.get('url','')).strip()
    direct=(row.get('URL_imagem_direta','') or '').strip()
    verified=IMAGE_VERIFIED.get(ident)
    if verified:
        row['URL_imagem_direta']=verified['url']
        row['URL_imagem_candidata']=''
        row['URL_pagina_origem_imagem']=verified['page']
        row['Status']='URL direta carregada no navegador; MIME, dimensões e correspondência visual confirmados; código HTTP numérico indisponível'
        row['Observacao_candidata']=verified['visual']
        row['Data_verificacao']=verified.get('date', IMAGE_VERIFY_DATE)
        row['Status_HTTP']=str(verified['http'])
        row['Tipo_conteudo']=verified['mime']
        row['Dimensoes']=verified['dimensions']
        row['Formato']=verified['format']
        row['Correspondencia_visual']=verified['visual']
        row['Editora_ou_artista']=verified['publisher']
    elif direct:
        candidate = candidate or direct
        row['URL_imagem_candidata']=candidate
        row['URL_imagem_direta']=''
        row['Status']='PENDENTE: URL candidata retornou conteúdo de imagem, mas HTTP/MIME/dimensões e correspondência visual não foram confirmados'
        row['Observacao_candidata']=(row.get('Observacao_candidata','')+'; URL direta anterior preservada como candidata; confirmação incompleta em 2026-10-09').strip('; ')
    elif candidate_info:
        row['URL_imagem_candidata']=candidate
        row['URL_imagem_direta']=''
        row['URL_pagina_origem_imagem']=candidate_info['page']
        row['Status']='PENDENTE: arquivo candidato localizado na página, sem validação técnica completa'
        row['Observacao_candidata']=candidate_info['note']
        row['Editora_ou_artista']=candidate_info['artist']
    else:
        row['Status']='PENDENTE: sem URL direta verificada'
    if not verified:
        row['Data_verificacao']=''
        row['Status_HTTP']=''
        row['Tipo_conteudo']=''
        row['Dimensoes']=''
        row['Formato']=''
        row['Correspondencia_visual']='Não confirmada'
        row['Editora_ou_artista']=candidate_info.get('artist',row.get('Editora',''))
    image_rows.append(row)

# Compute status counts from current records.
local_complete=sum(1 for r in data['fichas'] if r.get('status_ficha')=='FICHA INTEGRAL LOCAL')
external_complete=sum(1 for r in data['fichas'] if r.get('ficha_mecanica_completa') and r.get('status_ficha')!='FICHA INTEGRAL LOCAL')
ficha_pending=607-local_complete-external_complete
known_pages=sum(1 for r in data['fichas'] if r.get('url_ficha_individual_conhecida'))
assert local_complete == 108, local_complete
assert external_complete == 95, external_complete
assert ficha_pending == 404, ficha_pending
assert known_pages == 110, known_pages
known_pages_still_pending=sum(1 for r in data['fichas'] if r.get('url_ficha_individual_conhecida') and not r.get('ficha_mecanica_completa'))
pending_without_page=sum(1 for r in data['fichas'] if not r.get('ficha_mecanica_completa') and not r.get('url_ficha_individual_conhecida'))
assert known_pages_still_pending == 15, known_pages_still_pending
assert pending_without_page == 389, pending_without_page
old_direct=sum(1 for r in images if r.get('URL_imagem_direta','').strip())
assert old_direct == 7, old_direct
assert set(IMAGE_VERIFIED).issubset(set(image_by_id))
verified_images=len(IMAGE_VERIFIED)
image_pending=607-verified_images
# retain the original 607-ID inventory exactly
assert len(data['fichas']) == 607 and len({r['id'] for r in data['fichas']}) == 607

# Structured JSON deliverable.
data['versao']=f'{DATE}-lote-{LOT}'
data['estatisticas']={
 'total_catalogo':607,
 'fichas_integral_local':local_complete,
 'fichas_mecanicamente_integradas_com_fatos_e_resumos_proprios':external_complete,
 'fichas_incompletas':ficha_pending,
 'paginas_individuais_conhecidas_total':known_pages,
 'paginas_individuais_conhecidas_ainda_nao_integradas':known_pages_still_pending,
 'fichas_pendentes_sem_pagina_individual_confirmada':pending_without_page,
 'imagens_diretas_verificadas':verified_images,
 'imagens_com_pendencia':image_pending,
 'urls_diretas_antigas_retestadas':old_direct,
 'urls_diretas_antigas_preservadas_como_candidatas':sum(1 for row in images if row.get('URL_imagem_direta','').strip() and row['ID'] not in IMAGE_VERIFIED),
 'novas_candidatas_nao_verificadas':len(IMAGE_CANDIDATES),
 'ids_unicos':len({r['id'] for r in data['fichas']})
}
data['auditoria_lote']={
 'data':DATE,'lote':LOT,'criterio_ids':'607 IDs do pacote original; sem adicionar registros',
 'registros_com_mecanica_analisada_neste_lote':len(CURRENT_BATCH_IDS),
 'registros_analisados_ids_neste_lote':CURRENT_BATCH_IDS,
 'fichas_completas_integradas_neste_lote':len(CURRENT_COMPLETE_IDS),
 'fichas_completas_integradas_ids_neste_lote':CURRENT_COMPLETE_IDS,
 'fichas_parciais_neste_lote':len(CURRENT_PARTIAL_IDS),
 'fichas_parciais_ids_neste_lote':CURRENT_PARTIAL_IDS,
 'pendencias_parciais_reavaliadas_neste_lote':CURRENT_REVIEWED_PENDING_IDS,
 'fichas_integradas_acumuladas':external_complete,
 'fichas_integradas_ids_acumuladas':sorted(r['id'] for r in data['fichas'] if r.get('ficha_mecanica_completa') and r.get('status_ficha')!='FICHA INTEGRAL LOCAL'),
 'fichas_parciais_ids_acumuladas':sorted(r['id'] for r in data['fichas'] if r.get('mecanica_externa_integrada') and not r.get('ficha_mecanica_completa')),
 'fichas_integradas_paginas_conhecidas_restantes':known_pages_still_pending,
 'fontes_com_leitura_bloqueada':BLOCKED_PAGES,
 'fontes_com_identidade_ou_variante_inconsistente':MISMATCHED_PAGES,
 'divergencias_confirmadas':[{'id':'TF-442','campo':'PV','catalogo_pacote':76,'fonte':66,'acao':'PV fonte atualizado no índice web; valor de catálogo preservado no JSON e divergência anotada.'},{'id':'TF-376','campo':'salvaguardas','atributos_catalogo_fonte':{'INT':7,'CON':10},'salvaguardas_fonte':{'INT':7,'CON':6},'acao':'Valores da página preservados e marcados para confirmação editorial.'},{'id':'KP-A006','campo':'acoes','acao':'A página 5eSRD consultada não expõe Actions; apenas Slam e Create Quicksand foram recuperados da referência secundária KPOGL e o registro permaneceu parcial.'},{'id':'KP-A009','campo':'idiomas','fontes':{'pdf_oficial':['Giant','Dwarvish'],'5eSRD':['Common','Dwarvish','Giant']},'acao':'O PDF oficial foi priorizado; a divergência foi preservada na observação do registro.'},{'id':'KP-A010','campo':'Runic Blood','acao':'A errata oficial substitui a versão 5eSRD: Actions, 1d8 lightning adicional, sem reações e duração de 1 hora ou três acertos.'}],
  'divergencias_resolvidas_neste_lote':[],
  'divergencias_em_fontes_secundarias_neste_lote':[],
 'imagens_confirmadas':verified_images,'imagens_candidatas_retestadas':old_direct,'novas_candidatas_sem_validacao':len(IMAGE_CANDIDATES),
 'observacao_imagens':f'As {verified_images} URLs diretas foram abertas como imagens no navegador; MIME, dimensões e correspondência visual foram conferidos, e o carregamento foi concluído. O visualizador não expõe o código HTTP numérico, registrado como indisponível em cada linha. {len(IMAGE_CANDIDATES)} URLs candidatas continuam pendentes de abertura e/ou validação visual.'
}
for row in image_rows:
    by_id[row['ID']]['referencia_imagem']={
      'url_direta':row.get('URL_imagem_direta',''),
      'url_pagina_original':row.get('URL_pagina_origem_imagem',''),
      'editora_ou_artista':row.get('Editora_ou_artista',''),
      'formato':row.get('Formato',''),
      'dimensoes':row.get('Dimensoes',''),
      'data_verificacao':row.get('Data_verificacao',''),
      'status_http':row.get('Status_HTTP',''),
      'tipo_conteudo':row.get('Tipo_conteudo',''),
      'correspondencia_visual':row.get('Correspondencia_visual',''),
      'status':row.get('Status','')
    }
data['fichas'].sort(key=lambda x:x['id'])
json_path=OUT/'SRD_FICHAS_607.json'
json_path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Helper to add hyperlinks and format documents.
def set_cell_shading(cell, fill):
    tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def set_cell_margins(cell, top=70, start=90, bottom=70, end=90):
    tc=cell._tc; tcPr=tc.get_or_add_tcPr(); tcMar=tcPr.first_child_found_in('w:tcMar')
    if tcMar is None: tcMar=OxmlElement('w:tcMar'); tcPr.append(tcMar)
    for m,v in [('top',top),('start',start),('bottom',bottom),('end',end)]:
        node=tcMar.find(qn('w:'+m))
        if node is None: node=OxmlElement('w:'+m); tcMar.append(node)
        node.set(qn('w:w'),str(v)); node.set(qn('w:type'),'dxa')
def set_repeat_table_header(row):
    trPr=row._tr.get_or_add_trPr(); tblHeader=OxmlElement('w:tblHeader'); tblHeader.set(qn('w:val'),'true'); trPr.append(tblHeader)
def prevent_row_split(row):
    trPr=row._tr.get_or_add_trPr(); cant_split=OxmlElement('w:cantSplit'); trPr.append(cant_split)
def set_table_borders(table):
    tblPr=table._tbl.tblPr; borders=tblPr.first_child_found_in('w:tblBorders')
    if borders is None: borders=OxmlElement('w:tblBorders'); tblPr.append(borders)
    for edge in ('top','left','bottom','right','insideH','insideV'):
        tag='w:'+edge; el=borders.find(qn(tag))
        if el is None: el=OxmlElement(tag); borders.append(el)
        el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'4'); el.set(qn('w:space'),'0'); el.set(qn('w:color'),'D9D9D9')
def add_hyperlink(paragraph, text, url):
    part=paragraph.part; rid=part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
    hyperlink=OxmlElement('w:hyperlink'); hyperlink.set(qn('r:id'),rid)
    new_run=OxmlElement('w:r'); rPr=OxmlElement('w:rPr'); color=OxmlElement('w:color'); color.set(qn('w:val'),'1F4E79'); rPr.append(color)
    underline=OxmlElement('w:u'); underline.set(qn('w:val'),'single'); rPr.append(underline); new_run.append(rPr)
    t=OxmlElement('w:t'); t.text=text; new_run.append(t); hyperlink.append(new_run); paragraph._p.append(hyperlink)
def configure_doc(doc):
    sec=doc.sections[0]; sec.top_margin=Inches(.65); sec.bottom_margin=Inches(.65); sec.left_margin=Inches(.65); sec.right_margin=Inches(.65)
    styles=doc.styles
    styles['Normal'].font.name='Aptos'; styles['Normal'].font.size=Pt(9); styles['Normal'].font.color.rgb=RGBColor(35,35,35)
    styles['Normal'].paragraph_format.space_after=Pt(3)
    for name,size in [('Title',24),('Heading 1',15),('Heading 2',11)]:
        st=styles[name]; st.font.name='Aptos Display'; st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=RGBColor(0,0,0)
        st.paragraph_format.keep_with_next=True
    title_ppr=styles['Title']._element.get_or_add_pPr()
    title_border=title_ppr.find(qn('w:pBdr'))
    if title_border is not None: title_ppr.remove(title_border)
    header=sec.header.paragraphs[0]; header.text=f'SRD CARD GAME  |  Catálogo de referência v{VERSION}'; header.style='Caption'
    for run in header.runs:
        run.font.color.rgb=RGBColor(0,0,0); run.font.size=Pt(8)
    footer=sec.footer.paragraphs[0]; footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run(f'Lote de pesquisa {LOT}  •  {DATE}  •  Página ')
    fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); footer._p.append(fld)
def style_table(table, font_size=7.3):
    table.alignment=WD_TABLE_ALIGNMENT.CENTER; table.autofit=True; set_table_borders(table)
    for ri,row in enumerate(table.rows):
        if ri==0: set_repeat_table_header(row)
        for cell in row.cells:
            set_cell_margins(cell); cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if ri==0: set_cell_shading(cell,'1F4E79')
            elif ri%2==0: set_cell_shading(cell,'F2F6FA')
            for p in cell.paragraphs:
                p.paragraph_format.space_after=Pt(0); p.paragraph_format.space_before=Pt(0)
                for run in p.runs:
                    run.font.name='Aptos'; run.font.size=Pt(font_size)
                    if ri==0: run.font.bold=True; run.font.color.rgb=RGBColor(255,255,255)

def display_ability(m):
    a=m.get('atributos',{})
    return ', '.join(f"{k} {v['valor']} ({signed(v['modificador'])})" for k,v in a.items())
def format_defenses(m):
    pairs=[]
    for label,key in [('Resistências','resistencias_dano'),('Imunidades a dano','imunidades_dano'),('Vulnerabilidades','vulnerabilidades_dano'),('Imunidades a condições','imunidades_condicao')]:
        vals=m.get(key,[])
        if vals: pairs.append(label+': '+', '.join(vals))
    return '; '.join(pairs) if pairs else 'Nenhuma listada na fonte'

def format_movement(movement):
    parts=[]
    for key,value in movement.items():
        if key.endswith('_ft') and isinstance(value,(int,float)) and not isinstance(value,bool):
            label=key[:-3].replace('_',' ')
            if key=='fly_ft' and movement.get('fly_hover') is True:
                label='fly (hover)'
            parts.append(f'{label} {value} ft.')
    return ', '.join(parts) or 'não listado'

def add_mech_detail(doc,r,page_break_before=False):
    m=r['mecanica_externa_integrada']
    heading=doc.add_heading(f"{r['id']}  {r['nome']}",level=2)
    heading.paragraph_format.page_break_before=page_break_before
    p=doc.add_paragraph()
    p.add_run(f"{r.get('tipo_catalogo','')}  |  ND do catálogo {r.get('nd_catalogo','')}  |  Raridade/classificação do catálogo {r.get('raridade','')}  |  Editora {r.get('editora','')}\n").bold=True
    p.add_run(f"Fonte consultada: {m['fonte_publicacao']} — {m['editora_fonte']}. Sistema: {m['sistema'].rstrip('.')} ")
    add_hyperlink(p,'Abrir fonte',m['fonte_url'])
    if m.get('classe_fonte'):
        p=doc.add_paragraph(); p.add_run('Natureza das fontes. ').bold=True; p.add_run(m['classe_fonte'])
    p=doc.add_paragraph(); p.add_run('Situação da ficha. ').bold=True
    p.add_run('Ficha mecânica completa segundo as seções publicadas na fonte.' if r.get('ficha_mecanica_completa') else 'Registro parcial; há ambiguidade mecânica indicada adiante e não foi contado como ficha completa.')
    p=doc.add_paragraph()
    p.add_run('Bloco de combate. ').bold=True
    movement=(f"ambíguo na fonte: {m['deslocamento_fonte_ambiguo']}" if m.get('deslocamento_fonte_ambiguo') else format_movement(m['deslocamento']))
    p.add_run(f"{m['porte']} {m['tipo_fonte']}{(', '+m['alinhamento']) if m.get('alinhamento') else ''}; ND {m['nd_fonte']}; CA {m['ca']} {('('+m['ca_base']+')') if m.get('ca_base') else ''}; PV {m['pv']} ({m['formula_pv']}); deslocamento {movement.rstrip('.')}. ")
    if m.get('terreno_fonte'):
        p.add_run(f"Terrenos indicados pela fonte: {', '.join(m['terreno_fonte'])}. ")
    if m.get('papel_fonte') or m.get('xp_fonte') is not None:
        source_role=f"Função MCDM: {m.get('papel_fonte','não listada')}" if m.get('papel_fonte') else ''
        source_xp=f"XP: {m['xp_fonte']}" if m.get('xp_fonte') is not None else ''
        p.add_run(' '.join(x for x in (source_role,source_xp) if x)+'. ')
    prof_origin=f" ({m['bonus_proficiencia_origem']})" if m.get('bonus_proficiencia_origem') else ''
    if m.get('iniciativa_fonte'):
        p.add_run(f"Iniciativa conforme indicada pela fonte: {m['iniciativa_fonte']}. ")
    else:
        p.add_run(f"Iniciativa base {m['iniciativa']['valor_formatado']} derivada de Destreza. ")
    p.add_run(f"Bônus de proficiência +{m['bonus_proficiencia']}{prof_origin}; Maneuver DC {m.get('maneuver_dc','não informada')}.")
    p=doc.add_paragraph(); p.add_run('Atributos. ').bold=True; p.add_run(display_ability(m))
    p=doc.add_paragraph(); p.add_run('Salvaguardas. ').bold=True; p.add_run(', '.join(f'{k} {signed(v)}' for k,v in m.get('salvaguardas',{}).items()) or 'Nenhuma listada')
    skills=[]
    for k,v in m.get('pericias',{}).items():
        skill=f'{k} {signed(v)}'
        if m.get('pericias_bonus_dado',{}).get(k): skill+=f" (+{m['pericias_bonus_dado'][k]})"
        skills.append(skill)
    p=doc.add_paragraph(); p.add_run('Perícias. ').bold=True; p.add_run(', '.join(skills) or 'Nenhuma listada')
    if m.get('pericias_nao_especificadas'):
        p=doc.add_paragraph(); p.add_run('Nota de perícia da fonte. ').bold=True; p.add_run(m['pericias_nao_especificadas'])
    p=doc.add_paragraph(); p.add_run('Defesas. ').bold=True; p.add_run(format_defenses(m))
    senses='; '.join(m.get('sentidos',[])) or 'nenhum sentido especial listado'
    p=doc.add_paragraph(); p.add_run('Sentidos e idiomas. ').bold=True; p.add_run(f"{senses}; percepção passiva {m.get('percepcao_passiva','não listada')}; idiomas {(', '.join(m.get('idiomas',[])) or 'nenhum listado').rstrip('.')}.")
    if m.get('economia_lendaria'):
        p=doc.add_paragraph(); p.add_run('Economia lendária. ').bold=True; p.add_run(m['economia_lendaria'])
    for heading,key in [('Traços','tracos'),('Ações','acoes'),('Ações bônus','acoes_bonus'),('Reações','reacoes'),('Ações especiais da ficha','acoes_especiais'),('Ações de vilão','acoes_de_vilao'),('Ações lendárias','acoes_lendarias'),('Ações míticas','acoes_miticas'),('Ações de covil','acoes_de_covil'),('Características de covil (não são ações)','caracteristicas_de_covil')]:
        vals=m.get(key,[])
        if vals:
            p=doc.add_paragraph(); p.add_run(heading+':').bold=True
            for x in vals:
                p=doc.add_paragraph(style='List Bullet'); p.paragraph_format.left_indent=Inches(.2); p.paragraph_format.first_line_indent=Inches(-.13)
                p.add_run(x['nome']+'. ').bold=True; p.add_run(x['resumo_mecanico'])
    if m.get('equipamento_fonte'):
        p=doc.add_paragraph(); p.add_run('Equipamento associado descrito pela fonte (não é ação do monstro):').bold=True
        for x in m['equipamento_fonte']:
            p=doc.add_paragraph(style='List Bullet'); p.paragraph_format.left_indent=Inches(.2); p.paragraph_format.first_line_indent=Inches(-.13)
            p.add_run(x['nome']+'. ').bold=True; p.add_run(x['resumo_mecanico'])
    if m.get('efeitos_dependentes'):
        p=doc.add_paragraph(); p.add_run('Efeitos e condições referenciados em outras regras:').bold=True
        for x in m['efeitos_dependentes']:
            p=doc.add_paragraph(style='List Bullet'); p.paragraph_format.left_indent=Inches(.2); p.paragraph_format.first_line_indent=Inches(-.13)
            p.add_run(x['nome']+'. ').bold=True; p.add_run(x['resumo_mecanico'])
            if x.get('fonte_url'):
                p.add_run(' '); add_hyperlink(p,'Fonte da regra',x['fonte_url'])
    if m.get('conjuracao'):
        c=m['conjuracao']; p=doc.add_paragraph(); p.add_run('Conjuração. ').bold=True
        spell_parts=[]
        if c.get('cantrips_at_will'): spell_parts.append('truques à vontade: '+', '.join(c['cantrips_at_will']))
        for k in ('constant','at_will','1/day','1/day each','2/day','3/day','3/day each','5/day'):
            if c.get(k): spell_parts.append(f"{k}: {', '.join(c[k])}")
        if c.get('slots'):
            for level,slot in c['slots'].items(): spell_parts.append(f"{level} ({slot['slots']} espaços): {', '.join(slot['spells'])}")
        p.add_run(f"Atributo {c.get('atributo','não informado')}; nível de conjurador {c.get('nivel_conjurador','não informado')}; CD {c.get('cd','não informada')}; ataque mágico {c.get('ataque_magia') or 'não informado'}; " + (f"tempo de conjuração {c['tempo_conjuracao']}; " if c.get('tempo_conjuracao') else '') + '; '.join(spell_parts) + (f"; componentes {', '.join(c['componentes'])}" if c.get('componentes') else '') + (f"; sem componentes {', '.join(c['sem_componentes'])}" if c.get('sem_componentes') else ''))
        if c.get('detalhes_adicionais'):
            p.add_run('; ' + c['detalhes_adicionais'])
    if m.get('tags'):
        p=doc.add_paragraph(); p.add_run('Tags da fonte. ').bold=True; p.add_run(', '.join(m['tags']))
    if m.get('fontes_adicionais'):
        p=doc.add_paragraph(); p.add_run('Fontes mecânicas adicionais. ').bold=True
        for i,source in enumerate(m['fontes_adicionais']):
            if i: p.add_run('; ')
            add_hyperlink(p,source['titulo'],source['url'])
    if m.get('terreno'):
        p=doc.add_paragraph(); p.add_run('Terreno indicado pela fonte. ').bold=True; p.add_run(', '.join(m['terreno']))
    if m.get('nota_tatica'):
        p=doc.add_paragraph(); p.add_run('Nota tática / observação da fonte. ').bold=True; p.add_run(m['nota_tatica'])
    if m.get('nota_fonte'):
        p=doc.add_paragraph(); p.add_run('Pendência da fonte. ').bold=True; p.add_run(m['nota_fonte'])
    p=doc.add_paragraph(); p.add_run('Escopo da conferência. ').bold=True; p.add_run('Estatísticas, traços e ações presentes na página foram registrados em resumo próprio. Seções não listadas pela fonte: '+(', '.join(m.get('secoes_nao_listadas_na_fonte',[])) or 'nenhuma')+'.')
    p.paragraph_format.space_after=Pt(8)

# Build the comprehensive ficha document.
batch_complete_noun = 'ficha' if len(CURRENT_COMPLETE_IDS)==1 else 'fichas'
batch_complete_adj = 'completa' if len(CURRENT_COMPLETE_IDS)==1 else 'completas'
batch_complete_verb = 'foi' if len(CURRENT_COMPLETE_IDS)==1 else 'foram'
batch_complete_participle = 'integrada' if len(CURRENT_COMPLETE_IDS)==1 else 'integradas'
batch_partial_clause = ('não houve registro parcial neste lote' if len(CURRENT_PARTIAL_IDS)==0 else
                        ('houve 1 registro parcial neste lote' if len(CURRENT_PARTIAL_IDS)==1 else f'houve {len(CURRENT_PARTIAL_IDS)} registros parciais neste lote'))
doc=Document(); configure_doc(doc)
p=doc.add_paragraph(style='Title'); p.add_run('Fichas das 607 criaturas do catálogo')
p=doc.add_paragraph(); p.add_run(f'Versão {VERSION}  |  Lote {LOT}  |  {DATE}').bold=True
reviewed_names=', '.join(f'{ident} {by_id[ident]["nome"]}' for ident in CURRENT_REVIEWED_PENDING_IDS)
reviewed_clause=(f'Foram reavaliadas {len(CURRENT_REVIEWED_PENDING_IDS)} pendências ainda parciais ({reviewed_names}); as lacunas continuam abertas.' if CURRENT_REVIEWED_PENDING_IDS else 'Nenhuma pendência parcial foi reavaliada neste lote.')
p=doc.add_paragraph(f'Este compêndio mantém os 607 IDs do pacote original. Reúne {local_complete} fichas integrais locais e {external_complete} fichas externas cujos fatos mecânicos foram conferidos até esta versão; {len(CURRENT_COMPLETE_IDS)} {batch_complete_noun} {batch_complete_adj} {batch_complete_verb} {batch_complete_participle} neste lote; {batch_partial_clause}. {reviewed_clause} Os outros {ficha_pending} registros permanecem identificados como pendentes; página encontrada não significa ficha integrada.')
p=doc.add_paragraph('Nas fontes externas protegidas, as regras estão resumidas em redação própria. As fichas locais do SRD mantêm o texto integral que já constava no pacote. Cada pendência continua visível no índice e no arquivo de auditoria.')
doc.add_heading('Cobertura deste lote',level=1)
t=doc.add_table(rows=1, cols=2); t.rows[0].cells[0].text='Indicador'; t.rows[0].cells[1].text='Quantidade'
for a,b in [('IDs conferidos no índice','607'),('Fichas integrais locais',str(local_complete)),('Fichas externas integradas neste lote',str(len(CURRENT_COMPLETE_IDS))),('Registros parciais neste lote',str(len(CURRENT_PARTIAL_IDS))),('Pendências parciais reavaliadas neste lote',str(len(CURRENT_REVIEWED_PENDING_IDS))),('Fichas externas integradas acumuladas',str(external_complete)),('Fichas incompletas',str(ficha_pending)),('Páginas individuais conhecidas ainda por integrar',str(known_pages_still_pending)),('Fichas pendentes sem página individual confirmada',str(pending_without_page))]:
    row=t.add_row().cells; row[0].text=a; row[1].text=b
style_table(t,8)
doc.add_heading('Índice por ID',level=1)
p=doc.add_paragraph('As fichas com dados mecânicos registrados aparecem em detalhe depois do índice. Os demais IDs estão listados com fonte e situação atual, sem preencher estatísticas ausentes por suposição.')
t=doc.add_table(rows=1,cols=5)
for c,x in zip(t.rows[0].cells,['ID','Criatura','ND catálogo','Editora','Situação']): c.text=x
for r in data['fichas']:
    row=t.add_row().cells
    row[0].text=r['id']; row[1].text=r['nome']; row[2].text=str(r.get('nd_catalogo','')); row[3].text=str(r.get('editora',''))
    status='Completa local' if r.get('status_ficha')=='FICHA INTEGRAL LOCAL' else ('Mecânica integrada' if r.get('ficha_mecanica_completa') else 'Pendente')
    row[4].text=status
style_table(t,6.8)
doc.add_page_break(); doc.add_heading('Fichas completas locais',level=1)
for r in data['fichas']:
    if r.get('status_ficha')=='FICHA INTEGRAL LOCAL' and r.get('ficha_integral_texto_local'):
        doc.add_heading(f"{r['id']}  {r['nome']}",level=2)
        p=doc.add_paragraph(); p.add_run(f"{r.get('tipo_catalogo','')}  |  ND {r.get('nd_catalogo','')}  |  {r.get('raridade','')}  |  {r.get('editora','')}\n").bold=True
        if r.get('url_referencia'):
            add_hyperlink(p,'Referência',r['url_referencia'])
        text=r['ficha_integral_texto_local']
        for line in text.splitlines():
            if line.strip():
                para=doc.add_paragraph(line.strip()); para.paragraph_format.space_after=Pt(1)
        doc.add_paragraph('')
doc.add_heading('Fichas externas integradas',level=1)
p=doc.add_paragraph('Os registros abaixo preservam a mecânica das páginas consultadas em resumo próprio. O site a5e.tools identifica seu conteúdo como ferramenta e informa que não é o A5E SRD; por isso as fichas A5E não são transcritas integralmente.')
external_detail_index=0
for r in data['fichas']:
    if r.get('mecanica_externa_integrada'):
        add_mech_detail(doc,r,page_break_before=(external_detail_index>0))
        external_detail_index+=1
fichas_path=OUT/'SRD_FICHAS_607_COMPLETAS.docx'; doc.save(fichas_path)
assert zipfile.is_zipfile(fichas_path), f'Ficha DOCX inválida imediatamente após save: {fichas_path.stat().st_size} bytes'

# Image index CSV, UTF-8 with semicolon separator.
img_cols=['ID','Criatura','Editora','Publicacao','Tipo','ND_catalogo','Raridade','URL_imagem_direta','URL_pagina_origem','URL_candidata_nao_verificada','Editora_ou_artista','Formato','Dimensoes','Data_verificacao','Status_HTTP','Tipo_conteudo','Correspondencia_visual','Status_verificacao','Observacoes']
img_rows=[]
for r in data['fichas']:
    old=image_by_id[r['id']]
    verified=IMAGE_VERIFIED.get(r['id'])
    candidate=old.get('URL_imagem_candidata','') or IMAGE_CANDIDATES.get(r['id'],{}).get('url','')
    previously_direct=old.get('URL_imagem_direta','') or ''
    if previously_direct and not verified: candidate=candidate or previously_direct
    if verified: candidate=''
    candidate_info=IMAGE_CANDIDATES.get(r['id'],{})
    sourcepage=(verified['page'] if verified else '') or candidate_info.get('page','') or r.get('url_ficha_individual_conhecida','') or old.get('URL_pagina_origem_imagem','') or old.get('URL_ficha_ou_catalogo','') or r.get('url_referencia_catalogo','')
    status='Pendente: sem imagem direta confirmada'
    note='Sem confirmação conjunta de arquivo, resposta HTTP, tipo MIME, dimensões e correspondência visual.'
    if candidate:
        status='Pendente: URL candidata precisa de validação técnica e visual'
        note='URL previamente cadastrada; a resposta de imagem foi obtida pela pesquisa web, mas status HTTP, cabeçalhos MIME, dimensões e inspeção visual não ficaram disponíveis.'
    if verified:
        status='URL direta carregada; MIME, dimensões e correspondência visual confirmados; código HTTP numérico indisponível'
        note=verified['visual']
    img_rows.append({
      'ID':r['id'],'Criatura':r['nome'],'Editora':r.get('editora',''),'Publicacao':r.get('publicacao',''),'Tipo':r.get('tipo_catalogo',''),'ND_catalogo':r.get('nd_catalogo',''),'Raridade':r.get('raridade',''),
      'URL_imagem_direta':verified['url'] if verified else '','URL_pagina_origem':sourcepage,'URL_candidata_nao_verificada':candidate,'Editora_ou_artista':verified['publisher'] if verified else candidate_info.get('artist',old.get('Editora_ou_artista',r.get('editora',''))),
      'Formato':verified['format'] if verified else '','Dimensoes':verified['dimensions'] if verified else '','Data_verificacao':verified.get('date', IMAGE_VERIFY_DATE) if verified else '','Status_HTTP':str(verified['http']) if verified else '','Tipo_conteudo':verified['mime'] if verified else '','Correspondencia_visual':verified['visual'] if verified else 'Não confirmada','Status_verificacao':status,'Observacoes':candidate_info.get('note',note) if not verified else note
    })
imgcsv=OUT/'SRD_URLS_IMAGENS_607.csv'
with imgcsv.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=img_cols,delimiter=';',lineterminator='\n',quoting=csv.QUOTE_MINIMAL); w.writeheader(); w.writerows(img_rows)

# Image reference document with one row per ID.
imgdoc=Document(); configure_doc(imgdoc)
p=imgdoc.add_paragraph(style='Title'); p.add_run('Referências visuais das 607 criaturas')
p=imgdoc.add_paragraph(); p.add_run(f'Versão {VERSION}  |  Lote {LOT}  |  {DATE}').bold=True
imgdoc.add_paragraph(f'O índice contém os 607 IDs do catálogo. {verified_images} imagens têm URL direta que carregou no navegador, página original, tipo MIME, dimensões e correspondência visual confirmados. O navegador não expõe o código HTTP numérico; essa limitação aparece no campo de status para cada linha. As outras {image_pending} permanecem pendentes; URLs sem validação não foram promovidas a diretas.')
imgdoc.add_heading('Índice por ID',level=1)
t=imgdoc.add_table(rows=1,cols=6)
for c,x in zip(t.rows[0].cells,['ID','Criatura','URL direta verificada','Candidata não verificada','Página original','Situação']): c.text=x
for r in img_rows:
    row=t.add_row().cells
    prevent_row_split(t.rows[-1])
    row[0].text=r['ID']; row[1].text=r['Criatura']; row[2].text=r['URL_imagem_direta'] or '—'
    row[3].text=r['URL_candidata_nao_verificada'] or '—'
    row[4].text=r['URL_pagina_origem'] or '—'
    row[5].text='Verificada' if r['URL_imagem_direta'] else ('Candidata pendente' if r['URL_candidata_nao_verificada'] else 'Sem URL direta')
style_table(t,6.2)
imgdocpath=OUT/'SRD_URLS_IMAGENS_607.docx'; imgdoc.save(imgdocpath)

# Per-ID pending audit.
audit_cols=['ID','Criatura','Editora','Publicacao','ND_catalogo','ND_fonte','Divergencia_ND','Status_ficha','Ficha_mecanica_completa','Pendencia_ficha','URL_ficha_individual','URL_imagem_direta_verificada','URL_imagem_candidata','Status_imagem','Pendencia_imagem','Observacoes_auditoria']
audit=[]
for r in data['fichas']:
    m=r.get('mecanica_externa_integrada')
    old=image_by_id[r['id']]
    image=IMAGE_VERIFIED.get(r['id'])
    candidate='' if image else (old.get('URL_imagem_candidata','') or old.get('URL_imagem_direta','') or IMAGE_CANDIDATES.get(r['id'],{}).get('url',''))
    complete=bool(r.get('ficha_mecanica_completa'))
    ndsrc=m.get('nd_fonte') if m else source_by_id[r['id']].get('nd_fonte_web','')
    nddiv=''
    if ndsrc:
        cr_norm={'1/2':'0.5','1/4':'0.25','1/8':'0.125'}
        nddiv='SIM' if cr_norm.get(str(ndsrc),str(ndsrc)) != cr_norm.get(str(r.get('nd_catalogo','')),str(r.get('nd_catalogo',''))) else 'NÃO'
    fp=''
    if not complete:
        fp=r.get('pendencia_ficha_detalhe') or ('Estatísticas mecânicas não integradas integralmente; página conhecida não prova completude.' if r.get('url_ficha_individual_conhecida') else 'Página individual não confirmada; fonte e ficha completas pendentes.')
    ip='' if image else 'Não há URL direta confirmada com HTTP, MIME, dimensões e correspondência visual.'
    if candidate: ip='URL candidata existente; falta validar HTTP, MIME, dimensões e correspondência visual.'
    note=''
    if r['id']=='TF-442': note='Divergência confirmada: ND igual; PV fonte 66 versus PV anterior no índice web 76.'
    if r['id'] in BLOCKED_PAGES: note=(note+' ' if note else '')+BLOCKED_PAGES[r['id']]
    if r['id'] in MISMATCHED_PAGES: note=(note+' ' if note else '')+MISMATCHED_PAGES[r['id']]
    if r['id']=='TF-376': note=(note+' ' if note else '')+'A página lista Int +7 e Con +6 apesar dos atributos Int 7 e Con 10; confirmar valores publicados.'
    if m and m.get('nota_fonte'): note=(note+' ' if note else '')+m['nota_fonte']
    if m and m.get('observacao_resolucao'): note=(note+' ' if note else '')+m['observacao_resolucao']
    if m: note=(note+' ' if note else '')+f'Ficha integrada em resumo próprio em {DATE}.'
    if image: note=(note+' ' if note else '')+f"Imagem direta validada em {image.get('date', IMAGE_VERIFY_DATE)}; MIME, dimensões e correspondência conferidos; evidência HTTP: {image['http']}."
    audit.append({'ID':r['id'],'Criatura':r['nome'],'Editora':r.get('editora',''),'Publicacao':r.get('publicacao',''),'ND_catalogo':r.get('nd_catalogo',''),'ND_fonte':ndsrc or '', 'Divergencia_ND':nddiv,'Status_ficha':r.get('status_ficha',''),'Ficha_mecanica_completa':'SIM' if complete else 'NÃO','Pendencia_ficha':fp,'URL_ficha_individual':r.get('url_ficha_individual_conhecida',''),'URL_imagem_direta_verificada':image['url'] if image else '','URL_imagem_candidata':candidate,'Status_imagem':'Verificada' if image else 'Pendente','Pendencia_imagem':ip,'Observacoes_auditoria':note})
audit_path=OUT/'SRD_AUDITORIA_PENDENCIAS_607.csv'
with audit_path.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=audit_cols,delimiter=';',lineterminator='\n',quoting=csv.QUOTE_MINIMAL); w.writeheader(); w.writerows(audit)

# Research report.
integrated_ids=sorted(r['id'] for r in data['fichas'] if r.get('ficha_mecanica_completa') and r.get('status_ficha')!='FICHA INTEGRAL LOCAL')
partial_ids=sorted(r['id'] for r in data['fichas'] if r.get('mecanica_externa_integrada') and not r.get('ficha_mecanica_completa'))
integrated_names=', '.join(f"{ident} {by_id[ident]['nome']}" for ident in integrated_ids)
current_names=', '.join(f"{ident} {by_id[ident]['nome']}" for ident in CURRENT_COMPLETE_IDS)
current_partial_names=', '.join(f"{ident} {by_id[ident]['nome']}" for ident in CURRENT_PARTIAL_IDS)
reviewed_pending_names=', '.join(f"{ident} {by_id[ident]['nome']}" for ident in CURRENT_REVIEWED_PENDING_IDS)
complete_noun='ficha' if len(CURRENT_COMPLETE_IDS)==1 else 'fichas'
complete_adj='completa' if len(CURRENT_COMPLETE_IDS)==1 else 'completas'
current_batch_summary=(f"{len(CURRENT_COMPLETE_IDS)} {complete_noun} externa {complete_adj} ({current_names})" if CURRENT_COMPLETE_IDS else 'nenhuma ficha nova concluída')
if CURRENT_PARTIAL_IDS:
    partial_noun='registro parcial' if len(CURRENT_PARTIAL_IDS)==1 else 'registros parciais'
    current_batch_summary += f" e {len(CURRENT_PARTIAL_IDS)} {partial_noun} ({current_partial_names})"
else:
    current_batch_summary += '; nenhuma ficha parcial nova'
partial_summary=' (' + ', '.join(ident + ' ' + by_id[ident]['nome'] for ident in partial_ids) + ')' if partial_ids else ''
partial_label='registro externo parcial acumulado' if len(partial_ids)==1 else 'registros externos parciais acumulados'
integrated_refs='\n'.join(f"- [{ident} {by_id[ident]['nome']} — {EXTERNAL[ident]['editora_fonte']}]({EXTERNAL[ident]['url']})" for ident in integrated_ids)
partial_refs='\n'.join(f"- [{ident} {by_id[ident]['nome']} — {EXTERNAL[ident]['editora_fonte']}]({EXTERNAL[ident]['url']}): {EXTERNAL[ident].get('nota_fonte','') }" for ident in partial_ids)
blocked_refs='\n'.join(f"- {ident} {by_id[ident]['nome']}: {issue} Referência: {by_id[ident]['url_ficha_individual_conhecida']}" for ident,issue in BLOCKED_PAGES.items())
mismatched_refs='\n'.join(f"- {ident} {by_id[ident]['nome']}: {issue} Referência: {by_id[ident]['url_ficha_individual_conhecida']}" for ident,issue in MISMATCHED_PAGES.items())
verified_image_names=', '.join(f"{ident} {by_id[ident]['nome']}" for ident in sorted(IMAGE_VERIFIED))
report=f'''# Relatório de coleta e auditoria do SRD Card Game

**Versão:** {VERSION}  
**Lote:** {LOT}  
**Data:** {DATE}

## Resultado do lote

O pacote original contém 607 IDs únicos e os mesmos 607 IDs aparecem nos índices de fichas e imagens. Nenhum ID foi criado ou removido. Este lote integrou {current_batch_summary}. Há {len(partial_ids)} {partial_label}{partial_summary}; o total de fichas completas acumuladas é {local_complete + external_complete} ({local_complete} locais + {external_complete} externas), entre {known_pages} páginas individuais conhecidas. Restam {known_pages_still_pending} páginas conhecidas incompletas e {pending_without_page} fichas pendentes sem página individual confirmada.

| Situação de ficha | Quantidade |
|---|---:|
| Ficha integral local preservada | {local_complete} |
| Ficha externa completa integrada neste lote | {len(CURRENT_COMPLETE_IDS)} |
| Registro mecânico parcial neste lote | {len(CURRENT_PARTIAL_IDS)} |
| Fichas externas integradas acumuladas | {external_complete} |
| Fichas completas acumuladas | {local_complete + external_complete} |
| Ficha incompleta ou não confirmada | {ficha_pending} |
| Total de IDs | 607 |

## Imagens

As {old_direct} URLs diretas que já estavam no pacote e mais {verified_images-old_direct} imagens encontradas durante a pesquisa foram abertas como arquivos de imagem no navegador. O navegador confirmou carregamento, MIME, dimensões e correspondência visual para: {verified_image_names}. Ele não expõe o código HTTP numérico; esse campo fica explicitamente marcado como indisponível, sem atribuir HTTP 200. Permanecem {len(IMAGE_CANDIDATES)} URLs candidatas e {image_pending} criaturas sem imagem direta confirmada.

| Situação de imagem | Quantidade |
|---|---:|
| URL direta carregada, MIME/dimensões/visual conferidos | {verified_images} |
| Novos arquivos candidatos sem validação | {len(IMAGE_CANDIDATES)} |
| URLs diretas antigas retestadas | {old_direct} |
| Candidatas restantes sem verificação | {sum(1 for row in image_rows if row.get('URL_imagem_candidata',''))} |
| Registros com pendência de imagem | {image_pending} |

## Fichas externas integradas

Fichas integradas até esta versão: {integrated_names}. Para Kobold Press, o índice oficial foi usado para confirmar publicação, edição, porte, tipo e ND; as referências mecânicas são marcadas individualmente como secundárias quando não são páginas editoriais. As páginas A5E pertencem a publicações como Monstrous Menagerie, To Save A Kingdom, Dungeon Delver's Guide e Gate Pass Gazette. O site da EN Publishing informa que suas páginas de ferramentas não são o A5E SRD. Os sete registros MCDM já integrados em lotes anteriores vêm de prévias oficiais de Flee, Mortals! e Where Evil Lives; suas regras próprias de minions e ações de vilão foram preservadas. Por isso, os arquivos armazenam fatos mecânicos e resumos próprios, não uma transcrição integral.

### Conferências adicionais do ciclo operacional 16–20

- **KP-A006 Beach Weird:** o índice oficial confirma Tome of Beasts 3, Large elemental e ND 3. A página 5eSRD foi reaberta para confirmar identidade, estatísticas e traços; a seção Actions não ficou exposta. Slam e Create Quicksand permanecem separados como referência secundária, portanto o registro continua parcial.
- **KP-A016 Tidehunter:** o índice oficial confirma Tome of Beasts 2, Huge monstrosity e ND 6. O bloco mecânico foi resumido de uma reprodução secundária, incluindo Amphibious, Net Maker, Underwater Camouflage, Multiattack, Claw, Net, Reel e a reação Entangle Weapon. Nenhuma imagem direta nova foi validada.
- **KP-A017 Crimson Mist:** o índice e o artigo oficiais da Kobold Press confirmam Creature Codex, Medium undead e ND 6. A ação Engulf e os valores estruturados foram conferidos em uma referência secundária; as apresentações divergentes de modificadores e salvaguardas foram preservadas como publicadas, sem recalcular.
- **KP-A018 Glacial Corrupter:** o índice oficial confirma Tome of Beasts 2, Medium undead e ND 1. O bloco mecânico foi resumido de uma reprodução secundária, incluindo Longsword, Glacial Touch e a regra de reanimação; nenhuma imagem direta nova foi validada.
- **KP-A019 Crimson Shambler:** o índice oficial confirma Tome of Beasts 2, Medium plant e ND 1/2. A ficha 5eSRD e a reprodução secundária forneceram atributos, imunidades, Eerie Resemblance, Spores, Slam e Slime Glob. Nenhuma imagem direta nova foi validada.

## Registros parciais

As seguintes páginas foram lidas e as mecânicas recuperáveis foram resumidas, mas não são contadas como fichas completas porque a própria fonte contém uma regra contraditória ou não resolve um resultado: {partial_refs}

Páginas de referência consultadas:

{integrated_refs}

## Páginas conhecidas sem leitura mecânica nesta tentativa

{blocked_refs}

## Páginas com possível erro de identidade ou variante

{mismatched_refs}

## Divergências e decisões

- **TF-442 Flame-Spitting Statue:** o CSV anterior registrava 76 PV; a página A5E informa 66 PV (7d10 + 28). O valor de fonte foi atualizado no índice de coleta; o registro de catálogo anterior permanece preservado e a diferença está no CSV de auditoria.
- **TF-473 Flying Lion e TF-504 Warlord's Ghost:** divergências de identidade/variante no texto da própria página; não foram contadas como integradas.
- **ND:** os {external_complete} registros integrados coincidem com o ND do catálogo; frações foram normalizadas apenas para comparação.
- **TF-376 Heshgarat Cat:** a página imprime salvaguardas Int +7 e Con +6, embora os atributos sejam Int 7 e Con 10. Os valores publicados foram mantidos e a anomalia foi sinalizada para confirmação editorial.
- **Iniciativa:** quando a fonte não informa iniciativa explicitamente, o JSON registra apenas o modificador base de Destreza como valor derivado, sem bônus adicionais.
- **Ações não listadas:** bônus, reações, ações lendárias, míticas e de covil permanecem como não listadas quando a página não contém tais seções; não foram inventadas.

## Auditoria dos arquivos-base

 O manifesto e os CSVs preservam o total de 607 IDs; a contagem atual é {local_complete} fichas locais completas, {external_complete} fichas externas mecanicamente integradas e {ficha_pending} incompletas. A página conhecida permanece separada da ficha integrada.

## Próximas pendências

1. Resolver as {known_pages_still_pending} páginas individuais conhecidas ainda sem integração mecânica, incluindo dois casos de identidade/variante inconsistente e os bloqueios de leitura já registrados.
2. Localizar e confirmar fontes individuais para as {pending_without_page} fichas pendentes sem página individual confirmada, incluindo MCDM, EN Publishing/A5E e Kobold Press.
3. Validar as {image_pending} imagens restantes por correspondência visual, URL direta, tipo de conteúdo e dimensões; obter o código HTTP numérico, que o visualizador usado não expõe.
4. Reconciliar divergências de ND, variante, publicação e estatísticas em cada lote, mantendo os valores do catálogo e da fonte em campos separados.

## Critério de conclusão do lote

Uma ficha é considerada mecanicamente integrada somente quando a página consultada permite registrar as estatísticas e todas as seções de regras apresentadas. Um link de página, um resultado de busca ou uma URL de imagem não basta para marcar conclusão. As pendências individuais estão no arquivo SRD_AUDITORIA_PENDENCIAS_607.csv.

## Gate de verificação visual dos DOCX

O render_docx.py foi executado para os dois DOCX deste lote, mas a conversão parou porque soffice.exe/LibreOffice não está instalado nem disponível no PATH desta execução. Portanto, a inspeção página a página das imagens renderizadas permanece BLOQUEADA e não é apresentada como concluída. O pacote é um artefato de continuidade com este bloqueio explícito; o supervisor deve repetir a renderização visual antes de aprovar o ciclo.
'''
report_path=OUT/'SRD_RELATORIO_DE_COLETA.md'; report_path.write_text(report,encoding='utf-8')

# Atualized source index with the confirmed mechanical findings of this batch.
source_path=OUT/'SRD_Card_Game_Fichas_607_Fontes_Web_Lote1.csv'
source_cols=list(source_by_id[next(iter(source_by_id))].keys())
with source_path.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=source_cols,delimiter=';',lineterminator='\n',quoting=csv.QUOTE_MINIMAL); w.writeheader(); w.writerows(source_by_id.values())

# Preserve old URLs as candidates only when they have not passed verification.
for row in img_rows:
    ident=row['ID']; old=image_by_id[ident]
    if old.get('URL_imagem_direta','').strip() and ident not in IMAGE_VERIFIED:
        row['URL_candidata_nao_verificada']=old['URL_imagem_direta']
# Re-write image CSV with candidate preservation after JSON normalization.
with imgcsv.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=img_cols,delimiter=';',lineterminator='\n',quoting=csv.QUOTE_MINIMAL); w.writeheader(); w.writerows(img_rows)

# Bundle only requested deliverables, with a versioned archive filename.
zip_path=OUT/f'SRD_FICHAS_IMAGENS_607_v{VERSION}_{DATE}.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in [fichas_path,json_path,imgdocpath,imgcsv,audit_path,report_path,source_path]:
        z.write(p,p.name)

# Final machine checks, including CSV encoding/separator and content counts.
assert len(read_csv(imgcsv))==607
assert len(read_csv(audit_path))==607
assert len(read_csv(source_path))==607
for path in (imgcsv,audit_path):
    raw=path.read_bytes(); assert raw.startswith(b'ID;')
    raw.decode('utf-8')
assert sum(1 for r in img_rows if r['URL_imagem_direta'])==verified_images
assert sum(1 for r in img_rows if r['URL_candidata_nao_verificada'])==len(IMAGE_CANDIDATES)
assert {r['ID'] for r in img_rows if r['URL_candidata_nao_verificada']}==set(IMAGE_CANDIDATES)
with zipfile.ZipFile(zip_path) as z:
    assert len(z.namelist())==7
    assert len(set(z.namelist()))==7
    assert z.testzip() is None
print(json.dumps({'output_dir':str(OUT),'files':[str(x) for x in [fichas_path,json_path,imgdocpath,imgcsv,audit_path,report_path,source_path,zip_path]],'counts':{'ids':607,'local_complete':local_complete,'external_complete':external_complete,'partial_external_records':len(partial_ids),'incomplete_fichas':ficha_pending,'known_pages':known_pages,'known_pages_still_pending':known_pages_still_pending,'pending_without_page':pending_without_page,'verified_images':verified_images,'unverified_image_candidates':len(IMAGE_CANDIDATES),'image_pending':image_pending,'old_image_urls_retested':old_direct}},ensure_ascii=False,indent=2))
