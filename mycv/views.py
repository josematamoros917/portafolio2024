from .models import Proyecto, GIF
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProyectoForm, GIFForm, GIFFormSet,ContactForm
from email.utils import parseaddr
# Create your views here.def index(request):

def index(request):
    proyectos = Proyecto.objects.prefetch_related('skills').all()  # Preload related skills
    context = {
        'proyectos': proyectos,
    }
    return render(request, 'mycv/index.html', context)

def detalle_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, 'mycv/detalle_proyecto.html', {'proyecto': proyecto})

def administrar_proyectos(request):
    proyectos = Proyecto.objects.all()
    gifs = GIF.objects.all()
    context = {
        'proyectos': proyectos,
        'gifs': gifs,
    }
    return render(request, 'mycv/administrar_proyectos.html', context)

def nuevo_proyecto(request):
    if request.method == 'POST':
        proyecto_form = ProyectoForm(request.POST)
        gif_formset = GIFFormSet(request.POST, request.FILES, queryset=GIF.objects.none())
        
        if proyecto_form.is_valid() and gif_formset.is_valid():
            proyecto = proyecto_form.save()
            for form in gif_formset:
                if form.cleaned_data:
                    gif = form.save(commit=False)
                    gif.proyecto = proyecto
                    gif.save()
            return redirect('administrar_proyectos')
    else:
        proyecto_form = ProyectoForm()
        gif_formset = GIFFormSet(queryset=GIF.objects.none())
    
    context = {
        'proyecto_form': proyecto_form,
        'gif_formset': gif_formset,
    }
    return render(request, 'mycv/nuevo_proyecto.html', context)


def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('administrar_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'mycv/editar_proyecto.html', {'form': form, 'proyecto': proyecto})

def agregar_gif(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == 'POST':
        form = GIFForm(request.POST, request.FILES)
        if form.is_valid():
            gif = form.save(commit=False)
            gif.proyecto = proyecto
            gif.save()
            return redirect('administrar_proyectos')
    else:
        form = GIFForm()
    return render(request, 'mycv/agregar_gif.html', {'form': form, 'proyecto': proyecto})
def is_valid_email(email):
    return parseaddr(email)[1] == email

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            send_mail(
                f'Nuevo mensaje de {contact_message.name}',
                f'Nombre: {contact_message.name}\n'
                f'Email: {contact_message.email}\n'
                f'Mensaje:\n{contact_message.message}\n'
                f'Fecha y hora: {contact_message.timestamp}',
                'no-reply@gmail.com',  # Puedes cambiar esto a una dirección de correo no-reply o tu dirección
                ['josematamoros917@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'mycv/contact.html', {'form': form})

