from django.db import models

class Parrafo(models.Model):
    texto = models.TextField()
    palabras_subrayadas = models.TextField(default="")  # Puedes usar un valor predeterminado adecuado

