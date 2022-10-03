from config.config import *

class Dinheiro(db.Model):
    # atributos da moeda
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    ano = db.Column(db.String(254))
    valor = db.Column(db.Float)

    
    
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


class Moeda(Dinheiro):
    pass

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(db.db):
        os.remove(db.db)

    # criar tabelas
    db.create_all()

    # teste da classe Moeda
    m1 = Moeda(nMoeda = "Euro", ano = "2002", valor = "0.50")
    m2 = Moeda(nMoeda = "Dolar", ano = "1980", valor = "0.10")      

    # persistir
    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()

    # exibir a Moeda
    print(m2)

    # exibir a Moeda no format json
    print(m2.json())