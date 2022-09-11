"""CINETIC URL Configuration

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
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from cinetic_app.views import *

router = routers.DefaultRouter()
router.register('empleado', Empleado_view, basename='empleado')
router.register('ventaProducto', VentaProducto_view, basename='vendeProductos')
router.register('ventaBoletas', VendeBoletas_view, basename='vendeBoletas')
router.register('producto', Producto_view, basename='producto')
router.register('combo', Combo_view, basename='combo')
router.register('integraCombo', IntegraCombo_view, basename='integraCombo')
router.register('listaVentaProducto', ListaVentaProducto_view, basename='listaVentaProducto')
router.register('pelicula', Pelicula_view, basename='pelicula')
router.register('cinema', Cinema_view, basename='cinema')
router.register('sala', Sala_view, basename='sala')
router.register('funcion', Funcion_view, basename='funcion')
router.register('boleta', Boleta_view, basename='boleta')

urlpatterns = [
    path('', include(router.urls)),
    path('login', CustomAuthToken.as_view(), name='token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)