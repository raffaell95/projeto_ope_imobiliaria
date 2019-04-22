from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', sair, name='logout'),
    path('register/', registrar, name='register'),
    path('sistema/', home_sistema, name='home-sistema'),
    path('cadastro/',cadastro, name='cadastro'),
    path('cadastro/clientes/', cadastro_clientes, name='cadastro-clientes'),
    path('cadastro/imoveis/', cadastro_imoveis, name='cadastro-imoveis'),
    path('cadastro/delete_cliente/<int:pk>/', delete_cliente, name='delete_cliente'),
    path('cadastro/atualizar_view_cliente/<int:pk>/', atualizar_view_cliente, name='atualizar_view_cliente'),
]