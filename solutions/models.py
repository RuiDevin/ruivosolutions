from django.db import models

class Ferramenta(models.Model):
    CODIGO_CHOICES = (
        ('FDC', 'Ferramentas de Celular'),
        ('FDPC', 'Ferramentas de Computador'),
        ('FDN', 'Ferramentas de Notebook'),
    )
    
    codigo = models.CharField(max_length=4, choices=CODIGO_CHOICES, default='FDC', unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"
    
    @classmethod
    def buscar_por_codigo(cls, codigo):
        try:
            return cls.objects.get(codigo=codigo)
        except cls.DoesNotExist:
            return None 


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Caixa(models.Model):
    descricao = models.CharField(max_length=100)
    gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lucros = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def prejuizo(self):
        return self.lucros - self.gastos

    def __str__(self):
        return self.descricao
    
class ItemEstoque(models.Model):
    codigo = models.PositiveIntegerField(unique=True)
    descricao = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"Código: {self.codigo} | Descrição: {self.descricao} "
