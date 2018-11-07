from django.shortcuts import render, redirect
from sistema.models import Clientes

# Create your views here.
def homeSistema(request):
    
    return render(request, 'home-sistema.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def incluirCliente(request):
    if request.POST:

        Clientes.objects.create(
            nome = request.POST.get('nome'),
            idade = request.POST.get('idade'),
            celular = request.POST.get('celular'),
            email = request.POST.get('email'),
            cep = request.POST.get('cep'),
            endereco = request.POST.get('endereco'),
            rg = request.POST.get('rg'),
            cpf = request.POST.get('cpf'),
            descricao = request.POST.get('descricao'),
            foto = request.POST.get('foto'),
        )
        return redirect('/sistema/cadastro/')