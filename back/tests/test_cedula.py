import unittest

from config.config import db
from modelos.cedula import Cedula


class TestMoney(unittest.TestCase):
    def test_coin(self):
        c1 = Cedula(nome="TesteDeCedula", ano="Foi dinsgraça?")
        db.session.add(c1)
        db.session.commit()

        c1 = Cedula.query.filter_by(nome="TesteDeCedula").first()
        self.assertEqual(c1.nome, "TesteDeCedula")
        self.assertEqual(c1.ano, "Foi dinsgraça?")

        db.session.delete(c1)
        db.session.commit()