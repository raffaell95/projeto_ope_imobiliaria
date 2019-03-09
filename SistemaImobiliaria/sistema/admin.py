from django.contrib import admin
from .models import Imoveis, Clientes


class ImovelAdmin(admin.ModelAdmin):
    list_display = ['nome_responsavel', 'celular_responsavel', 'endereco', 'cep', 'valor_compra', 'valor_aluguel', 'descricao_imovel']
    search_fields = ['nome_responsavel', 'cep']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'celular', 'email', 'cep', 'endereco', 'cpf']
    search_fields = ['nome', 'cpf']

admin.site.register(Imoveis, ImovelAdmin)
admin.site.register(Clientes, ClienteAdmin)