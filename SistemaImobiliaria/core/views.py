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
           
           
def sair(request):
    logout(request)
    
    return redirect('/')

def registrar(request):
    
    return redirect('/')


def home_sistema(request):

    return render(request, 'sistema/index.html')


def cadastro(request):
    
    return render(request, 'sistema/cadastro.html')

def atualizar_view_cliente(request, pk):
    url_cliente = f"http://localhost:8000/api/cliente/{pk}"
    url_endereco = f"http://localhost:8000/api/endereco/{pk}/cliente"
    url_contato = f"http://localhost:8000/api/contato/{pk}"
    cliente = requests.api.get(url_cliente).json()
    endereco = requests.api.get(url_endereco).json()
    contato = requests.api.get(url_contato).json()

    dados_cliente = {**cliente, **endereco, ** contato}

    return JsonResponse(dados_cliente)

def delete_cliente(request, pk):
    url = f"http://localhost:8000/api/cliente/{pk}"
    requests.api.delete(url)

    return redirect('/cadastro/clientes')

def cadastro_clientes(request):
    clientes = []
    url = "http://localhost:8000/api/cliente/"
    todos_clientes = requests.api.get(url).json()
    for i in todos_clientes:
        url_endereco = f"http://localhost:8000/api/endereco/{i['id']}/cliente"
        url_contato = f"http://localhost:8000/api/contato/{i['id']}"
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

def cadastro_imoveis(request):
    url = "http://localhost:8000/api/imovel/"
    todos_imoveis = requests.api.get(url).json()
    url_proprietario = "http://localhost:8000/api/proprietario/"
    todos_proprietarios = requests.api.get(url_proprietario).json()
    imoveis = []
    for i in todos_imoveis:
        url_endereco = f"http://localhost:8000/api/endereco/{i['id']}/imovel"
        url_contato = f"http://localhost:8000/api/contato/{i['id_proprietario']}"
        endereco = requests.api.get(url_endereco).json()
        contato = requests.api.get(url_contato).json()
        del endereco["id_cliente"], endereco["id_corretor"], endereco["id_imovel"], endereco["id"], endereco["id_proprietario"]
        del contato["id_cliente"], contato["id_corretor"], contato["id"], contato["id_proprietario"]

        imoveis.append({**i, **endereco, **contato})
        
    contexto = {
        'proprietarios': todos_proprietarios,
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
        url = 'http://localhost:8000/api/imovel'
        retorno_api = requests.api.post(url, json=imovel).json()

        return redirect('/cadastro/clientes')


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
