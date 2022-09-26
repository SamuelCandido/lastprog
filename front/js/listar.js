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
                '<td>' + "Foto " + '</td>' +
                '<td><button class="btn btn-danger deletar-moeda" data-id-moeda="'+moedas[i].id+'"> Excluir </button></td>'
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaMoedas').append(lin);
            
        };
    };

});