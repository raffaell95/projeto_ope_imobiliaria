from django.urls import path
from sistema.views import *

urlpatterns = [
    path('', homeSistema, name='home-sistema'),
    path('cadastro/',cadastro, name='cadastro'),
    path('cadastro/incluir-clientes/',incluirCliente, name='cadastro-cliente'),
    path('cadastro/incluir-usuario/',incluirUsuario, name='cadastro-usuario'),
    path('cadastro/incluir-imovel/',incluirImovel, name='cadastro-imovel'),
    path('cadastro/alterar-cliente/<int:id>/', alterarCliente, name="alterar-cliente"),
    path('cadastro/alterar-imovel/<int:id>/', alterarImovel, name="alterar-imovel"),
    path('cadastro/alterar-usuario/<int:id>/', alterarUsuario, name='alterar-usuario'),
    path('cadastro/remover-cliente/<int:id>/', removerCliente, name='remover-cliente'),
    path('cadastro/remover-imovel/<int:id>/', removerImovel, name='remover-imovel'),
    path('cadastro/remover-usuario/<int:id>/', removerUsuario, name='remover-cliente')
]