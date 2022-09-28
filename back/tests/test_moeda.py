import unittest

from config.config import db
from modelos.moeda import Moeda


class TestCoin(unittest.TestCase):
    def test_coin(self):
        m1 = Moeda(nome="TesteDeMoeda", ano="Foi?")
        db.session.add(m1)
        db.session.commit()

        m1 = Moeda.query.filter_by(nome="TesteDeMoeda").first()
        self.assertEqual(m1.nome, "TesteDeMoeda")
        self.assertEqual(m1.ano, "Foi?")

        db.session.delete(m1)
        db.session.commit()