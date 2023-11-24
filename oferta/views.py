from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from .models import Oferta


# tu_app/views.py
from django.shortcuts import render

# elementos desde landing

def landing_page_view(request):
    return render(request, 'landing/landing.html')

def oferta_view(request):
    return render(request, 'oferta/index.html')

def empresa_view(request):
    return render(request, 'empresa/empresa.html')

def adminMag_view(request):
    return render(request, 'adminMag/adminMag.html')

# elementos de empresa

def empresa_crear(request):
    return render(request, 'empresa/crearEmpresa.html')

def empresa_select(request):
    return render(request, 'empresa/selectEmpresa.html')



# oferta
# ------
from django.http import JsonResponse
from .palabras import palabras_predefinidas as palabras

def palabras_predefinidas(request):
    return JsonResponse({'palabras_predefinidas': palabras})

def guardar_oferta(request):
    if request.method == 'POST':
        id_oferta = request.POST['id_oferta']
        nombre_oferta = request.POST['nombre_oferta']
        descripcion_oferta = request.POST['descripcion_oferta']
        empresa_oferta = request.POST['empresa_oferta']
        fecha_oferta = request.POST['fecha_oferta']

        # Crear una nueva instancia de Oferta y guardarla en la base de datos
        nueva_oferta = Oferta.objects.create(
            id_oferta=id_oferta,
            nombre_oferta=nombre_oferta,
            descripcion_oferta=descripcion_oferta,
            empresa_oferta=empresa_oferta,
            fecha_oferta=fecha_oferta
        )

        # Redirigir a alguna página después de guardar la oferta
        # return redirect('nombre_de_tu_pagina')

    # return render(request, 'index.html')
    return render(request, 'oferta/index.html')

def mostrar_ofertas(request):
    ofertas = Oferta.objects.all()
    return render(request, 'oferta/mostrarOferta.html', {'ofertas': ofertas})

# implementacion de APIs
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.http import JsonResponse
import openai
from django.conf import settings

def generar_descripcion_consesgo(prompt_words):
    openai.api_key = settings.OPENAI_API_KEY

    # Construir el prompt para OpenAI
    prompt = f"Genera una descripción o recomendación para cambiar la palabra: {', '.join(prompt_words)}."

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=prompt,
            max_tokens=150,  # Ajusta según tus preferencias
            n=1,  # Número de respuestas a generar
        )

        # Obtener la respuesta generada
        generated_text = response.choices[0].text.strip()

        return JsonResponse({'generated_text': generated_text})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def generar_descripcion_consesgo_view(request):
    if request.method == 'POST':
        # Obtener la lista de palabras del cuerpo de la solicitud POST
        prompt_words = request.POST.getlist('prompt_words[]', [])
        
        # Llamar a la función para generar la descripción con sesgo
        response_data = generar_descripcion_consesgo(prompt_words)
        
        return response_data

    return JsonResponse({'error': 'Método no permitido'}, status=405)
