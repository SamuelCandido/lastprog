from config import *

class Moeda(db.Model):
    # atributos da moeda
    id = db.Column(db.Integer, primary_key=True)
    nMoeda = db.Column(db.String(254))
    ano = db.Column(db.String(254))

    # método para expressar a moeda em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nMoeda + ", " +\
            self.ano 
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nMoeda": self.nMoeda,
            "ano": self.ano,
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(moedasbd):
        os.remove(moedasbd)

    # criar tabelas
    db.create_all()

    # teste da classe Moeda
    m1 = Moeda(nMoeda = "Euro", ano = "2002")
    m2 = Moeda(nMoeda = "Dolar", ano = "1980")      
    
    # persistir
    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()
    
    # exibir a Moeda
    print(m2)

    # exibir a Moeda no format json
    print(m2.json())
