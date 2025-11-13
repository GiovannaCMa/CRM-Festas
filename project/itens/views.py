from django.shortcuts import render
from .models import Material


def itens(request):
   return render(request, 'itens/indexItem.html')

def listar_itens(request):
    materiais = Material.objects.all()
    return render(request, 'itens/indexItem.html', {'materiais': materiais})

