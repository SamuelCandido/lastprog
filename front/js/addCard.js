$(function(){

    $.ajax({
        url: 'http://localhost:5000/listar_albuns', // lembrar de trocar a url
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    //incluir album
    $("#btIncluirCard").click(function() {
        //pegar dados da tela
        nome = $("#tituloCard").val();
        descricao = $("#descricaoCard").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, descricao: descricao});
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_album',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: albumIncluido, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function albumIncluido (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Album incluída com sucesso!");
                //$("#mensagem").text("Pessoa incluída com sucesso!");
                window.location.reload();
                // limpar os campos
                // $("#typeUserX-2").val("");
                // $("#typeAnoX-2").val("");
            } else {
                // informar mensagem de erro
                alert("ERRO na inclusão: "+retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO ao contactar back-end: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
        // listar album
        
    $("#btIncluirCard").click(function(){

        // incluir card
    });
        
})

function listar(data) {
    console.log(data)
    for (let card of data) {
        let title =card["nome"];
        let descricao = card["descricao"];
        $("#listaAlbum").append(`
            <div class="col">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">${title}</h5>
                        <p class="card-text">${descricao}</p>
                    </div>
                    <div class="card-footer">
                        <a onclick="location.href='album.html'" class="btn btn-primary">Entrar no álbum</a>
                    </div>
                </div>
            </div>
        `);
    }
};