from django import forms
from django.forms import ModelForm
from .models import Persona
 

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields =['id_per','nombre_per','apellido_per','correo_per','clave_per','ciudad_per','region_per','codPostal_per']

        widget = {
            'id_per': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre_per': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_per': forms.TextInput(attrs={'class':'form-control'}),
            'correo_per': forms.TextInput(attrs={'class':'form-control'}),
            'clave_per': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad_per': forms.TextInput(attrs={'class':'form-control'}),
            'region_per': forms.TextInput(attrs={'class':'form-control'}),
            'codPostal_per': forms.NumberInput(attrs={'class':'form-control'}),
        }