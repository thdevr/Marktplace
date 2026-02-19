from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    nome_completo = forms.CharField(max_length=150)
    telefone = forms.CharField(max_length=20)
    rua = forms.CharField(max_length=150)
    numero = forms.CharField(max_length=20)
    bairro = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'nome_completo',
            'telefone',
            'rua',
            'numero',
            'bairro'
        ]
