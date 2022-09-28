from config.config import *
from modelos.moeda import *
from modelos.cedula import *

class Album(db.Model):
    # atributos do album
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=True)
    descricao = db.Column(db.String(254), nullable=True)

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


# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(bd):
        os.remove(albumbd)

    # criar tabelas
    db.create_all()

    # teste da classe usuario
    a1 = Album(nome = "Teste1", descricao = "blablabla")
    a2 = Album(nome = "Teste2", descricao = "pipipi")
    
    # persistir
    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()
    
    # exibir a usuario
    print(a2)

    # exibir a usuario no format json
    print(a2.json())