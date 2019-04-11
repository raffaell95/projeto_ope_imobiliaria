from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nome_cliente = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cliente'
