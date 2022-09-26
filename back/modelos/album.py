from config import *
from modelos.moeda import *
from modelos.cedula import *

class Album(db.Model):
    # atributos do album
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    decricao = db.Column(db.String(254))

    # método para expressar a moeda em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.descricao 
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
        }