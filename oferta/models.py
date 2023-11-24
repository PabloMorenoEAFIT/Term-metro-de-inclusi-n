from django.db import models

# Create your models here.

class Oferta(models.Model):
    id_oferta = models.CharField(max_length=20)
    nombre_oferta = models.CharField(max_length=50, default='oferta')
    descripcion_oferta = models.CharField(max_length=500)
    empresa_oferta = models.CharField(max_length=20)
    fecha_oferta = models.DateTimeField()


