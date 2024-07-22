from django.contrib import admin
from .models import Proyecto, GIF, Skill

# Registrar el modelo Skill
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'icono_preview')  # Mostrar nombre y vista previa del icono en la lista de habilidades

    def icono_preview(self, obj):
        if obj.icono:
            return '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.icono.url)
        return 'No icono'
    icono_preview.allow_tags = True  # Permitir etiquetas HTML en el método icono_preview

# Registrar el modelo GIF
@admin.register(GIF)
class GIFAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'descripcion_gif')
    search_fields = ('proyecto__titulo', 'descripcion_gif')
    list_filter = ('proyecto',)

# Registrar el modelo Proyecto
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion_proyecto', 'github_url')
    search_fields = ('titulo', 'descripcion_proyecto')
    filter_horizontal = ('skills',)  # Para mejorar la selección de habilidades en el administrador
