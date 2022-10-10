from config.config import *

class Usuario(db.Model):
    # atributos da usuario
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254),nullable=False)
    email = db.Column(db.String(254), nullable=False)
    senha = db.Column(db.Text, nullable=False)

    # método para expressar a usuario em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.email + ", " + self.senha

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

    # teste da classe usuario
    u1 = Usuario(nome = "Maria", email = "maria@gmail.com", senha = "123")
    u2 = Usuario(nome = "Joao", email = "joao@gmail.com", senha = "456")
    
    # persistir
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()
    
    # exibir a usuario
    print(u2)

    # exibir a usuario no format json
    print(u2.json())