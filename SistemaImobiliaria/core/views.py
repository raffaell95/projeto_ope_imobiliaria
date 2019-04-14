from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from core.mail import send_mail_template
from django.shortcuts import render, redirect
from core.models.Accounts import Usuario
import requests

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
    # TODO: END-POINT API PARA RETORNAR
    # TODOS DADOS DO CLIENTE NECESSARIOS 
    # DA PAGINA, SEM FOREIGN KEYS DE OUTRAS
    # TABELAS E IDS 

    clientes = []
    url = "http://localhost:8000/api/cliente/"
    todos_clientes = requests.api.get(url).json()
    for i in todos_clientes:
        url_endereco = f"http://localhost:8000/api/endereco/{i['id']}"
        url_contato = f"http://localhost:8000/api/contato/{i['id']}"
        endereco = requests.api.get(url_endereco).json()
        contato = requests.api.get(url_contato).json()
        
        # DELETANDO DADOS DESNECESSARIOS
        del i["id"]
        del endereco["id_cliente"], endereco["id_corretor"], endereco["id_imovel"], endereco["id"]
        del contato["id_cliente"], contato["id_corretor"], contato["id"]

        clientes.append({**i, **endereco, **contato})
        
    context = {
        'clientes': clientes
    }

    if request.method == "POST":
        cliente = {}
        cliente['nome'] = request.POST.get("nome")
        cliente['cpf'] =request.POST.get("cpf")
        cliente['endereco'] =request.POST.get("endereco")
        cliente['bairro'] =request.POST.get("bairro")
        cliente['cep'] =request.POST.get("cep")
        cliente['estado'] =request.POST.get("estado")
        cliente['uf'] =request.POST.get("uf")
        cliente['email'] =request.POST.get("email")
        cliente['telefone'] = request.POST.get("telefone")
        url = "http://localhost:8000/api/cliente/"

        retorno_api = requests.api.post(url, json=cliente).json()
        return HttpResponse(retorno_api)

    return render(request, 'sistema/clientes.html', context)

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
                'title': 'Premium Visa',
                'email_msg': 'Enviado com sucesso'
            }
            return render(request, 'index.html', context)
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
