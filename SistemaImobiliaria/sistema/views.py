from django.shortcuts import render, redirect
from sistema.models import Clientes, Imoveis
from login.models import Usuario

# Create your views here.


def homeSistema(request):

    return render(request, 'home-sistema.html')


def cadastro(request):
    contexto = {
            'clientes': Clientes.objects.all(),
            'imoveis': Imoveis.objects.all(),
            'usuarios': Usuario.objects.all()
    }
    return render(request, 'cadastro.html', contexto)


def incluirCliente(request):
    if request.POST:

        Clientes.objects.create(
            nome=request.POST.get('nome'),
            idade=request.POST.get('idade'),
            celular=request.POST.get('celular'),
            email=request.POST.get('email'),
            cep=request.POST.get('cep'),
            endereco=request.POST.get('endereco'),
            rg=request.POST.get('rg'),
            cpf=request.POST.get('cpf'),
            descricao=request.POST.get('descricao'),
        )
        return redirect('/sistema/cadastro/')


def incluirUsuario(request):

    if request.POST:
        Usuario.objects.create(
        nome=request.POST.get('nome'),
        email=request.POST.get('email'),
        senha=request.POST.get('senha'),

        )
        return redirect('/sistema/cadastro/')


def incluirImovel(request):

    if request.POST:
        Imoveis.objects.create(
        nome_responsavel=request.POST.get('nome_responsavel'),
        celular_responsavel=request.POST.get('celular_responsavel'),
        endereco=request.POST.get('endereco'),
        cep=request.POST.get('cep'),
        valor_compra=request.POST.get('valor_compra'),
        valor_aluguel=request.POST.get('valor_aluguel'),
        descricao_imovel=request.POST.get('descricao_imovel')
        )
        return redirect('/sistema/cadastro/')


def alterarCliente(request, id):

        contexto = {
                'cliente': Clientes.objects.get(id=id)
        }

        if request.POST:

                cliente = Clientes.objects.get(id=id)

                cliente.nome = request.POST.get('nome')
                cliente.idade = request.POST.get('idade')
                cliente.celular = request.POST.get('celular')
                cliente.email = request.POST.get('email')
                cliente.cep = request.POST.get('cep')
                cliente.endereco = request.POST.get('endereco')
                cliente.rg = request.POST.get('rg')
                cliente.cpf = request.POST.get('cpf')
                cliente.descricao = request.POST.get('descricao')

                cliente.save()

                return redirect('/sistema/cadastro/')

        return render(request, 'alterar-cliente.html', contexto)


def alterarImovel(request, id):

        contexto = {
                'imovel': Imoveis.objects.get(id=id)
        }

        if request.POST:

                imovel = Imoveis.objects.get(id=id)
                imovel.nome_responsavel = request.POST.get('nome_responsavel')
              
                imovel.celular_responsavel = request.POST.get('celular_responsavel')
                imovel.endereco = request.POST.get('endereco')
                imovel.cep = request.POST.get('cep')
                imovel.valor_compra = request.POST.get('valor_compra')
                imovel.valor_aluguel = request.POST.get('valor_aluguel')
                imovel.descricao_imovel = request.POST.get('descricao_imovel')
                        
                imovel.save()

                return redirect('/sistema/cadastro/')

        return render(request, 'alterar-imovel.html', contexto)


def alterarUsuario(request, id):

        contexto = {
                'usuario': Usuario.objects.get(id=id)
        }

        if request.POST:

                usuario = Usuario.objects.get(id=id)
                usuario.nome = request.POST.get('nome')
                usuario.email = request.POST.get('email')
                usuario.senha = request.POST.get('senha')
        
                usuario.save()

                return redirect('/sistema/cadastro/')

        return render(request, 'alterar-usuario.html', contexto)


def removerCliente(request, id):
    contexto = {
        'cliente': Clientes.objects.all(),
    }
    
    if request.method == 'GET':
        a = Clientes.objects.filter(id=id).delete()
  
        return redirect('/sistema/cadastro/')

    return render(request, 'home.html', contexto)


def removerImovel(request, id):
    contexto = {
        'imovel': Imoveis.objects.all(),
    }
    
    if request.method == 'GET':
        a = Imoveis.objects.filter(id=id).delete()
  
        return redirect('/sistema/cadastro/')

    return render(request, 'home.html', contexto)


def removerUsuario(request, id):
    contexto = {
        'usuario': Usuario.objects.all(),
    }
    
    if request.method == 'GET':
        a = Usuario.objects.filter(id=id).delete()
  
        return redirect('/sistema/cadastro/')

    return render(request, 'home.html', contexto)

