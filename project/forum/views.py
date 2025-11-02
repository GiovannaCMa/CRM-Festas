from .models import Cliente
from django.shortcuts import render,redirect
from .forms import ClienteForm

def home(request):
    return render(request, 'index.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()  # pega todos os clientes do banco
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

