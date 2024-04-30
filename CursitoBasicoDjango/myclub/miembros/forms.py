from django import forms
from .models import Ciudad
#Este es la clase donde se declara los tipos de formularios 
class CiudadForm(forms.ModelForm): #Este es el formulario que se utiliza en la view (ciudadesVenezuela)
    class Meta:
        model = Ciudad
        fields = ['nb_ciudad', 'id_estado']