from config.config import *
from modelos.moeda import Moeda
from modelos.cedula import Cedula
from modelos.album import Album
from rotas.cadastro import cadastro
from rotas.login import login


@app.route("/")
def inicio():
    return '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">' +\
        '<h1 style="text-align: center;" class="p-2 text-bg-primary">Sistema de gerenciamento de dinheiro</h1>'+\
        '<h3 style="text-align: center;">Bem vindo a rota padrão</h3>'+\
        '<h4 style="text-align: center;">⇩ Link para o diretorio do git ⇩</h4>'+\
        '<button class="d-block btn btn-primary position-absolute top-50 start-50 translate-middle" onclick="location.href=\'https://github.com/SamuelCandido/lastprog\'">Click-me</button>'


@jwt_required
@app.route("/listar_moedas")
def listar_moedas():
    # obter as Moeda do cadastro
    moedas = db.session.query(Moeda).all()
    # aplicar o método json que a classe Moeda possui a cada elemento da lista
    moedas_em_json = [ x.json() for x in moedas ]
    # converter a lista do python para json
    resposta = jsonify(moedas_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...


# teste da rota: curl -d '{"nome":"Euro", "ano":"2002"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_moeda
@jwt_required
@app.route("/incluir_moeda", methods=['post'])
def incluir_moeda():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "Moeda icluida com sucesso"})
    # receber as informações da nva moeda
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    if dados["nome"] == "": 
        return jsonify({"resultado":"erro", "detalhes":"Nome da moeda não pode ser vazia"})
    try: # tentar executar a operação
      nova = Moeda(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!


# teste: curl -X DELETE http://localhost:5000/excluir_moeda/1
@jwt_required
@app.route("/excluir_moeda/<int:moeda_id>", methods=['DELETE'])
def excluir_moeda(moeda_id):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "Moeda excluida com sucesso"})
    try:
        # excluir a pessoa do ID informado
        Moeda.query.filter(Moeda.id == moeda_id).delete()
        # confirmar a exclusão
        db.session.commit()
    except Exception as e:
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

''' teste da exclusão:
$ curl -X DELETE http://localhost:5000/excluir_moeda/1
{
  "detalhes": "ok", 
  "resultado": "ok"
} 
'''

@jwt_required
@app.route("/listar_albuns")
def listar_albuns():
    # obter as Moeda do cadastro
    albums = db.session.query(Album).all()
    # aplicar o método json que a classe Moeda possui a cada elemento da lista
    albums_em_json = [ x.json() for x in albums ]
    # converter a lista do python para json
    resposta = jsonify(albums_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...


# teste da rota: curl -d '{"nome":"Euro", "ano":"2002"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_moeda
@jwt_required
@app.route("/incluir_album", methods=['post'])
def incluir_album():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "Album incluido com sucesso"})
    # receber as informações da nova moeda
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    if dados["nome"] == "": 
        return jsonify({"resultado":"erro", "detalhes":"Nome do album não pode ser vazio"})
    try: # tentar executar a operação
      nova = Album(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!


# teste: curl -X DELETE http://localhost:5000/excluir_moeda/1
@jwt_required
@app.route("/excluir_album/<int:album_id>", methods=['DELETE'])
def excluir_album(album_id):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "Album excluido com sucesso"})
    try:
        # excluir a pessoa do ID informado
        Album.query.filter(Album.id == album_id).delete()
        # confirmar a exclusão
        db.session.commit()
    except Exception as e:
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!


#trocar cedulas por cedula
@jwt_required
@app.route("/listar_cedulas")
def listar_cedulas():
    # obter as Cedula do cadastro
    cedulas = db.session.query(Cedula).all()
    # aplicar o método json que a classe cedula possui a cada elemento da lista
    cedulas_em_json = [ x.json() for x in cedulas ]
    # converter a lista do python para json
    resposta = jsonify(cedulas_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...


# teste da rota: curl -d '{"nome":"Euro", "ano":"2002"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_cedula
@jwt_required
@app.route("/incluir_cedula", methods=['post'])
def incluir_cedula():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "Cedula incluida com sucesso"})
    # receber as informações da nva cedula
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    if dados["nome"] == "": 
        return jsonify({"resultado":"erro", "detalhes":"Nome da cedula não pode ser vazia"})
    try: # tentar executar a operação
      nova = Cedula(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de errohttp://localhost:5000/
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!


# teste: curl -X DELETE http://localhost:5000/excluir_cedula/1
@jwt_required
@app.route("/excluir_cedula/<int:cedula_id>", methods=['DELETE'])
def excluir_cedula(cedula_id):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "Cedula excluida com sucesso"})
    try:
        # excluir a pessoa do ID informado
        Cedula.query.filter(Cedula.id == cedula_id).delete()
        # confirmar a exclusão
        db.session.commit()
    except Exception as e:
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!
# SÓ ATÉ AQUI O DE BAIXO DEIXA



db.create_all()
app.run(host="0.0.0.0", debug=True)

