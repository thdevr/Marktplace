from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm
from .forms import ProdutoForm, ServicoForm
from .models import Produto, Servico, Categoria

def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'detalhe_produto.html', {'produto': produto})


def detalhe_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    return render(request, 'detalhe_servico.html', {'servico': servico})


@login_required
def editar_servico(request, id):
    servico = get_object_or_404(Servico, id=id, prestador=request.user)

    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('meus_anuncios')
    else:
        form = ServicoForm(instance=servico)

    return render(request, 'editar_servico.html', {'form': form})



@login_required
def excluir_servico(request, id):
    servico = get_object_or_404(Servico, id=id, prestador=request.user)
    servico.delete()
    return redirect('meus_anuncios')

@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id, vendedor=request.user)
    produto.delete()
    return redirect('meus_anuncios')


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id, vendedor=request.user)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('meus_anuncios')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'editar_produto.html', {'form': form})


@login_required
def meus_anuncios(request):
    produtos = Produto.objects.filter(vendedor=request.user)
    servicos = Servico.objects.filter(prestador=request.user)
    
    context = {
        'produtos': produtos,
        'servicos': servicos
    }
    return render(request, 'meus_anuncios.html', context)



@login_required
@login_required
def anunciar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.prestador = request.user  # atribui corretamente
            # criar categoria se não existir
            categoria_nome = form.cleaned_data['categoria']
            categoria, created = Categoria.objects.get_or_create(nome=categoria_nome)
            servico.categoria = categoria
            servico.save()
            return redirect('home')
    else:
        form = ServicoForm()

    return render(request, 'anunciar_servicos.html', {'form': form})




@login_required
def anunciar(request):
    return render(request, 'anunciar.html')

@login_required
def anunciar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.vendedor = request.user

            categoria_nome = form.cleaned_data['categoria_nome']
            categoria, created = Categoria.objects.get_or_create(nome=categoria_nome)
            produto.categoria = categoria

            produto.save()
            return redirect('home')
    else:
        form = ProdutoForm()

    return render(request, 'anunciar_produto.html', {'form': form})


