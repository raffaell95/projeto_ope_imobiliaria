from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from core.mail import send_mail_template
from django.shortcuts import render, redirect
from core.models.Accounts import Usuario

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
