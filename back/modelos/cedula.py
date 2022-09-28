from back.config.config import *

class Cedula(db.Model):
    # atributos da moeda
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    ano = db.Column(db.String(254), nullable=False)

    # método para expressar a pessoa em forma de texto
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

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(moedasbd):
        os.remove(moedasbd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    m1 = Moeda(nome = "Euro", ano = "2002")
    m2 = Moeda(nome = "Dolar", ano = "1980")      
    
    # persistir
    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()
    
    # exibir a pessoa
    print(m2)

    # exibir a pessoa no format json
    print(m2.json())
