from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('entrar/', entrar, name='entrar'),
    path('sair/', sair, name='sair'),
    path('sistema/', homeSistema, name='home-sistema'),
    path('cadastro/',cadastro, name='cadastro'),
    path('cadastro/clientes/', cadastro_clientes, name='cadastro-clientes'),
    path('cadastro/delete_cliente/<int:pk>/', delete_cliente, name='delete_cliente'),
    path('cadastro/atualizar_view_cliente/<int:pk>/', atualizar_view_cliente, name='atualizar_view_cliente'),
]