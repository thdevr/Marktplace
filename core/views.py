from django.shortcuts import render
from produtos.models import Produto, Categoria, Servico



def home(request):
    categoria_nome = request.GET.get('categoria')

    if categoria_nome:
        produtos = Produto.objects.filter(categoria__nome=categoria_nome)
        servicos = Servico.objects.filter(categoria__nome=categoria_nome)
    else:
        produtos = Produto.objects.all()
        servicos = Servico.objects.all()

    categorias = Categoria.objects.filter(produto__isnull=False).distinct()

    context = {
        'produtos': produtos,
        'servicos': servicos,
        'categorias': categorias,
        'categoria_ativa': categoria_nome
    }

    return render(request, 'home.html', context)
