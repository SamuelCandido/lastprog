$(function() { // quando o documento estiver pronto/carregado
    
    // código para mapear click do botão incluir moeda
    $(document).on("click", "#btIncluir", function() {
        //pegar dados da tela
        nome = $("#typeUserX-2").val();
        ano = $("#typeAnoX-2").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, ano: ano});
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://172.17.99.244:5000/incluir_moeda',
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
                window.location.reload()
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