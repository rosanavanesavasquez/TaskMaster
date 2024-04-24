from django.contrib import admin
from .models import Categoria, Tarea, UserProfile 

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tarea)
admin.site.register(UserProfile)