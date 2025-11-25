from django.shortcuts import render
from forum.models import Festa, Cliente  # Importa os modelos Festa e Cliente

def painel_financeiro(request):
    festas = Festa.objects.all()
    clientes = Cliente.objects.filter(valor_total__isnull=False).exclude(valor_total=0)
    
    # Calcula o total de festas
    total_precos_festas = sum(f.preco for f in festas if f.preco) or 0
    
    # Calcula o total de clientes
    total_precos_clientes = sum(c.valor_total for c in clientes if c.valor_total) or 0
    
    # Total geral
    total_precos = total_precos_festas + total_precos_clientes
    
    return render(request, 'financas/finanças.html', {
        'festas': festas,
        'clientes': clientes,
        'total_precos': total_precos
    })
