from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from api_banco_dado.serializers.cliente_serializer import ClienteSerializer
from api_banco_dado.serializers.corretor_serializer import CorretorSerializer
from api_banco_dado.serializers.imovel_serializer import ImovelSerializer
from api_banco_dado.serializers.proprietario_serializer import ProprietarioSerializer
from core.models.Cliente import Cliente
from core.models.Corretor import Corretor
from core.models.Imovel import Imovel
from core.models.Proprietario import Proprietario


# Start cadastro cliente views
@api_view(['GET', 'POST'])
def clientes_list(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        dado = JSONParser().parse(request)
        cliente = ClienteSerializer(data=dado)
        if cliente.is_valid():
            cliente.save()

        return JsonResponse(cliente.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cliente_detail(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        cliente = ClienteSerializer(cliente)
        return JsonResponse(cliente.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        print(dado)
        cliente = ClienteSerializer(cliente, data=dado)
        if cliente.is_valid():
            cliente.save()

        return JsonResponse(cliente.errors, status=status.HTTP_400_BAD_REQUEST)

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

        return JsonResponse(proprietario.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proprietario_detail(request, pk):
    try:
        proprietario = Proprietario.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProprietarioSerializer(proprietario)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        dado = JSONParser().parse(request)
        proprietario = ProprietarioSerializer(proprietario, data=dado)

        if proprietario.is_valid():
            proprietario.save()

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

        return JsonResponse(corretor.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def corretor_detail(request, pk):
    try:
        corretor = Corretor.objects.get(pk=pk)
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

        return JsonResponse(imovel.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def imovel_detail(request, pk):
    try:
        imovel = Imovel.objects.get(pk=pk)
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

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        imovel.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)