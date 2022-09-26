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
                alert("Album incluído com sucesso!");
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
        
});

$(function(){
    $(document).on("click", "#xClose", function() {

        // $(this) pega o botao que foi 
        // .attr('data-id-moeda') pega o atributo
        // data-(alguma coisa) é usado para atributos com nomes customizados
        let id_album = $(this).attr('data-album');
        console.log(id_album)
        $.ajax({
            url: 'http://localhost:5000/excluir_album/'+ id_album,
            type: 'DELETE',
            success: albumExcluido, // chama a função listar para processar o resultado
            error: erroAoExcluir
        });
        function albumExcluido (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Album excluído com sucesso!");
                window.location.reload()
                //$("#mensagem").text("Moeda excluída com sucesso!");
                // // limpar os campos
                // $("#typeUserX-2").val("");
                // $("#typeAnoX-2").val("");
                // $('#corpoTabelaMoedas').remove(lin);
            } 
            else {
                // informar mensagem de erro
                alert("ERRO na exclusão: "+retorno.resultado + ":" + retorno.detalhes);
            }            
        };
        function erroAoExcluir (retorno) {
            // informar mensagem de erro
            alert("ERRO ao contactar back-end: "+retorno.resultado + ":" + retorno.detalhes);
        };
    });
});


function listar(data) {
    console.log(data)
    for (let card of data) {
        let title =card["nome"];
        let descricao = card["descricao"];
        $("#listaAlbum").append(`
            <div class="col">
                <div class="card h-100">
                    <div class="card-body">
                    <button id="xClose" type="button" class="btn-close btn-close-black float-end" aria-label="Close" data-album="${card.id}"></button>
                        <h5 class="card-title">${title}</h5>
                        <p class="card-text">${descricao}</p>
                    </div>
                    <div class="card-footer">
                        <a onclick="location.href='album.html'" class="btn btn-primary">Entrar no álbum</a>
                    </div>
                </div>
            </div>
        `);
    };
};