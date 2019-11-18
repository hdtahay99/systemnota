from django.db import models

# Create your models here.

class Profesor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=true, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=true, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"
        ordering = ['-created']

    def __str_(self):
        return self.name 

class Materia(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=true, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=true, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "materia"
        verbose_name_plural ="materias"
        ordering = ['-created']

    def __str_(self):
        return self.name

class Seccion(models.Model):
    name = models.CharField(max_length=10, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=true, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=true, verbose_name="Fecha de actualización")
    class Meta:
        verbose_name = "seccion"
        verbose_name_plural = "secciones"
        ordering = ['-created']

    def __str_(self):
        return self.name  

class Grado(models.Model):
    name = models.CharField(max_length=10, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=true, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=true, verbose_name="Fecha de actualización")
    class Meta:
        verbose_name = "grado"
        verbose_name_plural = "grados"
        ordering = ['-created']

    def __str_(self):
        return self.name  


