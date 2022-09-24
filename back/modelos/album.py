from config import *
from moeda import *
from cedula import *

class Album(Moeda, Cedula):
    # atributos do album
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, nome: str, ano: int , foto, pais: str):
        super().__init__(nome, ano, foto, pais) 
        self.pais = pais

    def esconder_album(self):
        print("Só pra n dar erro")