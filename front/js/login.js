$(function () { // quando o documento estiver pronto/carregado
    function atualizarToken(token) {
        sessionStorage.setItem('login-token', token)
        window.location = '../html/galeria.html'
    }
    
    let token = sessionStorage.getItem('login-token')

    if (token != null) {
        atualizarToken(token)
    }

    $(document).on("click", "#btCadastrar", function () {
        //pegar dados da tela
        var email = $("#campoEmail").val();
        var senha = $("#campoSenha").val();

        $.ajax({
            url: '/cadastro',
            method: 'POST',

            contentType: 'application/json',
            data: JSON.stringify({
                email: email,
                senha: senha,
            }),

            success: atualizarToken,
            error: () => alert('não foi possível fazer login')
        })

        return window.location = '../html/login.html';  
    });

    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btLogar", function () {
        //pegar dados da tela
        var email = $("#campoEmail").val();
        var senha = $("#campoSenha").val();

        $.ajax({
            url: '/login',
            method: 'POST',

            contentType: 'application/json',
            data: JSON.stringify({
                email, senha
            }),

            success: (resultado) => {
                if (resultado.resultado == "ok") {
                    atualizarToken(resultado.detalhes)
                } else {
                    alert("Erro ao fazer login: " + resultado.detalhes)
                }
            },

            error: () => {
                alert("Não foi possível fazer login.")
            }
        })
        
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