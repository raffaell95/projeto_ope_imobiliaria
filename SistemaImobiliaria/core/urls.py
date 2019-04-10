from django.urls import path
from core.views import *

urlpatterns = [
    path('entrar/', entrar, name='entrar'),
    path('sair/', sair, name='sair'),
    path('sistema/', homeSistema, name='home-sistema'),
    path('cadastro/',cadastro, name='cadastro'),
    path('cadastro/clientes/', cadastroClientes, name='cadastro-clientes')
]