from django.urls import  path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
]


