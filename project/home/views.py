from django.shortcuts import render
from forum.models import Festa 
from itens.models import Material 

def home(request):
    total_festas = Festa.objects.count() 
    total_itens = Material.objects.count() # conta quantos registros existem 
    festas = Festa.objects.all()
    total_precos = sum(f.preco for f in festas if f.preco)
    return render(request, 'home/index.html', {
        'total_festas': total_festas,
         'total_itens': total_itens, 
         'festas': festas,
         'total_precos': total_precos})
   
