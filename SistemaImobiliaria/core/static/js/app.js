//Start delete cliente script//
function clickDelete(id){
    $('#modal-exluir-cliente').attr('id_cliente', id);
};

$("#btn-delete-cliente").on("click", function(){
    var id = $('#modal-exluir-cliente').attr("id_cliente");
    var href_excluir = $(location).attr("href").replace('/clientes', '/delete_cliente/' + id);
    $(location).attr("href", href_excluir);
});
//End delete cliente script//

//Start update cliente script
function clickUpdate(id){
    $('#modal-alterar-cliente').attr('id_cliente', id);
    var url_cliente = $(location).attr('href').replace("/clientes", "/atualizar_view_cliente/" + id);
    $.get(url_cliente, function(data){
        console.log(data);
        $('input#nome').val(data["nome_cliente"]);
        $('input#cpf').val(data["cpf_cnpj"]);
        $('input#endereco').val(data["endereco"]);
        $('input#bairro').val(data["bairro"]);
        $('input#cidade').val(data["cidade"]);
        $('input#cep').val(data["cep"]);
        $('input#uf').val(data["uf"]);
        $('input#email').val(data["email"]);
        $('input#tel').val(data["telefone"]);
    });
}

$("#btn-atualiza-cliente").on("click", function(){
    var id = $('#modal-alterar-cliente').attr("id_cliente");
    var href_alterar = $(location).attr("href").replace('/clientes', '/atualizar_cliente/' + id);
    $(location).attr("href", href_alterar);
});
