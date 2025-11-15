from django.shortcuts import get_object_or_404, render

from forum.models import Cliente, Festa


def contratos(request):
    return render(request, 'contratos/home.html')


def contrato_cliente(request, cliente_id: int):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    festa = (
        Festa.objects.filter(cliente=cliente)
        .order_by('-data')
        .first()
    )

    contexto = {
        'cliente': cliente,
        'festa': festa,
    }
    return render(request, 'contratos/home.html', contexto)
