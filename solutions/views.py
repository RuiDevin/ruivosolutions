from rest_framework.viewsets import ModelViewSet

from solutions.models import Cliente, Funcionario
from solutions.serializers import ClienteSerializer, FuncionarioSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

 