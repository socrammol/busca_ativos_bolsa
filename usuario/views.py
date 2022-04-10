from django.shortcuts import redirect, render

from .models import Usuario
from .forms import UsuarioForm
from projeto.buscaAtivos import busca_ativos
from datetime import date, timedelta


def list_usuario(request):
    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        start = date.today() - timedelta(usuario.iniciomonitoramentoemdias)
        end = date.today() - timedelta(usuario.terminomonitoramentoemdias)
        busca_ativos(usuario.ticker, start.strftime('%m-%d-%Y'), end.strftime('%m-%d-%Y'))
    return render(request, 'Usuario.html', {'usuarios': usuarios})


def create_usuario(request):
    form = UsuarioForm(request.POST or None)
    usuarios = Usuario.objects.all()

    if usuarios.exists():
        return redirect('list_usuario')
    else:
        if form.is_valid():
            form.save()
            return redirect('list_usuario')
        return render(request, 'usuario-form.html', {'form': form})


def update_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('list_usuario')

    return render(request, 'usuario-form.html', {'form': form, 'usuario': usuario})


def delete_usuario(request, id):
    usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('list_usuario')

    return render(request, 'usuario-delete-confirm.html', {'usuario': usuario})

# Create your views here.
