from config.config import *
from dinheiro import Dinheiro

class Moeda(Dinheiro):
    # estabelecer vínculo com a tabela-pai. Este campo define
    # a criação da tabela cedula
    id = db.Column(db.Integer, db.ForeignKey('dinheiro.id'), primary_key=True)

    # a identidade polimórfica da classe será armazenada 
    # no campo type da classe pai
    __mapper_args__ = { 
        'polymorphic_identity':'moeda',
    }
    material = db.Column(db.String(254)) # atributo da moeda
    def __str__(self):
        return super().__str__() + f", material={self.material}"

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(db.db):
        os.remove(db.db)

    # criar tabelas
    db.create_all()

    # teste da classe Moeda
    m1 = Moeda(nMoeda = "Euro", ano = "2002", valor = "0.50", material = "prata")
    m2 = Moeda(nMoeda = "Dolar", ano = "1980", valor = "0.10", material = "bronze")      

    # persistir
    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()

    # exibir a Moeda
    print(m2)

    # exibir a Moeda no format json
    print(m2.json())