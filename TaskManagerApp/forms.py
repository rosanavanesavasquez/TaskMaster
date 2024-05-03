from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tarea, Categoria, User, UserProfile


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_date', 'phone_number', 'address', 'facebook_url']
        # Agrega otros campos de perfil que quieras incluir en el formulario

#--------------CATEGORIA----------------------------------------------------------
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class BuscarCategoriaForm(forms.Form):
    nombre = forms.CharField(label='Nombre de la categoría', max_length=100)

class EditarCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']  # Campos a editar en la categoría

class BorrarCategoriaForm(forms.Form):
    confirmacion = forms.BooleanField(label='¿Estás seguro de que deseas eliminar esta categoría?', required=True)

#--------------FIN CATEGORIA----------------------------------------------------------
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_limite', 'categoria']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }
        
