from config.config import *

class Adm(db.Model):
    # atributos da usuario
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254),nullable=False)
    email = db.Column(db.String(254), nullable=False)
    senha = db.Column(db.Text, nullable=False)

    # método para expressar a usuario em forma de texto
    def __str__(self):
        return f'{self.nome} [id={str(self.id)}], ' +\
               f'{self.email}, {self.senha}'

    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(db.db):
        os.remove(db.db)

    # criar tabelas
    db.create_all()

    # teste da classe Adm
    ad1 = Adm(nAdm = "Maria", email = "maria@gmail.com", senha = "123")
    ad2 = Adm(nAdm = "Joao", email = "joao@gmail.com", senha = "456")      

    # persistir
    db.session.add(ad1)
    db.session.add(ad2)
    db.session.commit()

    # exibir a Adm
    print(ad2)

    # exibir a Adm no format json
    print(ad2.json())
