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
$("#btn-atualizar-cliente").on("click", function(){
    console.log("botao atualizar acionado");
    var id = $('#modal-alterar-cliente').attr("id_cliente");
    var href_alterar = $(location).attr("href").replace('cadastro/clientes', 'api/cliente/' + id);
    var url_alterar = href_alterar.slice(0, -1);
    var nome = $('input#nome').val();
    var cpf_cnpj = $('input#cpf-alterar').val();
    var endereco = $('input#endereco').val();
    var bairro = $('input#bairro').val();
    var cidade = $('input#cidade').val();
    var cep = $('input#cep').val();
    var uf = $('input#uf').val();
    var email = $('input#email').val();
    var telefone = $('input#tel').val();
    
    $.ajax({
        url: url_alterar,
        type: 'PUT',
        data: JSON.stringify({
            "id": id,
            "nome_cliente": nome,
            "cpf_cnpj": cpf_cnpj,
            "endereco": endereco,
            "bairro": bairro,
            "cidade": cidade,
            "cep": cep,
            "uf": uf,
            "email": email,
            "telefone": telefone
        }),
        dataType: 'json',
        success: function(data) {
            alert('Alterado com sucesso.');
            $(location).attr("href", $(location).attr("href"));
        }
      });
});



function clickUpdate(id){
    $('#modal-alterar-cliente').attr('id_cliente', id);
    var url_cliente = $(location).attr('href').replace("/clientes", "/atualizar_view_cliente/" + id);
    $.get(url_cliente, function(data){
        console.log(data);
        $('input#nome').val(data["nome_cliente"]);
        $('input#cpf-alterar').val(data["cpf_cnpj"]);
        $('input#endereco').val(data["endereco"]);
        $('input#bairro').val(data["bairro"]);
        $('input#cidade').val(data["cidade"]);
        $('input#cep').val(data["cep"]);
        $('input#uf').val(data["uf"]);
        $('input#email').val(data["email"]);
        $('input#tel').val(data["telefone"]);
    });
};





$(function()
{
    //Executa a requisição quando o campo username perder o foco
    $('#cpf-alterar').blur(function()
    {
        var cpf = $('#cpf-alterar').val().replace(/[^0-9]/g, '').toString();

        if( cpf.length == 11 )
        {
            var v = [];

            //Calcula o primeiro dígito de verificação.
            v[0] = 1 * cpf[0] + 2 * cpf[1] + 3 * cpf[2];
            v[0] += 4 * cpf[3] + 5 * cpf[4] + 6 * cpf[5];
            v[0] += 7 * cpf[6] + 8 * cpf[7] + 9 * cpf[8];
            v[0] = v[0] % 11;
            v[0] = v[0] % 10;

            //Calcula o segundo dígito de verificação.
            v[1] = 1 * cpf[1] + 2 * cpf[2] + 3 * cpf[3];
            v[1] += 4 * cpf[4] + 5 * cpf[5] + 6 * cpf[6];
            v[1] += 7 * cpf[7] + 8 * cpf[8] + 9 * v[0];
            v[1] = v[1] % 11;
            v[1] = v[1] % 10;

            //Retorna Verdadeiro se os dígitos de verificação são os esperados.
            if ( (v[0] != cpf[9]) || (v[1] != cpf[10]) ){   
                $("#cpf-error-alterar").css({
                    "color": "rgba(163, 5, 5, 0.966)",
                    "font-size": "12px",
                    "text-align": "center",
                    "padding-bottom": "8px"
                  });
                $("#btn-atualizar-cliente").css({"display": "none"});
                $("#cpf-error-alterar").html("Digite um CPF válido!");
                
                $('#cpf-alterar').val('');
                $('#cpf-alterar').focus();
            } else {
                $("#btn-atualizar-cliente").css({"display": "inline-block"});
                $("#cpf-error-alterar").html("");
            }
        } else {   
                $("#cpf-error-alterar").css({
                    "color": "rgba(163, 5, 5, 0.966)",
                    "font-size": "12px",
                    "text-align": "center",
                    "padding-bottom": "8px"
                });
                $("#btn-atualizar-cliente").css({"display": "none"});
                $("#cpf-error-alterar").html("Digite um CPF válido!");
                
                $('#cpf-alterar').val('');
                $('#cpf-alterar').focus();
            }
    });
});


$(function()
{
    //Executa a requisição quando o campo username perder o foco
    $('#cpf-incluir').blur(function()
    {
        var cpf = $('#cpf-incluir').val().replace(/[^0-9]/g, '').toString();

        if( cpf.length == 11 )
        {
            var v = [];

            //Calcula o primeiro dígito de verificação.
            v[0] = 1 * cpf[0] + 2 * cpf[1] + 3 * cpf[2];
            v[0] += 4 * cpf[3] + 5 * cpf[4] + 6 * cpf[5];
            v[0] += 7 * cpf[6] + 8 * cpf[7] + 9 * cpf[8];
            v[0] = v[0] % 11;
            v[0] = v[0] % 10;

            //Calcula o segundo dígito de verificação.
            v[1] = 1 * cpf[1] + 2 * cpf[2] + 3 * cpf[3];
            v[1] += 4 * cpf[4] + 5 * cpf[5] + 6 * cpf[6];
            v[1] += 7 * cpf[7] + 8 * cpf[8] + 9 * v[0];
            v[1] = v[1] % 11;
            v[1] = v[1] % 10;

            //Retorna Verdadeiro se os dígitos de verificação são os esperados.
            if ( (v[0] != cpf[9]) || (v[1] != cpf[10]) )
            {
                $("#cpf-error-incluir").css({
                    "color": "rgba(163, 5, 5, 0.966)",
                    "font-size": "12px",
                    "text-align": "center",
                    "padding-bottom": "8px"
                  });
                $("#btn-cad-cliente").css({"display": "none"});
                $("#cpf-error-incluir").html("Digite um CPF válido!");
                $('#cpf-incluir').val('');
                $('#cpf-incluir').focus();
            } else {
                $("#btn-cad-cliente").css({"display": "inline-block"});
                $("#cpf-error-incluir").html("");
            }
        }
        else
        {   
            $("#cpf-error-incluir").css({
                "color": "rgba(163, 5, 5, 0.966)",
                "font-size": "12px",
                "text-align": "center",
                "padding-bottom": "8px"
              });
            $("#btn-cad-cliente").css({"display": "none"});
            $("#cpf-error-incluir").html("Digite um CPF válido!");
            $('#cpf-incluir').val('');
            $('#cpf-incluir').focus();
        }
    });
});