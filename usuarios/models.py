from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
