from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from decimal import Decimal, InvalidOperation
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'tema', 'data_evento', 'local', 'valor_total', 'email', 'telefone', 'situacao']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do cliente'
            }),
            'tema': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Defina o tema da festa'
            }),
            'data_evento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'min': date.today().isoformat(),
                'data-placeholder': 'dd/mm/aaaa'
            }),
            'local': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o local do evento'
            }),
            'valor_total': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0,00',
                'inputmode': 'decimal'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o e-mail'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
                'type': 'tel'
            }),
            'situacao': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
    
    def clean_data_evento(self):
        data_evento = self.cleaned_data.get('data_evento')
        if data_evento and data_evento < date.today():
            raise ValidationError('A data do evento não pode ser anterior ao dia de hoje.')
        return data_evento

    def clean_tema(self):
        tema = self.cleaned_data.get('tema', '').strip()
        return tema if tema else None
    
    def clean_valor_total(self):
        raw_value = self.data.get(self.add_prefix('valor_total'), '').strip()
        if not raw_value:
            return None

        # Remove símbolos de moeda e espaços
        normalized = raw_value.replace('R$', '').replace(' ', '').strip()
        
        # Se já está no formato numérico (ex: 1234.56), usa diretamente
        if normalized.replace('.', '').replace('-', '').isdigit():
            try:
                valor_decimal = Decimal(normalized)
                if valor_decimal < 0:
                    raise ValidationError('O valor não pode ser negativo.')
                return valor_decimal.quantize(Decimal('0.01'))
            except (InvalidOperation, ValueError):
                pass
        
        # Tenta converter formato brasileiro (1.234,56) para numérico
        # Remove pontos (milhares) e substitui vírgula por ponto (decimal)
        normalized = normalized.replace('.', '').replace(',', '.')
        
        try:
            valor_decimal = Decimal(normalized)
        except (InvalidOperation, ValueError):
            raise ValidationError('Informe um valor válido.')

        if valor_decimal < 0:
            raise ValidationError('O valor não pode ser negativo.')

        return valor_decimal.quantize(Decimal('0.01'))
