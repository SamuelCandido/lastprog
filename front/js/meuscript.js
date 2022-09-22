$(function() { // quando o documento estiver pronto/carregado
    
    // função para exibir pessoas na tabela
    function exibir_moedas() {
        $.ajax({
            url: 'http://localhost:5000/listar_moedas',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar, // chama a função listar para processar o resultado
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend: ");
            }
        });
        function listar (moedas) {
            // esvaziar o corpo da tabela
            $('#corpoTabelaPessoas').empty();
            // tornar a tabela visível
            mostrar_conteudo("tabelaMoedas");      
            // percorrer a lista de moedas retornadas; 
            for (var i in pessoas) { //i vale a posição no vetor
                lin = '<tr id="linha_'+pessoas[i].id+'">' + 
                '<td>' + moedas[i].nome + '</td>' + 
                '<td>' + moedas[i].ano + '</td>' +  
                '<td><a href=# id="excluir_' + moedas[i].id + '" ' + 
                  'class="excluir_moedas"><img src="img/excluir.png" '+
                  'alt="Excluir moeda" title="Excluir moeda"></a>' + 
                '</td>' + 
                '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaMoedas').append(lin);
            }
        }
    }

    // função que mostra um conteúdo e esconde os outros
    function mostrar_conteudo(identificador) {
        // esconde todos os conteúdos
        $("#tabelaMoedas").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        // torna o conteúdo escolhido visível
        $("#"+identificador).removeClass('invisible');      
    }

    // código para mapear o click do link Listar
    $(document).on("click", "#linkListarMoedas", function() {
        exibir_moedas();
    });
    
    // código para mapear click do link Inicio
    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoInicial");
    });

    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirPessoa", function() {
        //pegar dados da tela
        nome = $("#campoNome").val();
        ano = $("#campoAno").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, ano: ano });
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
                // limpar os campos
                $("#campoNome").val("");
                $("#campoAno").val("");
            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("erro ao incluir dados, verifique o backend: ");
        }
    });

    // código a ser executado quando a janela de inclusão de moeda for fechada
    $('#modalIncluirMoeda').on('hide.bs.modal', function (e) {
        // se a página de listagem não estiver invisível
        if (! $("#tabelaMoeda").hasClass('invisible')) {
            // atualizar a página de listagem
            exibir_moedas();
        }
    });

    // a função abaixo é executada quando a página abre
    mostrar_conteudo("conteudoInicial");

    // código para os ícones de excluir moedas (classe css)
    $(document).on("click", ".excluir_moeda", function() {
        // obter o ID do ícone que foi clicado
        var componente_clicado = $(this).attr('id'); 
        // no id do ícone, obter o ID da moeda
        var nome_icone = "excluir_";
        var id_moeda = componente_clicado.substring(nome_icone.length);
        // solicitar a exclusão da pessoa
        $.ajax({
            url: 'http://localhost:5000/excluir_moeda/'+id_moeda,
            type: 'DELETE', // método da requisição
            dataType: 'json', // os dados são recebidos no formato json
            success: moedaExcluida, // chama a função listar para processar o resultado
            error: erroAoExcluir
        });
        function moedaExcluida (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // remover da tela a linha cuja moeda foi excluída
                $("#linha_" + id_moeda).fadeOut(1000, function(){
                    // informar resultado de sucesso
                    alert("Moeda removida com sucesso!");
                });
            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoExcluir (retorno) {
            // informar mensagem de erro
            alert("erro ao excluir dados, verifique o backend: ");
        }
    });
    
});
