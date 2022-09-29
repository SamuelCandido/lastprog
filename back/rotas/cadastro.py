from config.config import *
from cripto import *
from modelos.usuario import *


@app.route("/cadastro", methods=['POST'])
def cadastro():
    
    dados = request.get.json(force=True)
    email = dados['email']
    senha = dados['senha']

    encontrado = Pessoa.query.filter_by(email=email, senha=cifrar(senha)).first()
    
    if encontrado != None: 
        resposta = jsonify({"resultado": "erro", "detalhes":" Usuario já existente"})
