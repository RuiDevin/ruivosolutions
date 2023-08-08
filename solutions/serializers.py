from rest_framework.serializers import ModelSerializer

from solutions.models import Cliente, Funcionario, Ferramenta

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = "__all__"

class FerramentaSerializer(ModelSerializer):
    class Meta:
        model = Ferramenta
        fields = "__all__"