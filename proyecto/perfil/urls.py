# perfil/urls.py

from django.urls import path
from .views import perfil_view, editar_perfil

app_name = 'perfil'

urlpatterns = [
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path('perfil/', perfil_view, name='perfil'),
]
