$(function(){
    $(document).on("click", ".deletar-moeda", function() {

        // $(this) pega o botao que foi 
        // .attr('data-id-moeda') pega o atributo
        // data-(alguma coisa) é usado para atributos com nomes customizados
        let id_moeda = $(this).attr('data-id-moeda');

        $.ajax({
            url: 'http://172.17.99.244:5000/excluir_moeda/'+ id_moeda,
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
});

