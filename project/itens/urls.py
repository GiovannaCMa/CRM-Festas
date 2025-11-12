from django.urls import path
from . import views

urlpatterns = [
    path('itens/', views.listar_itens, name='listar_itens'),  # lista vinda do banco
]
