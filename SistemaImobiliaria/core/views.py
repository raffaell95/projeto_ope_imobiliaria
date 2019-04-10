from django.shortcuts import render, redirect
from .models.acounts import Usuario



def login(request):

        return render(request, 'login.html')


def entrar(request):
        emailusuario = request.POST.get('inputEmail')
        senhausuario = request.POST.get('inputPassword')

        try:
                if Usuario.objects.get(email = emailusuario) and Usuario.objects.get(senha = senhausuario):
                        return redirect('/cadastro/')
                else:
                        contexto = {'erro':'senha errada'}
                        return redirect('/')
        except Exception as error:
                contexto = {'erro': 'usuario nao existe'}
                return redirect('/')
           
def sair(request):
        return redirect('/')




def homeSistema(request):

    return render(request, 'sistema/home-sistema.html')


def cadastro(request):
    
    return render(request, 'sistema/cadastro.html')


def cadastroClientes(request):
    
    return render(request, 'sistema/clientes.html')