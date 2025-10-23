from .models import Cliente
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()  # pega todos os clientes do banco
    return render(request, 'index.html', {'clientes': clientes})
