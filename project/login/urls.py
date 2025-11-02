from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_login, name='pagina_login'),  # rota principal do app
]
