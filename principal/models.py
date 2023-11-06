from djongo import models

class Parrafo(models.Model):
    texto = models.TextField()
    palabras_subrayadas = models.TextField(default="")

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=15) 
    nombre_usuario = models.IntegerField()

class Oferta(models.Model):
    nombre_propuesta= models.CharField(max_length=15) 
    Empresa.nombre_empresa = models.CharField(max_length=15) 
    descripcion_propuesta = models.CharField(max_length=500)

class Analista(models.Model):
    Usuario.id_usuario = models.CharField(max_length=15) 
    Empresa.id_empresa = models.CharField(max_length=20)

class Empresa(model.Model):
    nombre_empresa = models.CharField(max_length=15) 
    id_empresa = models.CharField(max_length=20)
    numero_propuetas = models.IntegerField()

