$(function(){
    $("#btIncluirCard").click(function(){
        var title = $("#tituloCard").val()
        var description = $("#descricaoCard").val()

        $("#listaAlbum").append(`
            <div class="col">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">${title}</h5>
                        <p class="card-text">${description}</p>
                    </div>
                    <div class="card-footer">
                        <a onclick="location.href='album.html'" class="btn btn-primary">Entrar no álbum</a>
                    </div>
                </div>
            </div>
        `);
    });
})