from django import forms
from .models import Profile
from django.core.exceptions import ValidationError

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo', 'gender', 'country', 'email']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    # Método clean para agregar validaciones
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        
        # Validar que el usuario haya subido una foto de perfil
        if not photo:
            raise ValidationError("Es obligatorio subir una foto de perfil.")
        
        return photo
