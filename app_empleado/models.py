from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono= models.IntegerField()
    
    #Es para el administrador servidor admin
    def __srt__(self):
        return f"{self.nombre} {self.telefono}"