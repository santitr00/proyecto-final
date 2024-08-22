# perfil/decorators.py

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps
from .models import Profile

def ensure_profile_exists(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        try:
            request.user.profile
        except Profile.DoesNotExist:
            Profile.objects.create(user=request.user)
        return view_func(request, *args, **kwargs)
    return _wrapped_view