from django.db import models
from .Cliente import Cliente
from .Proprietario import Proprietario

class Imovel(models.Model):
    id_imovel = models.IntegerField(primary_key=True)  # Field name made lowercase.
    id_proprietario = models.ForeignKey('Proprietario', models.DO_NOTHING, db_column='id_proprietario', blank=True, null=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    matricula = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    iptu = models.CharField(max_length=100, blank=True, null=True)
    metro_quadrado = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'imovel'

