from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'preco', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do serviço'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descrição do serviço'}),
            'categoria': forms.TextInput(attrs={'placeholder': 'Categoria do serviço'}),
        }
