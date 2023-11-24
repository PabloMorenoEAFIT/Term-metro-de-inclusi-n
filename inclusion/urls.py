"""inclusion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from oferta import views
from oferta.views import palabras_predefinidas, guardar_oferta, oferta_view, empresa_view, adminMag_view, landing_page_view, empresa_crear, empresa_select, mostrar_ofertas, generar_descripcion_consesgo_view

from empresa.views import select_empresa_view, obtener_oferta, eliminar_oferta

urlpatterns = [
    path('', landing_page_view, name='landing'),
    path('oferta/', oferta_view, name='oferta'),
    path('empresa/', empresa_view, name='empresa'),
    path('adminMag/', adminMag_view, name='adminMag'),

    # empresa
    path('selectEmpresa/', empresa_select, name='selectEmpresa'),
    path('crearEmpresa/', empresa_crear, name='crearEmpresa'),

    path('select-empresa/', select_empresa_view, name='select_empresa'),
    path('empresa-info/<str:id_oferta>/', obtener_oferta, name='empresa_info'),
    path('eliminar-oferta/<str:id_oferta>/', eliminar_oferta, name='eliminar_oferta'),

    path('palabras-predefinidas/', palabras_predefinidas, name='palabras_predefinidas'),
    path('guardar-oferta/', guardar_oferta, name='guardar_oferta_url'),

    # oferta
    path('mostrar-ofertas/', mostrar_ofertas, name='mostrar_ofertas'),

    # apis
    path('generar-descripcion-sesgada/', generar_descripcion_consesgo_view, name='generar_descripcion_sesgada'),

]
