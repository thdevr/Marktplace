from django.shortcuts import render
from produtos.models import Produto, Categoria, Servico
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    query = request.GET.get('q')
    categoria_nome = request.GET.get('categoria')

    produtos = Produto.objects.all()
    servicos = Servico.objects.all()

    # 🔎 Filtro por pesquisa
    if query:




        produtos = produtos.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query) |
            Q(categoria__nome__icontains=query)
        )

        servicos = servicos.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query)
        )


    # 📂 Filtro por categoria
    if categoria_nome:
        produtos = produtos.filter(categoria__nome=categoria_nome)
        servicos = servicos.filter(categoria__nome=categoria_nome)

    categorias = Categoria.objects.filter(produto__isnull=False).distinct()

    context = {
        'produtos': produtos,
        'servicos': servicos,
        'categorias': categorias,
        'categoria_ativa': categoria_nome
    }

    return render(request, 'home.html', context)

def suporte(request):
    return render(request, 'suporte.html')