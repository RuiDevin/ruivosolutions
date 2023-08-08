from django.contrib import admin
from .models import Caixa, Cliente, Ferramenta, Funcionario, ItemEstoque

admin.site.register(Ferramenta)
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Caixa)
admin.site.register(ItemEstoque)
