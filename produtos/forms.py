from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    categoria_nome = forms.CharField(
        label='Categoria',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite a categoria'})
    )

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'imagem']  # removemos 'categoria'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do produto'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descrição do produto'}),
            'preco': forms.NumberInput(attrs={'placeholder': 'Preço'}),
            'quantidade': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
        }

# SERVIÇOS
from .models import Servico  # crie esse modelo se ainda não tiver

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'categoria', 'imagem']  # inclui o campo do modelo
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do serviço'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descrição do serviço'}),
            'categoria': forms.TextInput(attrs={'placeholder': 'Digite a categoria'}),
        }
