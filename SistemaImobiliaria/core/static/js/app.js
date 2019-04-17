$("#btn-delete-cliente").on("click", function(){
    var id = $('#modal-exluir-cliente').attr("id_cliente");
    var href_excluir = $(location).attr("href").replace('/clientes', '/delete_cliente/' + id);
    console.log(href_excluir);
    $(location).attr("href", href_excluir);
});

function clickDelete(id){
    $('#modal-exluir-cliente').attr('id_cliente', id);
};

