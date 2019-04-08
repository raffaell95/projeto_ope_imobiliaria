from django.shortcuts import render, redirect


# Create your views here.


def homeSistema(request):

    return render(request, 'home-sistema.html')


def cadastro(request):
    
    return render(request, 'cadastro.html')


def incluirCliente(request):
    
        return redirect('/sistema/cadastro/')


def incluirUsuario(request):

   
        return redirect('/sistema/cadastro/')


def incluirImovel(request):

    
        return redirect('/sistema/cadastro/')


      
       

def alterarUsuario(request, id):

       
        return render(request, 'alterar-usuario.html')


def removerCliente(request, id):
   
    return render(request, 'home.html')


def removerImovel(request, id):
    
        

    return render(request, 'home.html')


def removerUsuario(request, id):
    

    return render(request, 'home.html')

