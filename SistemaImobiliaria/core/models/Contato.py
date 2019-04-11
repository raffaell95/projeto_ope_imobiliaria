from django.db import models
from .Cliente import Cliente


class Contato(models.Model):
    id_contato = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    proprietario = models.ForeignKey('Proprietario', models.DO_NOTHING, db_column='proprietario', blank=True, null=True)
    id_corretor = models.ForeignKey('Corretor', models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contato'