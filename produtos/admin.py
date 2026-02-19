from django.contrib import admin
from .models import Produto, Categoria, Servico

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Servico)
