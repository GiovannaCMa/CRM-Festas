from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel_financeiro, name='painel_financeiro'),
]

