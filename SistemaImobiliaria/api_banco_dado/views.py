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
def endereco_detail(request, pk, tipo):
    try:
        if tipo == "proprietario":
            endereco = Endereco.objects.get(id_proprietario=pk)
        elif tipo == "cliente":
            endereco = Endereco.objects.get(id_cliente=pk)
        elif tipo == "imovel":
            endereco = Endereco.objects.get(id_imovel=pk)
        elif tipo == "corretor":
            endereco = Endereco.objects.get(id_corretor=pk)
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



# Start cadastro cliente views
@api_view(['GET', 'POST'])
def clientes_list(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        serializer = ClientSerializer(clientes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        dado = JSONParser().parse(request)
        cliente = ClientSerializer(data=dado)
        if cliente.is_valid():
            cliente.save()
            dado['id_cliente'] = cliente.data['id']
            endereco = EnderecoSerializer(data=dado)
            contato = ContatoSerializer(data=dado)
            if endereco.is_valid() and contato.is_valid():
                endereco.save()
                contato.save()
                cliente_dados = {}
                cliente_dados['cliente'] = cliente.data
                cliente_dados['endereco'] = endereco.data
                cliente_dados['contato'] = contato.data
                return JsonResponse(cliente_dados, status=status.HTTP_201_CREATED)
            else:
                cliente_error = {}
                cliente_error['cliente'] = cliente.errors
                cliente_error['endereco'] = endereco.errors
                cliente_error['contato'] = contato.errors
                return JsonResponse(cliente_error, status=status.HTTP_400_BAD_REQUEST)
            
        return JsonResponse(cliente.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cliente_detail(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
        endereco = Endereco.objects.get(id_cliente=pk)
        contato = Contato.objects.get(id_cliente=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        cliente = ClientSerializer(cliente)
        return JsonResponse(cliente.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        print(dado)
        cliente = ClientSerializer(cliente, data=dado)
        if cliente.is_valid():
            cliente.save()
            endereco = EnderecoSerializer(endereco, data=dado)
            contato = ContatoSerializer(contato, data=dado)
            if endereco.is_valid() and contato.is_valid():
                endereco.save()
                contato.save()
                cliente_dados = {}
                cliente_dados['cliente'] = cliente.data
                cliente_dados['endereco'] = endereco.data
                cliente_dados['contato'] = contato.data
                return JsonResponse(cliente_dados)
            else:
                cliente_error = {}
                cliente_error['cliente'] = cliente.errors
                cliente_error['endereco'] = endereco.errors
                cliente_error['contato'] = contato.errors
                return JsonResponse(cliente_error, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        cliente.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Start cadastro proprietario views
@api_view(['GET', 'POST'])
def proprietarios_list(request):
    if request.method == "GET":
        proprietarios = Proprietario.objects.all()
        serializer = ProprietarioSerializer(proprietarios, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        dado = JSONParser().parse(request)
        proprietario = ProprietarioSerializer(data=dado)

        if proprietario.is_valid():
            proprietario.save()
            dado['id_proprietario'] = proprietario.data['id']
            endereco = EnderecoSerializer(data=dado)
            contato = ContatoSerializer(data=dado)

            if endereco.is_valid() and contato.is_valid():
                endereco.save()
                contato.save()
                proprietario_dados = {}
                proprietario_dados['proprietario'] = proprietario.data
                proprietario_dados['endereco'] = endereco.data
                proprietario_dados['contato'] = contato.data

                return JsonResponse(proprietario_dados, status=status.HTTP_201_CREATED)
                
            else:
                proprietario_error = {}
                proprietario_error['proprietario'] = proprietario.errors
                proprietario_error['endereco'] = endereco.errors
                proprietario_error['contato'] = contato.errors

                return JsonResponse(proprietario_error, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(cliente.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proprietario_detail(request, pk):
    try:
        proprietario = Proprietario.objects.get(pk=pk)
        endereco = Endereco.objects.get(id_proprietario=pk)
        contato = Contato.objects.get(id_proprietario=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = MensagemSerializer(proprietario)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        proprietario = ProprietarioSerializer(proprietario, data=dado)

        if proprietario.is_valid():
            proprietario.save()
            endereco = EnderecoSerializer(data=dado)
            contato = ContatoSerializer(data=dado)

            if endereco.is_valid() and contato.is_valid():
                endereco.save()
                contato.save()
                proprietario_dados = {}
                proprietario_dados['proprietario'] = proprietario.data
                proprietario_dados['endereco'] = endereco.data
                proprietario_dados['contato'] = contato.data

                return JsonResponse(proprietario_dados, status=status.HTTP_201_CREATED)

            else:
                proprietario_error = {}
                proprietario_error['proprietario'] = proprietario.errors
                proprietario_error['endereco'] = endereco.errors
                proprietario_error['contato'] = contato.errors

                return JsonResponse(proprietario_error, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        proprietario.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Start cadastro corretor views
@api_view(['GET', 'POST'])
def corretores_list(request):
    if request.method == "GET":
        corretores = Corretor.objects.all()
        serializer = CorretorSerializer(corretores, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        dado = JSONParser().parse(request)
        corretor = CorretorSerializer(data=dado)
        if corretor.is_valid():
            corretor.save()
            dado['id_corretor'] = corretor.data['id']
            endereco = EnderecoSerializer(data=dado)
            contato = ContatoSerializer(data=dado)
            if endereco.is_valid() and contato.is_valid():
                endereco.save()
                contato.save()
                corretor_dados = {}
                corretor_dados['proprietario'] = cliente.data
                corretor_dados['endereco'] = endereco.data
                corretor_dados['contato'] = contato.data
                return JsonResponse(corretor_dados, status=status.HTTP_201_CREATED)
            else:
                corretor_error = {}
                corretor_error['proprietario'] = cliente.errors
                corretor_error['endereco'] = endereco.errors
                corretor_error['contato'] = contato.errors
                return JsonResponse(corretor_error, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(corretor.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def corretor_detail(request, pk):
    try:
        corretor = Corretor.objects.get(pk=pk)
        endereco = Endereco.objects.get(id_corretor=pk)
        contato = Contato.objects.get(id_corretor=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        corretor = CorretorSerializer(corretor)
        return JsonResponse(corretor.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        corretor = CorretorSerializer(corretor, data=dado)
        if corretor.is_valid():
            corretor.save()
            endereco = EnderecoSerializer(endereco, data=dado)
            contato = ContatoSerializer(contato, data=dado)
            if endereco.is_valid() and contato.is_valid():
                endereco.save()
                contato.save()
                corretor_dados = {}
                corretor_dados['proprietario'] = corretor.data
                corretor_dados['endereco'] = endereco.data
                corretor_dados['contato'] = contato.data

                return JsonResponse(corretor_dados, status=status.HTTP_201_CREATED)

            else:
                corretor_error = {}
                corretor_error['proprietario'] = corretor.errors
                corretor_error['endereco'] = endereco.errors
                corretor_error['contato'] = contato.errors

                return JsonResponse(corretor_error, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        corretor.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Start cadastro imovel views
@api_view(['GET', 'POST'])
def imoveis_list(request):
    if request.method == "GET":
        imoveis = Imovel.objects.all()
        serializer = ImovelSerializer(imoveis, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        dado = JSONParser().parse(request)
        imovel = ImovelSerializer(data=dado)
        if imovel.is_valid():
            imovel.save()
            dado['id_imovel'] = imovel.data['id']
            endereco = EnderecoSerializer(data=dado)
            if endereco.is_valid():
                endereco.save()
                imovel_dados = {}
                imovel_dados['proprietario'] = imovel.data
                imovel_dados['endereco'] = endereco.data
                return JsonResponse(imovel_dados, status=status.HTTP_201_CREATED)
            else:
                imovel_error = {}
                imovel_error['proprietario'] = imovel.errors
                imovel_error['endereco'] = endereco.errors
                return JsonResponse(imovel_error, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(imovel.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def imovel_detail(request, pk):
    try:
        imovel = Imovel.objects.get(pk=pk)
        endereco = Endereco.objects.get(id_imovel=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        imovel = ImovelSerializer(imovel)
        return JsonResponse(imovel.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        imovel = ImovelSerializer(imovel, data=dado)
        if imovel.is_valid():
            imovel.save()
            endereco = EnderecoSerializer(endereco, data=dado)
            if endereco.is_valid():
                endereco.save()
                imovel_dados = {}
                imovel_dados['proprietario'] = imovel.data
                imovel_dados['endereco'] = endereco.data

                return JsonResponse(imovel_dados, status=status.HTTP_201_CREATED)

            else:
                imovel_error = {}
                imovel_error['proprietario'] = imovel.errors
                imovel_error['endereco'] = endereco.errors

                return JsonResponse(imovel_error, status=status.HTTP_400_BAD_REQUEST)
                
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        imovel.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)