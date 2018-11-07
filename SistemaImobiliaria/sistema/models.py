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
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to='clientes_fotos', null=True, blank=True)
     
    def __str__(self):
        return self.nome
