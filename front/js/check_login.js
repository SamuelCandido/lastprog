$(function () {

    // obtém login da sessão
    var login = sessionStorage.getItem('login');
    var mensagem = "";
    // o login existe?
    if (login === null) {
        mensagem = `Você ainda não fez login. <a href=login.html>Faça agora</a> :-)`;
    } else {
        mensagem = `Bem vindo, ${login}.`;
        // carrega o menu de opções
    }
    // exibe a mensagem na tela
    $("#mensagem").html(mensagem);

    // código para mapear click do botão de logout
    $(document).on("click", "#logout", function () {
        // remove item da sessao
        sessionStorage.removeItem('login');
        // atualiza a tela
        window.location = 'login.html';
    });

});