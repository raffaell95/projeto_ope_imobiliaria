from django.urls import path
from api_banco_dado import views

urlpatterns = [
    path('cliente/', views.clientes_list),
    path('cliente/<int:pk>', views.cliente_detail, name="cliente_detail"),
    path('corretor/', views.corretores_list),
    path('corretor/<int:pk>', views.corretor_detail),
    path('imovel/', views.imoveis_list),
    path('imovel/<int:pk>', views.imovel_detail),
    path('proprietario/', views.proprietarios_list),
    path('proprietario/<int:pk>', views.proprietario_detail),
]