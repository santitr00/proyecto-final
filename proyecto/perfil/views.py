# perfil/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from perfil.forms import EditarPerfilForm
from .models import Profile
from .decorators import ensure_profile_exists

@login_required
@ensure_profile_exists
def perfil_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    return render(request, 'perfil/perfil.html', {'profile': profile})


@login_required
@ensure_profile_exists
def editar_perfil(request):
    # Obtener el perfil del usuario actual
    profile = request.user.profile

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil:perfil')
    else:
        form = EditarPerfilForm(instance=profile)

    return render(request, 'perfil/editar_perfil.html', {'form': form})
