from django.db import models
from django.http import JsonResponse
from core.models.imovel import Imovel
from core.models.proprietario import Proprietario

# Create your models here.
def create_cliente():
    pass

def create_corretor():
    pass


#queries proprietarios
def create_proprietario(request, nome, cpf_cnpj):
    proprietario = Proprietario(nome_proprietario=nome, cpf_cnpj=cpf_cnpj)
    proprietario.save()

def select_proprietario(request, cpf_cnpj):
    return JsonResponse(Proprietario.objects.filter(cpf_cnpj=cpf_cnpj))


#queries imoveis
def create_imovel():
    Imovel()