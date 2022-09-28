from config.config import *

class Moeda(db.Model):
    # atributos do usuario
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    ano = db.Column(db.String(254))

    # método para expressar a moeda em forma de texto j
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.ano 
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "ano": self.ano,
        }
