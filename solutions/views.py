from rest_framework.viewsets import ModelViewSet

from solutions.models import Cliente, Funcionario, Ferramenta
from solutions.serializers import ClienteSerializer, FuncionarioSerializer, FerramentaSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FerramentaViewSet(ModelViewSet):
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer