from django import forms
from django.forms import widgets
from ..models import Service
from decimal import Decimal

class ServiceForm(forms.ModelForm):
    valor_minimo = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    porcentagem_comissao = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_quarto = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_sala = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_banheiro = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_quintal = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_cozinha = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_outros = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))

    class Meta:
        model = Service
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        money_fields = [
            'valor_minimo',
            'porcentagem_comissao',
            'valor_quarto',
            'valor_sala',
            'valor_banheiro',
            'valor_quintal',
            'valor_cozinha',
            'valor_outros'
        ]

        for field_name in money_fields:
            if field_name in cleaned_data:
                data = cleaned_data[field_name]
                cleaned_data[field_name] = Decimal(data.replace(',', '.'))

        return cleaned_data
