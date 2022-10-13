import unittest

from config.config import db
from modelos.album import Album


class TestAlbum(unittest.TestCase):
    def test_coin(self):
        a1 = Album(nome="TesteDeAlbum", descricao="1999")
        db.session.add(a1)
        db.session.commit()

        a1 = Album.query.filter_by(nome="TesteDeAlbum").first()
        self.assertEqual(a1.nome, "TesteDeAlbum")
        self.assertEqual(a1.descricao, "1999")

        db.session.delete(a1)
        db.session.commit()