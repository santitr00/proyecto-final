# perfil/models.py

from django.db import models
from django.contrib.auth.models import User

# perfil/models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True)
    gender = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    def __str__(self):
        return self.user.username
