from django.urls import path
from api_banco_dado import views

urlpatterns = [
    path('accounts/', views.accounts_list),
    path('accounts/<int:pk>', views.account_detail),
    path('aluguel/', views.alugueis_list),
    path('aluguel/<int:pk>', views.aluguel_detail),
    path('boleto/', views.boletos_list),
    path('boleto/<int:pk>', views.boleto_detail),
    path('cliente/', views.clientes_list),
    path('cliente/<int:pk>', views.cliente_detail),
    path('contato/', views.contatos_list),
    path('contato/<int:pk>', views.contato_detail),
    path('corretor/', views.corretores_list),
    path('corretor/<int:pk>', views.corretor_detail),
    path('endereco/', views.enderecos_list),
    path('endereco/<int:pk>', views.endereco_detail),
    path('imovel/', views.imoveis_list),
    path('imovel/<int:pk>', views.imovel_detail),
    path('mensagem/', views.mensagens_list),
    path('mensagem/<int:pk>', views.mensagem_detail),
    path('proprietario/', views.proprietarios_list),
    path('proprietario/<int:pk>', views.proprietario_detail),
    path('venda/', views.vendas_list),
    path('venda/<int:pk>', views.venda_detail),
]