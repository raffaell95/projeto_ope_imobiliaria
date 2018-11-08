from django.urls import path
from login.views import login, entrar, sair

urlpatterns = [
    path('', login, name='login'),
    path('entrar/', entrar, name='entrar'),
    path('sair/', sair, name='sair')
]