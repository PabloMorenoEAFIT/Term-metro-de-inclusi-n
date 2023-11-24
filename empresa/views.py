from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from oferta.models import Oferta

def select_empresa_view(request):
    # Obtener empresas disponibles desde la base de datos
    empresas = Oferta.objects.values_list('empresa_oferta', flat=True).distinct()

    # Devolver las empresas como JSON
    data = {'empresas': list(empresas)}
    return JsonResponse(data, safe=False)


def obtener_oferta(request, id_oferta):
    try:
        # Obtener información de la oferta por su ID
        oferta = get_object_or_404(Oferta, id_oferta=id_oferta)
        
        # Devolver la información 
        data = {
            'id_oferta': oferta.id_oferta,
            'nombre_oferta': oferta.nombre_oferta,
            'descripcion_oferta': oferta.descripcion_oferta,
            'empresa_oferta': oferta.empresa_oferta,
            'fecha_oferta': oferta.fecha_oferta.strftime("%Y-%m-%d %H:%M:%S")  # Formato de fecha
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def eliminar_oferta(request, id_oferta):
    try:
        oferta = get_object_or_404(Oferta, id_oferta=id_oferta)
        oferta.delete()
        return JsonResponse({'mensaje': 'Oferta eliminada correctamente'})
    except Exception as e:
        print(f"Error al eliminar la oferta ({id_oferta}): {str(e)}")
        return JsonResponse({'error': 'Error al eliminar la oferta'}, status=500)