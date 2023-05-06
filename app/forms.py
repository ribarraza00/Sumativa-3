from django import forms
from django.forms import ModelForm
from .models import Personas
 

class PersonaForm(ModelForm):
    class Meta:
        model = Personas
        fields =['id_per','nombre_per','apellido_per','correo_per','clave_per','codPostal_per','Region','Comuna','Profecion']

        widget = {
            'id_per': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre_per': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_per': forms.TextInput(attrs={'class':'form-control'}),
            'correo_per': forms.TextInput(attrs={'class':'form-control'}),
            'clave_per': forms.TextInput(attrs={'class':'form-control'}),
            'codPostal_per': forms.NumberInput(attrs={'class': 'form-control'}),
            'Region': forms.Select(attrs={'class': 'form-control'}),
            'Comuna': forms.Select(attrs={'class': 'form-control'}),
            'Profecion': forms.Select(attrs={'class': 'form-control'}),
        }