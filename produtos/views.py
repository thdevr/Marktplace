from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm
from .forms import ProdutoForm, ServicoForm
from .models import Produto, Servico, Categoria
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.contrib.auth.decorators import login_required
from reportlab.platypus import Image
import os



@login_required
def gerar_relatorio(request):
    usuario = request.user
    perfil = usuario.perfil

    # 🔹 PEGAR PRODUTOS E SERVIÇOS
    produtos = Produto.objects.filter(vendedor=usuario)
    servicos = Servico.objects.filter(prestador=usuario)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="relatorio.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    elementos = []

    # 🔹 TÍTULO
    elementos.append(Paragraph("Relatório do Usuário", styles['Title']))
    elementos.append(Spacer(1, 12))

    # 🔹 DADOS DO USUÁRIO
    elementos.append(Paragraph("Dados do Usuário", styles['Heading2']))
    elementos.append(Paragraph(f"Nome: {usuario.username}", styles['Normal']))
    elementos.append(Paragraph(f"Email: {usuario.email}", styles['Normal']))
    elementos.append(Spacer(1, 12))

    # 🔹 DADOS DO PERFIL
    elementos.append(Paragraph("Dados do Perfil", styles['Heading2']))
    elementos.append(Paragraph(f"Nome completo: {perfil.nome_completo}", styles['Normal']))
    elementos.append(Paragraph(f"Telefone: {perfil.telefone}", styles['Normal']))
    elementos.append(Paragraph(
        f"Endereço: {perfil.rua}, {perfil.numero} - {perfil.bairro}",
        styles['Normal']
    ))
    elementos.append(Spacer(1, 12))

    # 🔹 PRODUTOS
    elementos.append(Paragraph("Produtos", styles['Heading2']))

    if produtos:
        for p in produtos:
            elementos.append(Paragraph(f"{p.nome} | R$ {p.preco}", styles['Normal']))

        if p.imagem:
            caminho_imagem = p.imagem.path  # pega caminho real da imagem
            img = Image(caminho_imagem, width=100, height=100)
            elementos.append(img)

        elementos.append(Spacer(1, 10))
    else:
        elementos.append(Paragraph("Nenhum produto cadastrado.", styles['Normal']))

    elementos.append(Spacer(1, 12))

    # 🔹 SERVIÇOS
    elementos.append(Paragraph("Serviços", styles['Heading2']))

    if servicos:
        for s in servicos:
            elementos.append(Paragraph(f"{s.nome} | R$ {s.preco}", styles['Normal']))

        if s.imagem:
            caminho_imagem = s.imagem.path
            img = Image(caminho_imagem, width=100, height=100)
            elementos.append(img)

        elementos.append(Spacer(1, 10))
    else:
        elementos.append(Paragraph("Nenhum serviço cadastrado.", styles['Normal']))

    # 🔹 GERAR PDF
    doc.build(elementos)

    return response

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


