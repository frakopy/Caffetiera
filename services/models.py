from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Sub Titulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='Services', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha De Modificación')

    class Meta():
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title
