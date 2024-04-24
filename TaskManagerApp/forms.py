from django import forms
from .models import Tarea, Categoria, User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

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
