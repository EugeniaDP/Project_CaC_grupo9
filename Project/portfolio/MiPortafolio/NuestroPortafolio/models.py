from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última modificación")
    link = models.URLField(verbose_name="Enlace al proyecto", default="https://google.com")

    def __str__(self):
        return self.title

class Meta:
    verbose_name = "Proyecto"
    verbose_name_plural = "Proyectos"
    ordering = ["-created"]