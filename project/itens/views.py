from django.shortcuts import render, redirect, get_object_or_404
from .models import Material

def itens(request):
    return render(request, 'itens/indexItem.html')

def listar_itens(request):
    termo = request.GET.get('pesquisar', '').strip()

    if termo:
        qs_text = Material.objects.filter(item__icontains=termo)
        qs_num = Material.objects.none()

        if termo.isdigit():
            num = int(termo)
            qs_num = Material.objects.filter(id=num) | Material.objects.filter(quant=num)

        materiais = (qs_text | qs_num).distinct()
    else:
        materiais = Material.objects.all()

    return render(request, 'itens/indexItem.html', {
        'materiais': materiais,
        'pesquisar': termo
    })


# MOSTRA tela de confirmação
def confirmar_exclusao(request, id):
    material = get_object_or_404(Material, id=id)
    return render(request, 'itens/confirmar_exclusao.html', {'material': material})


#  EXCLUIr
def excluir_item(request, id):
    material = get_object_or_404(Material, id=id)

    if request.method == "POST":
        material.delete()
        return redirect('listar_itens')

    return redirect('confirmar_exclusao', id=id)
