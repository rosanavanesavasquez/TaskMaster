from django import forms
from .models import Tarea, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_limite', 'categoria']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }
