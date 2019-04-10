from django.db import models
from .cliente import Cliente
from .imovel import Imovel
from .propietario import Propietario
from .corretor import Corretor

class Endereco(models.Model):
    id_endereco = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_imovel = models.ForeignKey('Imovel', models.DO_NOTHING, db_column='id_imovel', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'endereco'