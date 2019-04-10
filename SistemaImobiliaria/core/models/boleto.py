from django.db import models
from .aluguel import Aluguel
from .venda import Venda
from .cliente import Cliente
from .propietario import Propietario



class Boleto(models.Model):
    id_boleto = models.IntegerField(primary_key=True)
    id_aluguel = models.ForeignKey(Aluguel, models.DO_NOTHING, db_column='id_aluguel', blank=True, null=True)
    id_venda = models.ForeignKey('Venda', models.DO_NOTHING, db_column='id_venda', blank=True, null=True)
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    valor_boleto = models.FloatField(blank=True, null=True)
    multa_juros = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'boleto'