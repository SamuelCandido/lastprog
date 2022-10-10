from config.config import *
from modelos.dinheiro import Dinheiro

class Cedula(Dinheiro):
    # estabelecer vínculo com a tabela-pai. Este campo define
    # a criação da tabela cedula
    id = db.Column(db.Integer, db.ForeignKey('dinheiro.id'), primary_key=True)

    # a identidade polimórfica da classe será armazenada 
    # no campo type da classe pai
    __mapper_args__ = { 
        'polymorphic_identity':'cedula',
    }
    conservacao = db.Column(db.Float) # atributo da cedula
    def __str__(self):
        return super().__str__() + f", conservacao={self.conservacao}"

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(db.db):
        os.remove(db.db)

    # criar tabelas
    db.create_all()

    # teste da classe Cedula
    c1 = Cedula(nCedula = "Euro", ano = "2002", valor = "50", conservacao = "ótimo") 
    c2 = Cedula(nCedula = "Dolar", ano = "1980", valor = "100", conservacao = "ruim")      

    # persistir
    db.session.add(c1)
    db.session.add(c2)
    db.session.commit()

    # exibir a Cedula
    print(c2)

    # exibir a Cedula no format json
    print(c2.json())
