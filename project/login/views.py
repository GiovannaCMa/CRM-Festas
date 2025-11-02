from django.shortcuts import render

def pagina_login(request):
    return render(request, 'login/index.html')
