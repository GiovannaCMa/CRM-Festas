from django.shortcuts import render
from forum.models import Festa  # importa sua tabela Festa

def painel_financeiro(request):
    # pega todos os registros e soma os preços
    festas = Festa.objects.all()
    total_precos = sum(f.preco for f in festas if f.preco)

    context = {
        'festas': festas,
        'total_precos': total_precos,
    }

    return render(request, 'financas/finanças.html', context)

# Create your views here.
