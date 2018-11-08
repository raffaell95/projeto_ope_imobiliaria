from django.shortcuts import render, redirect
from sistema.models import Clientes, Imoveis
from login.models import Usuario

# Create your views here.
def homeSistema(request):
    
    return render(request, 'home-sistema.html')

def cadastro(request):
    contexto = {
            'clientes': Clientes.objects.all(),
            'imoveis' : Imoveis.objects.all(),
            'usuarios': Usuario.objects.all()
    }
    return render(request, 'cadastro.html', contexto)

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


def incluirUsuario(request):

    if request.POST:
        Usuario.objects.create(
        nome = request.POST.get('nome'),
        email = request.POST.get('email'),
        senha = request.POST.get('senha'),
        
        )
        return redirect('/sistema/cadastro/')


def incluirImovel(request):

    if request.POST:
        Imoveis.objects.create(
        nome_responsavel = request.POST.get('nome_responsavel'),
        celular_responsavel = request.POST.get('celular_responsavel'),
        endereco = request.POST.get('endereco'),
        cep = request.POST.get('cep'),
        valor_compra = request.POST.get('valor_compra'),
        valor_aluguel = request.POST.get('valor_aluguel'),
        descricao_imovel = request.POST.get('descricao_imovel')
        )
        return redirect('/sistema/cadastro/')

                
