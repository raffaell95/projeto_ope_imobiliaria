from rest_framework import serializers
from core.models.Cliente import Cliente

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')