import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from importar_artes_drive import index_source, slug, convert_webp


class ImportadorTests(unittest.TestCase):
    def setUp(self):
        self.cat = {
            "AT-009": {"NOME": "Cat"},
            "AT-010": {"NOME": "Owl"},
            "TF-277": {"NOME": "Shoth, Oth"},
        }

    def test_nome_canonico(self):
        self.assertEqual(slug("Shoth, Oth"), "shoth-oth")

    def test_identidade_e_deduplicacao(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AT-009-cat__candidata-nao-homologada.png").write_bytes(b"imagem-cat")
            (root / "AT-009-cat__candidata-nao-homologada (1).png").write_bytes(b"imagem-cat")
            (root / "AT-010-owl__candidata-nao-homologada.png").write_bytes(b"imagem-owl")
            selected, ignored = index_source(root, self.cat, {"AT-010"})
            self.assertEqual([x[0] for x in selected], ["AT-009"])
            self.assertEqual(ignored["ja_no_manifesto"], 1)

    def test_variantes_diferentes_sao_bloqueadas(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AT-009-cat__candidata-nao-homologada.png").write_bytes(b"variante-a")
            (root / "AT-009-cat__candidata-nao-homologada (2).png").write_bytes(b"variante-b")
            selected, ignored = index_source(root, self.cat, set())
            self.assertEqual(selected, [])
            self.assertEqual(ignored["variantes_visuais_conflitantes"], 1)

    def test_rejeitada_com_mesmo_hash_bloqueia(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AT-009-cat__candidata-nao-homologada.png").write_bytes(b"igual")
            (root / "AT-009-cat__rejeitada-arte-errada.png").write_bytes(b"igual")
            selected, ignored = index_source(root, self.cat, set())
            self.assertEqual(selected, [])
            self.assertEqual(ignored["imagem_tambem_marcada_para_revisao"], 1)

    def test_mesma_imagem_para_duas_criaturas(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AT-009-cat__candidata-nao-homologada.png").write_bytes(b"igual")
            (root / "AT-010-owl__candidata-nao-homologada.png").write_bytes(b"igual")
            selected, ignored = index_source(root, self.cat, set())
            self.assertEqual(selected, [])
            self.assertEqual(ignored["mesma_imagem_para_criaturas_diferentes"], 2)

    def test_conversao_real(self):
        from PIL import Image
        with TemporaryDirectory() as tmp:
            src = Path(tmp) / "entrada.png"
            im = Image.new("RGB", (320, 480))
            im.putdata([((x * 17 + y * 13) % 256,
                         (x * 7 + y * 19) % 256,
                         (x * 23 + y * 3) % 256)
                        for y in range(480) for x in range(320)])
            im.save(src)
            data = convert_webp(src)
            self.assertTrue(data.startswith(b"RIFF"))
            self.assertEqual(data[8:12], b"WEBP")
            self.assertTrue(5000 <= len(data) <= 2_000_000)


if __name__ == "__main__":
    unittest.main()
