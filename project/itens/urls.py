from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_itens, name='listar_itens'),
    path('excluir/<int:id>/', views.excluir_item, name='excluir_item'),
]

