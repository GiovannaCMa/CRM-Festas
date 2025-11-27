from django.shortcuts import render
from forum.models import Cliente 
from itens.models import Material 

def home(request):
    total_festas = Cliente.objects.count() 
    total_itens = Material.objects.count() # conta quantos registros existem 
    clientes = Cliente.objects.all()
    total_precos = sum(c.valor_total for c in clientes if c.valor_total)
    return render(request, 'home/index.html', {
        'total_festas': total_festas,
         'total_itens': total_itens, 
         'festas': clientes,
         'total_precos': total_precos})
   
