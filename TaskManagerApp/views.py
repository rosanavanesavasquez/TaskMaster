from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from TaskManagerApp.models import Tarea, Categoria, UserProfile
from .forms import TareaForm, CategoriaForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserEditForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# ---------------------#LOGIN - LOGOUT--------------------------------------------------------
def user_logout_view(request):
    logout(request)
    return redirect("login")


def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "TaskManagerApp/login.html", {"ROSANA": form})
#user edit
# -----------------------------------------------------------------------------
def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('completar_perfil')
    else:
        form = UserCreationForm()
    return render(request, 'TaskManagerApp/registro_usuario.html', {'form': form})

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'TaskManagerApp/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
#user edit fin

def completar_perfil(request):
    # Verificar si el usuario ya tiene un perfil
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Obtener el usuario actual
            user = request.user
            # Verificar si el usuario ya tiene un perfil
            if not hasattr(user, 'userprofile'):
                # Si no tiene un perfil, crear uno nuevo
                form.instance.user = user
                form.save()
                return redirect('home')
            else:
                # Si ya tiene un perfil, redirigir a alguna otra página o mostrar un mensaje de error
                # Por ejemplo:
                return HttpResponse("error")
    else:
        form = UserProfileForm()
    return render(request, 'TaskManagerApp/completar_perfil.html', {'form': form})
# -----------------------------PERFIL------------------------------------------------

@login_required
def perfil_completado(request):
    return render(request, 'TaskManagerApp/perfil_completado.html')

# -----------------------------------------------------------------------------

def homeview(request):
    return render(request, "TaskManagerApp/home.html")

# -----------------------------------------------------------------------------
def list_view(request):
    pass

# ----------------TAREAS-------------------------------------------------------------
@login_required
def tareas(request):
    # Obtener todas las tareas
    tareas = Tarea.objects.all()
    return render(request, 'TaskManagerApp/tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, tarea_id):
    # Obtener los detalles de una tarea específica
    tarea = Tarea.objects.get(pk=tarea_id)
    return render(request, 'TaskManagerApp/detalle_tarea.html', {'tarea': tarea})

def index(request):
    # Obtener las tareas pendientes
    tareas_pendientes = Tarea.objects.filter(completada=False)
    return render(request, 'TaskManagerApp/index.html', {'tareas': tareas_pendientes})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.fecha_limite = form.cleaned_data['fecha_limite']
            tarea.usuario = request.user  # Asigna el usuario actual al campo usuario
            tarea.save()
            return redirect('tareas')  # Redirigir a la página de tareas después de crear la tarea
    else:
        form = TareaForm()
    return render(request, 'TaskManagerApp/crear_tarea.html', {'form': form})
# ----------------------FIN TAREAS-------------------------------------------------------


# ----------------------CATEGORIAS-------------------------------------------------------
@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Puedes redirigir a cualquier página después de crear la categoría
    else:
        form = CategoriaForm()
    return render(request, 'TaskManagerApp/crear_categoria.html', {'form': form})

@login_required
def listar_categorias (request):
    # Obtener todas las categorias
    categorias = Categoria.objects.all()
    return render(request, 'TaskManagerApp/listar_categorias.html', {'categorias': categorias})

 #----------------------FIN CATEGORIAS-------------------------------------------------------