from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from core.mail import send_mail_template
from django.shortcuts import render, redirect
from core.models.Accounts import Usuario
from django.http import JsonResponse
import requests

def home(request):
    return render(request, 'index.html')

def sair(request):
    logout(request)
    return redirect('/')

def registrar(request):
    return redirect('/')

def home_sistema(request):
    url = "http://localhost:8000/api/imovel/"
    todos_imoveis = requests.api.get(url).json()
    imoveis = []
    for i in todos_imoveis:
        url_endereco = f"http://localhost:8000/api/endereco/{i['id']}/imovel"
        endereco = requests.api.get(url_endereco).json()
    contexto = {
        'imoveis': imoveis
    }    
    return render(request, 'sistema/index.html', contexto)

def cadastro(request):
    return render(request, 'sistema/cadastro.html')

def login_page(request):
    context = {
        'error_msg': ''
    }
    
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_URL_REDIRECT)
        else:
            context = {
                'error_msg': 'Senha e/ou usuário inválido.'
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)
           
           


def atualizar_view_cliente(request, pk):
    url_cliente = f"http://localhost:8000/api/cliente/{pk}"
    url_endereco = f"http://localhost:8000/api/endereco/{pk}/cliente"
    url_contato = f"http://localhost:8000/api/contato/{pk}/contato"
    cliente = requests.api.get(url_cliente).json()
    endereco = requests.api.get(url_endereco).json()
    contato = requests.api.get(url_contato).json()

    dados_cliente = {**cliente, **endereco, ** contato}

    return JsonResponse(dados_cliente)

def atualizar_view_imovel(request, pk):
    url_imovel = f"http://localhost:8000/api/imovel/{pk}"
    url_endereco = f"http://localhost:8000/api/endereco/{pk}/imovel"
    imovel = requests.api.get(url_imovel).json()
    endereco = requests.api.get(url_endereco).json()

    dados_imovel = {**imovel, **endereco}
    
    return JsonResponse(dados_imovel)

def atualizar_view_proprietario(request, pk):
    url_proprietario = f"http://localhost:8000/api/proprietario/{pk}"
    url_endereco = f"http://localhost:8000/api/endereco/{pk}/proprietario"
    url_contato = f"http://localhost:8000/api/contato/{pk}/proprietario"
    proprietario = requests.api.get(url_proprietario).json()
    endereco = requests.api.get(url_endereco).json()
    contato = requests.api.get(url_contato).json()

    dados_proprietario = {**proprietario, **endereco, ** contato}

    return JsonResponse(dados_proprietario)

def delete_cliente(request, pk):
    url = f"http://localhost:8000/api/cliente/{pk}"
    requests.api.delete(url)

    return redirect('/cadastro/clientes')

def delete_corretor(request, pk):
    url = f"http://localhost:8000/api/corretor/{pk}"
    requests.api.delete(url)

    return redirect('/cadastro/corretores')

def delete_imovel(request, pk):
    url = f"http://localhost:8000/api/imovel/{pk}"
    requests.api.delete(url)

    return redirect('/cadastro/imoveis')

def delete_proprietario(request, pk):
    url = f"http://localhost:8000/api/proprietario/{pk}"
    requests.api.delete(url)

    return redirect('/cadastro/proprietarios')

def cadastro_clientes(request):
    clientes = []
    url = "http://localhost:8000/api/cliente/"
    todos_clientes = requests.api.get(url).json()
    for i in todos_clientes:
        url_endereco = f"http://localhost:8000/api/endereco/{i['id']}/cliente"
        url_contato = f"http://localhost:8000/api/contato/{i['id']}/cliente"
        endereco = requests.api.get(url_endereco).json()
        contato = requests.api.get(url_contato).json()
        del endereco["id_cliente"], endereco["id_corretor"], endereco["id_imovel"], endereco["id"], endereco["id_proprietario"]
        del contato["id_cliente"], contato["id_corretor"], contato["id"], contato["id_proprietario"]

        clientes.append({**i, **endereco, **contato})
        
    context = {
        'clientes': clientes
    }

    if request.method == "POST":
        cliente = {}
        cliente['nome_cliente'] = request.POST.get("nome")
        cliente['cpf_cnpj'] = request.POST.get("cpf")
        cliente['endereco'] = request.POST.get("endereco")
        cliente['bairro'] = request.POST.get("bairro")
        cliente['cep'] = request.POST.get("cep")
        cliente['cidade'] = request.POST.get("cidade")
        cliente['uf'] = request.POST.get("uf")
        cliente['email'] = request.POST.get("email")
        cliente['telefone'] = request.POST.get("telefone")
        url = "http://localhost:8000/api/cliente/"
        retorno_api = requests.api.post(url, json=cliente).json()

        return redirect('/cadastro/clientes')

    return render(request, 'sistema/clientes.html', context)

