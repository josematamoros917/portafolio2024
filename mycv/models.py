from django.db import models

class Skill(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.FileField(upload_to='skill_icons/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Proyecto(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion_proyecto = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    dataset_original = models.FileField(upload_to='datasets/originals/', blank=True, null=True)
    dataset_limpio = models.FileField(upload_to='datasets/cleaned/', blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='proyectos', blank=True)
    powerbi_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo

class GIF(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='gifs', on_delete=models.CASCADE)
    gif_file = models.FileField(upload_to='gifs/', blank=True, null=True)
    descripcion_gif  = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"GIF for {self.proyecto.titulo} - {self.descripcion_gif}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} at {self.timestamp}'
