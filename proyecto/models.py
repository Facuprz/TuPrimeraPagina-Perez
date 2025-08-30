from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=200, blank=True)
    contenido = RichTextField()  # texto enriquecido
    imagen = models.ImageField(upload_to='pages/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']  # más nuevas primero

    def __str__(self):
        return self.titulo