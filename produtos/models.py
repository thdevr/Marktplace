from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)


    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

# Modelo Serviço
class Servico(models.Model):
    imagem = models.ImageField(upload_to='servicos/', blank=True, null=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    prestador = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100)  # Texto simples

    def __str__(self):
        return self.nome