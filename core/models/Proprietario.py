from django.db import models

class Proprietario(models.Model):
    #id_proprietario = models.IntegerField(primary_key=True)
    nome_proprietario = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proprietario'
