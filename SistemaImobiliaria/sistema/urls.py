from django.urls import path
from sistema.views import homeSistema, cadastro, incluirCliente

urlpatterns = [
    path('', homeSistema, name='home-sistema'),
    path('cadastro/',cadastro, name='cadastro'),
    path('cadastro/incluir-clientes/',incluirCliente, name='cadastro-cliente')
]