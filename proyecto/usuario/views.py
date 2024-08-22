from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, InicioSesionForm
from django.contrib import messages

def inicio(request):
    return render(request, 'usuario/inicio.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil:editar_perfil')  # Redirige a la página de perfil
    else:
        form = RegistroForm()
    return render(request, 'usuario/registro.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError

class CustomLoginError(Exception):
    pass

def inicio_sesion(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    error_message = "usuario o contraseña incorrecto."
            else:
                error_message = "Datos invalidos"
        except CustomLoginError as e:
            error_message = str(e)
    else:
        form = AuthenticationForm()
    return render(request, 'usuario/inicio_sesion.html', {'form': form, 'error_message': error_message})
