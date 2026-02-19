from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CadastroForm
from .models import Perfil
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import forms


class EditarPerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ['nome_completo', 'telefone', 'rua', 'numero', 'bairro']

@login_required
def editar_perfil(request):
    usuario = request.user
    try:
        perfil = usuario.perfil
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(user=usuario)

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=perfil)
        email = request.POST.get('email', usuario.email)

        if form.is_valid():
            form.save()
            # Atualiza email do User
            usuario.email = email
            usuario.save()
            return redirect('perfil')  # redireciona para a página de perfil
    else:
        # Inicializa o formulário com os dados existentes
        form = EditarPerfilForm(instance=perfil)

    return render(request, 'editar_perfil.html', {'form': form, 'usuario': usuario})

@login_required
def perfil(request):
    usuario = request.user
    # pega o perfil associado ao usuário
    perfil_usuario = Perfil.objects.get(user=usuario)

    context = {
        'usuario': usuario,
        'perfil': perfil_usuario,
    }
    return render(request, 'perfil.html', context)


@login_required
def sair(request):
    logout(request)
    return redirect('home')

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            Perfil.objects.create(
                user=user,
                nome_completo=form.cleaned_data['nome_completo'],
                telefone=form.cleaned_data['telefone'],
                rua=form.cleaned_data['rua'],
                numero=form.cleaned_data['numero'],
                bairro=form.cleaned_data['bairro']
            )

            login(request, user)
            return redirect('home')
    else:
        form = CadastroForm()

    return render(request, 'cadastrar.html', {'form': form})



def entrar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('home')  # muda se sua home tiver outro nome
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
