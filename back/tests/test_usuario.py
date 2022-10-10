#import email
import unittest

from config.config import db
from modelos.usuario import Usuario


class TestUser(unittest.TestCase):
    def test_user(self):
        u1 = Usuario(email="asi@gmail.com", senha="123456")
        db.session.add(u1)
        db.session.commit()

        u1 = Usuario.query.filter_by(email="asi@gmail.com").first()
        self.assertEqual(u1.email, "asi@gmail.com")
        self.assertEqual(u1.senha, "123456")

        db.session.delete(u1)
        db.session.commit()