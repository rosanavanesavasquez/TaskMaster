from django.shortcuts import render, redirect
from django.http import HttpResponse
from TaskManagerApp.models import Tarea
from .forms import TareaForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


#LOGIN - LOGOUT

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

def homeview(request):
    return render(request, "TaskManagerApp/home.html")


def list_view(request):
    pass

@login_required
def index(request):
    # Obtener las tareas pendientes
    tareas_pendientes = Tarea.objects.filter(completada=False)
    return render(request, 'TaskManagerApp/index.html', {'tareas': tareas_pendientes})

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

