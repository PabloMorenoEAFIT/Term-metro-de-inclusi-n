from django.db import models


class Usuario(models.Model):
    id_usuario = models.CharField(max_length=20)
    correo_usuario = models.CharField(max_length=100)
    telefono_usuario = models.IntegerField()
    edad_usuario = models.IntegerField()
    nivel_educacion = models.CharField(max_length=45)
    genero_usuario = models.CharField(max_length=45)

#     class Meta:
#         abstract = True

# class Rol(models.Model):
#     usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    
#     class Meta:
#         abstract = True

# Implementación de Abstracciones
class AdministradorMag(Usuario):
    id_adminMag = models.CharField(max_length=20)

class AnalistaPropuesta(Usuario):
    id_analista = models.CharField(max_length=20)
    empresa_analista = models.CharField(max_length=20)

class Aplicante(Usuario):
    nombre_aplicante = models.CharField(max_length=100)
