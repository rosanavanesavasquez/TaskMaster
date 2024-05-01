from django.urls import path
from .views import (
    homeview,
    list_view,
    index,
    tareas,
    listar_categorias,
    detalle_tarea,
    crear_tarea,
    crear_categoria,
    user_login_view,
    user_logout_view,
    completar_perfil,
    perfil_completado,
    registro_usuario,
    UserUpdateView, 
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homeview, name='home'),  # Página de inicio
    # Login - Logout-creación de usuarios
    path('login/', user_login_view, name='login'),  # 
    path('logout/', user_logout_view, name='logout'),  # 
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'), 
    path('registro_usuario/', registro_usuario, name='registro_usuario'),#Primero crear el usuario
    path('completar-perfil/', completar_perfil, name='completar_perfil'),
    path('perfil-completado/', perfil_completado, name='perfil_completado'),
    # Paginas para listar
    path('list/', list_view, name='list'),  # Página de lista de tareas
    path('index/', index, name='index'),  # Página de índice
    path('tareas/', tareas, name='tareas'),  # Página de todas las tareas -Lista de tareas
    path('detalle_tarea/<int:tarea_id>/', detalle_tarea, name='detalle_tarea'),  # Detalle de tarea
    path('categorias/', listar_categorias, name='listar_categorias'),
    # Paginas de edición CRUD
    path('crear_tarea/', crear_tarea, name='crear_tarea'),  # Vista para crear una nueva tarea
    path('crear-categoria/', crear_categoria, name='crear_categoria')
]
