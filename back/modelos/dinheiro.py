from config.config import *

class Dinheiro(db.Model):
    # atributos da moeda
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    ano = db.Column(db.String(254))
    valor = db.Column(db.Float)

    # atributo necessário para armazenar tipo de classe especializada (discriminador)
    type = db.Column(db.String(50))
    
    # definições de mapeamento da classe mãe
    __mapper_args__ = {
        'polymorphic_identity':'dinheiro', 
        'polymorphic_on': type # nome do campo que vincula os filhos
    }
    
    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.ano + ", " + self.valor
            
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "ano": self.ano,
            "valor": self.valor,
        }
