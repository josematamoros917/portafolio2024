from django import forms
from .models import Proyecto, GIF
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
