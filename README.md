# Lastprog
**Contribuintes para esta criação:**
- Alana Andreazza, Prof. Hylson Vescovi, Samuel José Candido Yara Rahn

**Do que se trata:**
- Se trata de um sistema de albuns de moedas/cedulas ("Galeria"), em tese não é de muita utilidade, toda via serve para testar os conhecimentos e por em pratica tudo visto no 3 ano do Instituto Federal Catarinense 

# TESTES

- Para funcionar os testes é necessario rodar dentro da pasta back
- Em caso de erro tente: python3 -m unittest discover -s ./tests/ -p "test_*.py" (RODAR DENTRO DE BACK)

# Documentação API

**/**
- Rota padrão, deve retornar o link do github: [Link do repositorio](https://github.com/SamuelCandido/lastprog)

**/listar_moedas**
- teste: curl localhost:5000/listar_moedas
- Vai listar as moedas em json

**/listar_cedulas**
- teste: curl localhost:5000/listar_cedulas
- Vai listar as cedula em json

**/listar_albuns**
- teste: curl localhost:5000/listar_albuns
- Vai listar os albuns em json

**/incluir_moeda**
- teste da rota: curl -d '{"nome":"Euro", "ano":"2002"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_moeda
- Para fazer esta rota ficar operante podes fazer por meio do curl, que se encontra acima da função da rota no back/servidor-back.py
- Se der certo a inclusão deve retornar: "resultado": "ok",  "detalhes": "Moeda incluida com sucesso"
- Em caso Nome == null, deve retornar: "resultado": "erro",  "detalhes": "Nome da moeda não pode ser vazia"
- Em caso de qualquer erro, deve retornar: "resultado": "erro",  "detalhes": (Descrição do erro)

**/incluir_cedula**
- teste da rota: curl -d '{"nome":"Euro", "ano":"2002"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_cedula
- Para fazer esta rota ficar operante podes fazer por meio do curl, que se encontra acima da função da rota no back/servidor-back.py
- Se der certo a inclusão deve retornar: "resultado": "ok",  "detalhes": "Cedula incluida com sucesso"
- Em caso Nome == null, deve retornar: "resultado": "erro",  "detalhes": "Nome do cedula não pode ser vazia"
- Em caso de qualquer erro, deve retornar: "resultado": "erro",  "detalhes": (Descrição do erro)

**/incluir_album**
- teste da rota: curl -d '{"nome":"Euro", "ano":"2002"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_album
- Para fazer esta rota ficar operante podes fazer por meio do curl, que se encontra acima da função da rota no back/servidor-back.py
- Se der certo a inclusão deve retornar: "resultado": "ok",  "detalhes": "Album incluido com sucesso"
- Em caso Nome == null, deve retornar: "resultado": "erro",  "detalhes": "Nome do album não pode ser vazio"

**/excluir_moeda**
- teste: curl -X DELETE http://localhost:5000/excluir_moeda/1
- Ao excluir, deve retornar: "resultado": "ok", "detalhes": "Moeda excluida com sucesso"

**/excluir_cedula**
- teste: curl -X DELETE http://localhost:5000/excluir_cedula/1
- Ao excluir, deve retornar: "resultado": "ok", "detalhes": "Cedula excluida com sucesso"

**/excluir_album**
- teste: curl -X DELETE http://localhost:5000/excluir_album/1
- Ao excluir, deve retornar: "resultado": "ok", "detalhes": "Album excluido com sucesso"

**/cadastro**
- teste da rota: curl -X POST localhost:5000/cadastro -d '{"nome":"joao da silva","email":"josilva@gmail.com","senha":"joao123"}' -H 'Content-Type: application/json'
- Deve incluir pessoa/usuario no banco de dados
- Em caso de usuario existente deve retornar: "resultado": "erro", "detalhes": "Usuario já existente"
- Em caso de nome/email Null deve retornar: "resultado":"erro", "detalhes":"Nome de usuario não pode ser vazio"
- Em caso de qualquer erro não tratado deve retornar: "resultado":"erro", "detalhes":str(e)

**/login**
- teste da rota: curl -X POST localhost:5000/login -d '{"email":"josilva@gmail.com","senha":"joao123"}' -H 'Content-Type: application/json'
- Deve ao acessar, com email e senhas corretos, sua galeria
- O mesmo se encontra no erro por qualquer usuario acessar a mesma galeria
- Em caso de login correto deve retornar: "resultado":"ok", "detalhes":dict(token=access_token)
- Em caso de email/senha Null deve retornar: "resultado":"erro", "detalhes":"Nome de usuario não pode ser vazio"
- Em caso de login incorreto deve retornar: "resultado": "erro", "detalhes":"usuario ou senha incorreto(s)"


