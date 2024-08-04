from django import forms
from django.core.exceptions import ValidationError
from email.utils import parseaddr
import re
from .models import Proyecto, GIF, ContactMessage
from django.forms import modelformset_factory

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion_proyecto', 'github_url']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_proyecto': forms.Textarea(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class GIFForm(forms.ModelForm):
    class Meta:
        model = GIF
        fields = ['gif_file', 'descripcion_gif']
        widgets = {
            'gif_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'descripcion_gif': forms.TextInput(attrs={'class': 'form-control'}),
        }

GIFFormSet = modelformset_factory(GIF, form=GIFForm, extra=3)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'rows': 4}),
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not self.is_valid_email(email):
            raise ValidationError("El email no es válido.")
        return email

    def is_valid_email(self, email):
        # Validar si el email tiene el formato correcto
        return parseaddr(email)[1] == email and re.match(r"[^@]+@[^@]+\.[^@]+", email)