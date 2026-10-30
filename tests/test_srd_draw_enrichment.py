import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from srd_draw_enrichment import canonical_model, inspect, reject_private, stage


class TestDrawEnrichment(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        p = self.root / 'docs/catalogo/data'
        p.mkdir(parents=True)
        p.joinpath('megalista-1320.json').write_text(json.dumps({'records': [
            {'NOME':'Model A','ID NO JOGO':'','TIPO':'Humanoide','ND':'3','RARIDADE':'Comum','FONTE':'Livro A'},
            {'NOME':'Berserker','ID NO JOGO':'AT-096','TIPO':'Humanoide','ND':'2','RARIDADE':'Comum','FONTE':'SRD'}
        ]}),encoding='utf-8')
        p.joinpath('fichas-607.json').write_text(json.dumps({'fichas':[
            {'id':'AT-096','nome':'Berserker','status_ficha':'FICHA INTEGRAL LOCAL','ficha_integral_texto_local':'Texto real'}
        ]}),encoding='utf-8')
    def tearDown(self):
        self.tmp.cleanup()
    def test_ml_resolves_by_position(self):
        self.assertEqual(canonical_model(self.root, 'ML-0001')['name'], 'Model A')
    def test_reject_alternative_ml_when_catalogue_id_exists(self):
        with self.assertRaises(ValueError):canonical_model(self.root,'ML-0002')
    def test_missing_produces_three_independent_tasks(self):
        data=inspect(self.root,'ML-0001')
        self.assertEqual([x['kind'] for x in data['tasks']], ['GENERATE_IMAGE','RESEARCH_5E_STATBLOCK','DERIVE_SUPPORT_FROM_REAL_ABILITY'])
        self.assertNotIn('hand',json.dumps(data))
    def test_no_auto_homologation_or_game_state(self):
        data=inspect(self.root,'AT-096')
        self.assertTrue(data['statblock']['full_verified'])
        self.assertFalse(data['support']['approved'])
        self.assertFalse(data['draw_state_changed'])
    def test_existing_image_prevents_duplicate_generation(self):
        p=self.root/'operational/assets/creature-images'
        p.mkdir(parents=True)
        (p/'AT-096.webp').write_bytes(b'fake-picture-nonzero')
        self.assertNotIn('GENERATE_IMAGE',[t['kind'] for t in inspect(self.root,'AT-096')['tasks']])
    def test_private_metadata_is_rejected(self):
        with self.assertRaises(ValueError):reject_private({'model_id':'ML-0001','hand':['private']})
        with self.assertRaises(ValueError):reject_private({'support':{'copy_id':'private'}})
    def test_candidate_stage_and_inspect(self):
        incoming=self.root/'proposal.json'
        incoming.write_text(json.dumps({'model_id':'ML-0001','canonical_name':'Model A','status':'PENDENTE_HOMOLOGACAO','support':{'status':'CANDIDATA_NAO_HOMOLOGADA','approved':False,'category':'Buff','source_ability':'Real Ability'}}),encoding='utf-8')
        paths=stage(self.root,'ML-0001',incoming,None)
        self.assertEqual(paths,['operational/research/creature-candidates/ML-0001.json'])
        info=inspect(self.root,'ML-0001')
        self.assertTrue(info['support']['present'])
        self.assertIn('REVIEW_SUPPORT',[t['kind'] for t in info['tasks']])
    def test_cannot_stage_approved_support(self):
        incoming=self.root/'proposal.json'
        incoming.write_text(json.dumps({'model_id':'ML-0001','canonical_name':'Model A','status':'PENDENTE_HOMOLOGACAO','support':{'status':'CANDIDATA_NAO_HOMOLOGADA','approved':True,'category':'Buff','source_ability':'Ability'}}),encoding='utf-8')
        with self.assertRaises(ValueError):stage(self.root,'ML-0001',incoming,None)
    def test_mismatched_id_name_rejected(self):
        with self.assertRaises(ValueError):inspect(self.root,'ML-0001','Different')
    def test_copy_id_not_accepted_as_model_id(self):
        with self.assertRaises(ValueError):canonical_model(self.root,'SIM-B01-C1')


if __name__=='__main__':unittest.main()