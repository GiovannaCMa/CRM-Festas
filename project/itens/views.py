from django.shortcuts import render, redirect, get_object_or_404
from .models import Material

def listar_itens(request):

    # ==============================================
    #   SE FOR POST → ESTÁ EDITANDO UM MATERIAL
    # ==============================================
    if request.method == "POST":
        id = request.POST.get("id")
        novo_valor = request.POST.get("valor")
        campo = request.POST.get("campo")  # item, quant, categoria, preco

        material = get_object_or_404(Material, id=id)

        if campo == "item":
            material.item = novo_valor
        elif campo == "quant":
            material.quant = novo_valor
        elif campo == "categoria":
            material.categoria = novo_valor
        elif campo == "preco":
            material.preco = novo_valor

        material.save()
        return redirect("listar_itens")

    # ==============================================
    #   GET NORMAL → LISTAGEM COM BUSCA
    # ==============================================
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



# ==============================================
#          EXCLUSÃO (PERFEITO COMO ESTÁ)
# ==============================================

def excluir_item(request, id):
    material = get_object_or_404(Material, id=id)

    if request.method == "POST":
        material.delete()
        return redirect('listar_itens')

    return redirect('listar_itens')
