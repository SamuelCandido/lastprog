# Lastprog
Sistema de albuns de moedas/cedulas ("Galeria").

# TESTES

python3 -m unittest discover -s ./tests/ -p "test_*.py" (RODAR DENTRO DE BACK)

# Documentação API

**/**
- Rota padrão, deve retornar o link do github: [Link do repositorio](https://github.com/SamuelCandido/lastprog)

**/listar_moeda**
- Vai listar as moedas em json

**/listar_cedula**
- Vai listar as cedula em json

**/listar_album**
- Vai listar os albuns em json

**/incluir_moeda**
- Para fazer esta rota ficar operante podes fazer por meio do curl, que se encontra acima da função da rota no back/servidor-back.py
- Se der certo a inclusão deve retornar: "resultado": "ok",  "detalhes": "Moeda incluida com sucesso"
- Em caso Nome == null, deve retornar: "resultado": "erro",  "detalhes": "Nome da moeda não pode ser vazia"
- Em caso de qualquer erro, deve retornar: "resultado": "erro",  "detalhes": (Descrição do erro)

**/incluir_cedula**
- Para fazer esta rota ficar operante podes fazer por meio do curl, que se encontra acima da função da rota no back/servidor-back.py
- Se der certo a inclusão deve retornar: "resultado": "ok",  "detalhes": "Cedula incluida com sucesso"
- Em caso Nome == null, deve retornar: "resultado": "erro",  "detalhes": "Nome do cedula não pode ser vazia"
- Em caso de qualquer erro, deve retornar: "resultado": "erro",  "detalhes": (Descrição do erro)

**/incluir_album**
- Para fazer esta rota ficar operante podes fazer por meio do curl, que se encontra acima da função da rota no back/servidor-back.py
- Se der certo a inclusão deve retornar: "resultado": "ok",  "detalhes": "Album incluido com sucesso"
- Em caso Nome == null, deve retornar: "resultado": "erro",  "detalhes": "Nome do album não pode ser vazio"

**/excluir_moeda**
- Ao excluir, deve retornar: "resultado": "ok", "detalhes": "Moeda excluida com sucesso"

**/excluir_cedula**
- Ao excluir, deve retornar: "resultado": "ok", "detalhes": "Cedula excluida com sucesso"

**/excluir_album**
- Ao excluir, deve retornar: "resultado": "ok", "detalhes": "Album excluido com sucesso"

