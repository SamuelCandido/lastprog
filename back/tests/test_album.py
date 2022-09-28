import unittest

from config import db
from modelos import moeda


class TestAlbum(unittest.TestCase):
    def test_doenca(self):
        d1 = Doenca(nome="TesteDeDoenca", sintomas="N sei")
        db.session.add(d1)
        db.session.commit()

        d1 = Doenca.query.filter_by(nome="TesteDeDoenca").first()
        self.assertEqual(d1.nome, "TesteDeDoenca")
        self.assertEqual(d1.sintomas, "N sei")

        db.session.delete(d1)
        db.session.commit()