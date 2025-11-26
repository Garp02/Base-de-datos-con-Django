from django import forms
from .models import Sistemascomputo

class ComputadoraForm(forms.ModelForm):
    
    class Meta:
    
        model = Sistemascomputo
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'pais_origen': forms.TextInput(attrs = {'class': 'form-control'}),
            'numero_cores': forms.NumberInput(attrs = {'class': 'form-control'}),
            'ram_tb': forms.NumberInput(attrs = {'class': 'form-control'}),
            'almacenamiento_tb': forms.NumberInput(attrs = {'class': 'form-control'}),
            'teraflops': forms.NumberInput(attrs = {'class': 'form-control'}),
            'sistema_operativo': forms.TextInput(attrs = {'class': 'form-control'}),
        }