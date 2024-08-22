from django.urls import path
from .views import registro, inicio_sesion, inicio

urlpatterns = [
    path('', inicio, name='inicio'),  # Ruta para la página de inicio
    path('registro/', registro, name='registro'),
    path('login/', inicio_sesion, name='inicio_sesion'),
    
]

