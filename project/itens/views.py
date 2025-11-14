from django.shortcuts import render
from .models import Material

def itens(request):
    return render(request, 'itens/indexItem.html')

def listar_itens(request):
    termo = request.GET.get('pesquisar', '').strip()

    if termo:
        # busca por texto no campo 'item' (ajuste o nome se seu model usa outro)
        qs_text = Material.objects.filter(item__icontains=termo)

        # tentar buscar quantidade ou id se for número
        qs_num = Material.objects.none()
        if termo.isdigit():
            num = int(termo)
            qs_num = Material.objects.filter(id=num) | Material.objects.filter(quant=num)

        materiais = (qs_text | qs_num).distinct()
    else:
        materiais = Material.objects.all()

    # opcional: enviar o termo de volta para preencher o campo no template
    return render(request, 'itens/indexItem.html', {'materiais': materiais, 'pesquisar': termo})

