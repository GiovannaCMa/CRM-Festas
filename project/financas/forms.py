from django import forms
from .models import Festas

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Festas
        fields = ['nome_festa', 'data', 'local', 'cliente', 'preco']
