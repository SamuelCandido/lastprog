$(function() { // quando o documento estiver pronto/carregado
    
    // código para mapear click do botão incluir moeda
    $(document).on("click", "#btIncluir", function() {
        //pegar dados da tela
        nome = $("#nomeMoeda").text();
        ano = $("#anoMoeda").text();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, ano: ano});
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_moeda',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: moedaIncluida, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function moedaIncluida (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Moeda incluída com sucesso!");
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
});

    
$(function () { // quando o documento estiver pronto/carregado

    // chamada ao backend
    $.ajax({
        url: 'http://localhost:5000/listar_moedas', // lembrar de trocar a url
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    // função executada quando tudo dá certo
    function listar(moedas) {
        // percorrer a lista de pessoas retornadas; 
        for (var i in moedas) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da moedas
                '<td>' + moedas[i].nome + '</td>' +
                '<td>' + moedas[i].ano + '</td>' +
                '<td><img src="http://localhost:5000/get_image/' + moedas[i].id + '"></td>' +
                '<td><button class="btn-close btn-close-black deletar-moeda" data-id-moeda="'+moedas[i].id+'"></button></td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaMoedas').append(lin);
            
        };
    };
});



$(document).on("click", ".deletar-moeda", function() {

    // $(this) pega o botao que foi 
    // .attr('data-id-moeda') pega o atributo
    // data-(alguma coisa) é usado para atributos com nomes customizados
    let id_moeda = $(this).attr('data-id-moeda');

    $.ajax({
        url: 'http://localhost:5000/excluir_moeda/'+ id_moeda,
        type: 'DELETE',
        success: moedaExcluida, // chama a função listar para processar o resultado
        error: erroAoExcluir
    });
    function moedaExcluida (retorno) {
        if (retorno.resultado == "ok") { // a operação deu certo?
            // informar resultado de sucesso
            alert("Moeda Excluída com sucesso!");
            window.location.reload()
            //$("#mensagem").text("Moeda excluída com sucesso!");
            // // limpar os campos
            // $("#typeUserX-2").val("");
            // $("#typeAnoX-2").val("");
            // $('#corpoTabelaMoedas').remove(lin);
        } else {
            // informar mensagem de erro
            alert("ERRO na exclusão: "+retorno.resultado + ":" + retorno.detalhes);
        }            
    }
    function erroAoExcluir (retorno) {
        // informar mensagem de erro
        alert("ERRO ao contactar back-end: "+retorno.resultado + ":" + retorno.detalhes);
    }
});
