from django.urls import path

from . import views

urlpatterns = [
    path('', views.contratos, name='contratos'),
    path('<int:cliente_id>/', views.contrato_cliente, name='contrato_cliente'),
]