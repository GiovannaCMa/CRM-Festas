from .models import Cliente
from django.shortcuts import render,redirect
from .forms import ClienteForm

def home(request):
    return render(request, 'index.html')


def lista_clientes(request):
    termo_pesquisa = request.GET.get('pesquisar', '')  # pega o valor digitado

    if termo_pesquisa:
        clientes = Cliente.objects.filter(
            nome__icontains=termo_pesquisa
        ) | Cliente.objects.filter(
            email__icontains=termo_pesquisa
        ) | Cliente.objects.filter(
            telefone__icontains=termo_pesquisa
        )
    else:
        clientes = Cliente.objects.all()  # mostra todos se não tiver filtro

    return render(request, 'index.html', {'clientes': clientes})

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # mude para onde quiser redirecionar
    else:
        form = ClienteForm()
    return render(request, 'adicionar.html', {'form': form})

