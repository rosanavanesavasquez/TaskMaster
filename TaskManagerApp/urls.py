from django.urls import path
from .views import (
    homeview,
    list_view,
    tarea_delete_view,
    tareas,
    listar_categorias,
    crear_tarea,
    crear_categoria,
    user_login_view,
    user_logout_view,
    completar_perfil,
    perfil_completado,
    registro_usuario,
    tarea_complete_view,
    aboutme_view,
    UserUpdateView, 
    buscar_categoria,  
    CategoriaUpdateView,  
    CategoriaDeleteView,  
)

urlpatterns = [
    path('', homeview, name='home'),  # Página de inicio
    # Login - Logout-creación de usuarios
    path('login/', user_login_view, name='login'),  
    path('logout/', user_logout_view, name='logout'),  
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'), 
    path('registro_usuario/', registro_usuario, name='registro_usuario'),
    path('completar-perfil/', completar_perfil, name='completar_perfil'),
    path('perfil-completado/', perfil_completado, name='perfil_completado'),
    path('aboutme/', aboutme_view, name='aboutme'),
    # Paginas CRUD Clase 22
    path('crear_tarea/', crear_tarea, name='crear_tarea'), #Menu tareas para crear una nueva tarea
    path('tareas/', tareas, name='tareas'), #Menu Tareas para listar todas las tareas creadas
    path('tareas/delete/<int:tarea_id>/', tarea_delete_view, name='tarea-delete'),

    #path("tareas/update/<tarea_id>", tarea_update_view, name="tarea-update"),
    #path("tareas/buscar/", search_tarea_view, name="tarea-search"),
    #path('detalle_tarea/<int:tarea_id>/', detalle_tarea, name='detalle_tarea'),  
    path('categorias/', listar_categorias, name='listar_categorias'),
    # Paginas de edición CRUD - BUSQUEDA
    path('tareas/complete/<int:tarea_id>/', tarea_complete_view, name='tarea-complete'),
    path('crear-categoria/', crear_categoria, name='crear_categoria'),
    path('buscar-categoria/', buscar_categoria, name='buscar_categoria'),  # 
]
