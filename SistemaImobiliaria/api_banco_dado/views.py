from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from api_banco_dado.serializers.accounts_serializer import AccountSerializer
from api_banco_dado.serializers.aluguel_serializer import AluguelSerializer
from api_banco_dado.serializers.boleto_serializer import BoletoSerializer
from api_banco_dado.serializers.client_serializer import ClientSerializer
from api_banco_dado.serializers.contato_serializer import ContatoSerializer
from api_banco_dado.serializers.corretor_serializer import CorretorSerializer
from api_banco_dado.serializers.endereco_serializer import EnderecoSerializer
from api_banco_dado.serializers.imovel_serializer import ImovelSerializer
from api_banco_dado.serializers.mensagem_serializer import MensagemSerializer
from api_banco_dado.serializers.proprietario_serializer import ProprietarioSerializer
from api_banco_dado.serializers.venda_serializer import VendaSerializer
from core.models.Accounts import Usuario
from core.models.Aluguel import Aluguel
from core.models.Boleto import Boleto
from core.models.Cliente import Cliente
from core.models.Contato import Contato
from core.models.Corretor import Corretor
from core.models.Endereco import Endereco
from core.models.Imovel import Imovel
from core.models.Mensagens import Mensagens
from core.models.Proprietario import Proprietario
from core.models.Venda import Venda

# Start accounts views
# TODO: accounts should return senha encrypted.
@api_view(['GET', 'POST'])
def accounts_list(request):
    if request.method == "GET":
        contas = Usuario.objects.all()
        serializer = AccountSerializer(contas, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = AccountSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def account_detail(request, pk):
    try:
        conta = Usuario.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AccountSerializer(conta)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = AccountSerializer(conta, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        conta.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



# Start aluguel views
@api_view(['GET', 'POST'])
def alugueis_list(request):
    if request.method == "GET":
        alugueis = Aluguel.objects.all()
        serializer = AluguelSerializer(alugueis, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = AluguelSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def aluguel_detail(request, pk):
    try:
        aluguel = Aluguel.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AluguelSerializer(aluguel)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = AluguelSerializer(aluguel, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        aluguel.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Start boleto views
@api_view(['GET', 'POST'])
def boletos_list(request):
    if request.method == "GET":
        boletos = Boleto.objects.all()
        serializer = BoletoSerializer(boletos, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = BoletoSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def boleto_detail(request, pk):
    try:
        boleto = Boleto.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BoletoSerializer(boleto)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = BoletoSerializer(boleto, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        boleto.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Start cliente views
@api_view(['GET', 'POST'])
def clientes_list(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        serializer = ClientSerializer(clientes, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = ClientSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cliente_detail(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ClientSerializer(cliente)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = ClientSerializer(cliente, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        cliente.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Start contato views
@api_view(['GET', 'POST'])
def contatos_list(request):
    if request.method == "GET":
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(contatos, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = ContatoSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def contato_detail(request, pk):
    try:
        contato = Contato.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ContatoSerializer(contato)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = ContatoSerializer(contato, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        contato.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Start corretor views
@api_view(['GET', 'POST'])
def corretores_list(request):
    if request.method == "GET":
        corretores = Corretor.objects.all()
        serializer = CorretorSerializer(corretores, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = CorretorSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def corretor_detail(request, pk):
    try:
        corretor = Corretor.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CorretorSerializer(corretor)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = CorretorSerializer(corretor, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        corretor.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Start endereco views
@api_view(['GET', 'POST'])
def enderecos_list(request):
    if request.method == "GET":
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = EnderecoSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def endereco_detail(request, pk):
    try:
        endereco = Endereco.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = EnderecoSerializer(endereco)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = EnderecoSerializer(endereco, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        endereco.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Start imoveis views
@api_view(['GET', 'POST'])
def imoveis_list(request):
    if request.method == "GET":
        imoveis = Imoveis.objects.all()
        serializer = ImovelSerializer(imoveis, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = ImovelSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def imovel_detail(request, pk):
    try:
        imovel = Imovel.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ImovelSerializer(imovel)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = ImovelSerializer(imovel, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        imovel.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Start mensagens views
@api_view(['GET', 'POST'])
def mensagens_list(request):
    if request.method == "GET":
        mensagens = Mensagens.objects.all()
        serializer = MensagemSerializer(mensagens, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = MensagemSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mensagem_detail(request, pk):
    try:
        mensagem = Mensagens.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = MensagemSerializer(mensagem)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = MensagemSerializer(mensagem, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        mensagem.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Start proprietario views
@api_view(['GET', 'POST'])
def proprietarios_list(request):
    if request.method == "GET":
        proprietarios = Proprietario.objects.all()
        serializer = ProprietarioSerializer(proprietarios, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = ProprietarioSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proprietario_detail(request, pk):
    try:
        proprietario = Proprietario.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = MensagemSerializer(proprietario)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = ProprietarioSerializer(proprietario, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        proprietario.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Start venda views
@api_view(['GET', 'POST'])
def vendas_list(request):
    if request.method == "GET":
        vendas = Venda.objects.all()
        serializer = VendaSerializer(vendas, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        dado = JSONParser().parse(request)
        serializer = VendaSerializer(data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def venda_detail(request, pk):
    try:
        venda = Venda.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = VendaSerializer(venda)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        serializer = VendaSerializer(venda, data=dado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        venda.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



