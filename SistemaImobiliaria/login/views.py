from django.shortcuts import render, redirect
from login.models import Usuario
# Create your views here.

def login(request):

        return render(request, 'login.html')

def entrar(request):
        emailusuario = request.POST.get('inputEmail')
        senhausuario = request.POST.get('inputPassword')

        if Usuario.objects.get(email = emailusuario) and Usuario.objects.get(senha = senhausuario):
                return redirect('/sistema/cadastro/')

        
    
def sair(request):
        return redirect('/')




    
