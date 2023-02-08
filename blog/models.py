from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha De Modificación')

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateField(default=now, verbose_name='Fecha de Publicacion')
    image = models.ImageField(upload_to="Blog", verbose_name="Imagen", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha De Modificación')

    class Meta():
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title
