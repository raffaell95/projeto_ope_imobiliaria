from django.db import models
from .Cliente import Cliente


class Corretor(models.Model):
    #id_corretor = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)
    registro = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'corretor'