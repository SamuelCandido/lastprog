from config.config import *
from cripto import *
from modelos.usuario import *


@app.route("/cadastro", methods=['POST'])
def cadastro():
    resposta = jsonify({"resultado": "ok", "detalhes":" Usuario cadastrado"})
    dados = request.get_json(force=True)
    if dados["nome"] == "" or dados["email"] == "" or dados["senha"] == "": 
        return jsonify({"resultado":"erro", "detalhes":"Nome de usuario não pode ser vazio"})
    nome = dados['nome']
    email = dados['email']
    senha = dados['senha']

    usuario = Usuario.query.filter_by(nome=nome, email=email, senha=cifrar(senha)).first()
    
    if usuario != None: 
        resposta = jsonify({"resultado": "erro", "detalhes":" Usuario já existente"})

    try: # tentar executar a operação
      nova = Usuario(nome=nome, email=email, senha=cifrar(senha))# criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

# curl -X POST localhost:5000/cadastro -d '{"nome":"joao da silva","email":"josilva@gmail.com","senha":"joao123"}' -H 'Content-Type: application/json'