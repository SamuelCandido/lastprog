import unittest

from config import db
from modelos import Moeda


class TestCoin(unittest.TestCase):
    def test_doenca(self):
        m1 = Moeda(nome="TesteDeMoeda", descricao="Foi?")
        db.session.add(m1)
        db.session.commit()

        m1 = Moeda.query.filter_by(nome="TesteDeMoeda").first()
        self.assertEqual(m1.nome, "TesteDeDoenca")
        self.assertEqual(m1.descricao, "Foi?")

        db.session.delete(m1)
        db.session.commit()