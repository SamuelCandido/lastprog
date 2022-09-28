$(function () { // quando o documento estiver pronto/carregado

    $(document).on("click", "#btCadastrar", function () {
        //pegar dados da tela
        email = $("#campoEmail").val();
        senha = $("#campoSenha").val();    
        return window.location = '../html/login.html';  
    }); 
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btLogar", function () {
        //pegar dados da tela
        email = $("#campoEmail").val();
        senha = $("#campoSenha").val();
        
        if (email == $("#emailCad").val() && senha == $("#senhaCad").val()) {
            // guarda na sessao
            sessionStorage.setItem('login', login);

            // encaminha para a página principal
            window.location = '../html/galeria.html';
        } else {
            alert("Ae fizeste algo errado, tenta denovo");
        }        
    });   

});