def cadastro_proprietario(request):
    proprietarios = []
    url = "http://localhost:8000/api/proprietario/"
    todos_proprietarios = requests.api.get(url).json()
    for i in todos_proprietarios:
        url_endereco = f"http://localhost:8000/api/endereco/{i['id']}/proprietario"
        url_contato = f"http://localhost:8000/api/contato/{i['id']}/proprietario"
        endereco = requests.api.get(url_endereco).json()
        contato = requests.api.get(url_contato).json()
        del endereco["id_cliente"], endereco["id_corretor"], endereco["id_imovel"], endereco["id"], endereco["id_proprietario"]
        del contato["id_cliente"], contato["id_corretor"], contato["id"], contato["id_proprietario"]

        proprietarios.append({**i, **endereco, **contato})
        
    context = {
        'proprietarios': proprietarios
    }

    if request.method == "POST":
        proprietario = {}
        proprietario['nome_proprietario'] = request.POST.get("nome")
        proprietario['cpf'] = request.POST.get("cpf")
        proprietario['endereco'] = request.POST.get("endereco")
        proprietario['bairro'] = request.POST.get("bairro")
        proprietario['cep'] = request.POST.get("cep")
        proprietario['cidade'] = request.POST.get("cidade")
        proprietario['uf'] = request.POST.get("uf")
        proprietario['email'] = request.POST.get("email")
        proprietario['telefone'] = request.POST.get("telefone")
        url = "http://localhost:8000/api/proprietario/"
        retorno_api = requests.api.post(url, json=proprietario).json()

        return redirect('/cadastro/proprietarios')

    return render(request, 'sistema/proprietarios.html', context)

def cadastro_corretores(request):
    corretores = []
    url = "http://localhost:8000/api/corretor/"
    todos_corretores = requests.api.get(url).json()
    for i in todos_corretores:
        url_endereco = f"http://localhost:8000/api/endereco/{i['id']}/corretor"
        url_contato = f"http://localhost:8000/api/contato/{i['id']}/corretor"
        endereco = requests.api.get(url_endereco).json()
        contato = requests.api.get(url_contato).json()
        del endereco["id_cliente"], endereco["id_corretor"], endereco["id_imovel"], endereco["id"], endereco["id_proprietario"]
        del contato["id_cliente"], contato["id_corretor"], contato["id"], contato["id_proprietario"]

        corretores.append({**i, **endereco, **contato})
        
    context = {
        'corretores': corretores
    }

    if request.method == "POST":
        corretor = {}
        corretor['nome'] = request.POST.get("nome")
        corretor['registro'] = request.POST.get("registro")
        corretor['id_clientes'] = request.POST.get("id_cliente")
        corretor['cpf_cnpj'] = request.POST.get("cpf")
        corretor['endereco'] = request.POST.get("endereco")
        corretor['bairro'] = request.POST.get("bairro")
        corretor['cep'] = request.POST.get("cep")
        corretor['cidade'] = request.POST.get("cidade")
        corretor['uf'] = request.POST.get("uf")
        corretor['email'] = request.POST.get("email")
        corretor['telefone'] = request.POST.get("telefone")
        url = "http://localhost:8000/api/corretor/"
        retorno_api = requests.api.post(url, json=corretor).json()

        return redirect('/cadastro/corretores')

    return render(request, 'sistema/corretores.html', context)

def cadastro_imoveis(request):
    url = "http://localhost:8000/api/imovel/"
    todos_imoveis = requests.api.get(url).json()
    url_proprietario = "http://localhost:8000/api/proprietario/"
    todos_proprietarios = requests.api.get(url_proprietario).json()
    url_cliente = "http://localhost:8000/api/cliente/"
    todos_clientes = requests.api.get(url_cliente).json()
    imoveis = []
    for i in todos_imoveis:
        url_endereco = f"http://localhost:8000/api/endereco/{i['id']}/imovel"
        url_contato = f"http://localhost:8000/api/contato/{i['id_proprietario']}/proprietario"
        endereco = requests.api.get(url_endereco).json()
        contato = requests.api.get(url_contato).json()
        del endereco["id_cliente"], endereco["id_corretor"], endereco["id_imovel"], endereco["id"], endereco["id_proprietario"]
        del contato["id_cliente"], contato["id_corretor"], contato["id"], contato["id_proprietario"]

        imoveis.append({**i, **endereco, **contato})
    
    contexto = {
        'proprietarios': todos_proprietarios,
        'clientes': todos_clientes,
        'imoveis': imoveis
    }


    if request.method == "POST":
        imovel = {}
        imovel['descricao'] = request.POST.get('descricao')
        imovel['id_proprietario'] = request.POST.get('id_proprietario')
        imovel['matricula'] = request.POST.get('matricula')
        imovel['iptu'] = request.POST.get('iptu')
        imovel['metro_quadrado'] = request.POST.get('metro_quadrado')
        imovel['endereco'] = request.POST.get('endereco')
        imovel['bairro'] = request.POST.get('bairro')
        imovel['cep'] = request.POST.get('cep')
        imovel['cidade'] = request.POST.get('cidade')
        imovel['uf'] = request.POST.get('uf')
        url = 'http://localhost:8000/api/imovel/'
        retorno_api = requests.api.post(url, json=imovel).json()

        return redirect('/cadastro/imoveis')

    return render(request, 'sistema/imoveis.html', contexto)


def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        contexto = {
            'name': request.POST.get('name', ''),
            'subject': subject,
            'from_email' : from_email,
            'message' : message
        }
        if subject and message and from_email:
            template_name = 'contatoEmail.html'
            send_mail_template(subject, template_name, contexto, from_email)
            context = {
                'title': 'SK imobiliaria',
                'email_msg': 'Enviado com sucesso'
            }
            return render(request, 'index.html', context)
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

def view_endereco_imovel(request, pk):
    url_endereco = f"http://localhost:8000/api/endereco/{pk}/imovel"
    endereco = requests.api.get(url_endereco).json()
    return JsonResponse(endereco)