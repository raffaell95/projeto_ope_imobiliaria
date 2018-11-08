from django.db import models

class Clientes(models.Model):
    
    nome = models.CharField(max_length=150,blank=True)
    idade = models.IntegerField(null=True,blank=True)
    celular = models.IntegerField(null=True)
    email = models.CharField(max_length=60,blank=True)
    cep = models.IntegerField(blank=True)
    endereco = models.CharField(max_length=150,blank=True)
    rg = models.IntegerField(blank=True)
    cpf = models.IntegerField(blank=True)
     
    def __str__(self):
        return self.nome


class Imoveis(models.Model):
    
    nome_responsavel = models.CharField(max_length=150,blank=True)
    celular_responsavel = models.IntegerField(null=True)
    endereco = models.CharField(max_length=150,blank=True)
    cep = models.IntegerField(blank=True)
    valor_compra = models.CharField(max_length=150,blank=True)
    valor_aluguel = models.CharField(max_length=150,blank=True)
    descricao_imovel = models.TextField(blank=True)


    def __str__(self):
        return self.nome_responsavel

