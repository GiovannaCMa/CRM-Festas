from django.shortcuts import render
from forum.models import Festa  # Importa o modelo Festa de onde ele realmente está

def painel_financeiro(request):
    festas = Festa.objects.all()
    total_precos = sum(f.preco for f in festas if f.preco)  # Soma apenas os preços que existem
    return render(request, 'financas/finanças.html', {
        'festas': festas,
        'total_precos': total_precos
    })
