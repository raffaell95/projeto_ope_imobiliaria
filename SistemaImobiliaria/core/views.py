from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from core.mail import send_mail_template


def home(request):
    
    return render(request, 'home.html')


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