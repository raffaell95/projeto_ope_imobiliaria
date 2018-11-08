from django.urls import path
from login.views import login, entrar

urlpatterns = [
    path('', login, name='login'),
    path('entrar/', entrar, name='entrar')
]