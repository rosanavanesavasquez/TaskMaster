from django.urls import path
from .views import (
    homeview,
    list_view,
    index,
    tareas,
    detalle_tarea,
    crear_tarea,
    crear_categoria,
    user_login_view,
    user_logout_view,
    UserUpdateView, 
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homeview, name='home'),  # Página de inicio
    # Login - Logout-creación de usuarios
    path('login/', user_login_view, name='login'),  # 
    path('logout/', user_logout_view, name='logout'),  # 
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'), 
    # Paginas de busquedas
    path('list/', list_view, name='list'),  # Página de lista de tareas
    path('index/', index, name='index'),  # Página de índice
    path('tareas/', tareas, name='tareas'),  # Página de todas las tareas
    path('detalle_tarea/<int:tarea_id>/', detalle_tarea, name='detalle_tarea'),  # Detalle de tarea
    # Paginas de edición CRUD
    path('crear_tarea/', crear_tarea, name='crear_tarea'),  # Vista para crear una nueva tarea
    path('crear-categoria/', crear_categoria, name='crear_categoria')
]
