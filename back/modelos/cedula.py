from config.config import *

class Dinheiro(db.Model):
    # atributos da Cedula
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


class Cedula(Dinheiro):
    pass

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(db.db):
        os.remove(db.db)

    # criar tabelas
    db.create_all()

    # teste da classe Cedula
    c1 = Cedula(nCedula = "Euro", ano = "2002", valor = "50")
    c2 = Cedula(nCedula = "Dolar", ano = "1980", valor = "100")      

    # persistir
    db.session.add(c1)
    db.session.add(c2)
    db.session.commit()

    # exibir a Cedula
    print(c2)

    # exibir a Cedula no format json
    print(c2.json())
