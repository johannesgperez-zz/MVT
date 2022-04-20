import datetime
from django.db import models

class MiembroFlia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    vinculo = models.CharField(max_length=30)
    fecha_ingreso_bd = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ["-edad"]
    
    def __str__(self):
        return self.nombre

