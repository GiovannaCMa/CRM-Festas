from django.shortcuts import render

def contratos(request):
    return render(request, 'contratos/home.html')
