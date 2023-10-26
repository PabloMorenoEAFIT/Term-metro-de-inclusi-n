
from django.shortcuts import render
from .models import Parrafo

def pagina_principal(request):
    parrafos = Parrafo.objects.all()
    palabras_resaltar = ["palabra1", "palabra2", "palabra3"]
    
    for parrafo in parrafos:
        for palabra in palabras_resaltar:
            parrafo.texto = parrafo.texto.replace(palabra, f'<span class="resaltado">{palabra}</span>')
    
    return render(request, 'principal/pag_principal.html', {'parrafos': parrafos})
