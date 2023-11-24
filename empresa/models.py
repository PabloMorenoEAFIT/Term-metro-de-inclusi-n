from django.db import models

# Create your models here.

class Empresa(models.Model):
    id_empresa = models.CharField(max_length=20)
    nombre_empresa = models.CharField(max_length=50)
    num_ofertas = models.IntegerField()

