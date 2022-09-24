from config import *
from modelos.moeda import Moeda

@app.route("/")
def inicio():
    return 'Sistema de cadastro de moedas. '+\
        '<a href="/listar_moedas">Operação listar</a>'

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
@app.route("/incluir_moeda", methods=['post'])
def incluir_moeda():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "oi"})
    # receber as informações da nva moeda
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
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
@app.route("/excluir_moeda/<int:moeda_id>", methods=['DELETE'])
def excluir_moeda(moeda_id):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
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

db.create_all()
app.run(host="0.0.0.0", debug=True)

