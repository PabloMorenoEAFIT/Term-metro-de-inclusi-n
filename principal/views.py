from django.shortcuts import render
from .models import Parrafo

def pagina_principal(request):
    parrafos = Parrafo.objects.all()
    palabras_resaltar = ["palabra1", "palabra2", "palabra3"]
    
    for parrafo in parrafos:
        texto_modificado = parrafo.texto
        for palabra in palabras_resaltar:
            texto_modificado = texto_modificado.replace(palabra, f'<span class="resaltado">{palabra}</span>')
        parrafo.texto = texto_modificado
        parrafo.save()  # Guarda el parrafo modificado en la base de datos
    
    return render(request, 'principal/pag_principal.html', {'parrafos': parrafos})
