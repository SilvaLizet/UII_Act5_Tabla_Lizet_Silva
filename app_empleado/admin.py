from django.contrib import admin

# Register your models here.

from .models import Empleado
# Registrar el modelo Empleado en el admin
admin.site.register(Empleado)
