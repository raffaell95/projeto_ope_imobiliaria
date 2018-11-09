from django.shortcuts import render, redirect
from login.models import Usuario
# Create your views here.

def login(request):

        return render(request, 'login.html')

def entrar(request):
        emailusuario = request.POST.get('inputEmail')
        senhausuario = request.POST.get('inputPassword')

        
        
        try:
                if Usuario.objects.get(email = emailusuario) and Usuario.objects.get(senha = senhausuario):
                        return redirect('/sistema/cadastro/')
                else:
                        contexto = {'erro':'senha errada'}
                        return redirect('/')
        except Exception as error:
                contexto = {'erro': 'usuario nao existe'}
                return redirect('/')
        

        
    
def sair(request):
        return redirect('/')




    
