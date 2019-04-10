from django.db import models

class Propietario(models.Model):
    id_propietario = models.IntegerField(primary_key=True)
    nome_propietario = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'propietario'
