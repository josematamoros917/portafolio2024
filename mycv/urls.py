from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyecto/<int:id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('administrar_proyectos/', views.administrar_proyectos, name='administrar_proyectos'),
    path('nuevo_proyecto/', views.nuevo_proyecto, name='nuevo_proyecto'),
    path('editar_proyecto/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('agregar_gif/<int:proyecto_id>/', views.agregar_gif, name='agregar_gif'),
    path('contact/', views.contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)