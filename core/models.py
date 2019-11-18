from django.db import models

# Create your models here.

class Profesor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['-created']

    def __str_(self):
        return self.name 

class Materia(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    profesores = models.ManyToManyField(Profesor,related_name="get_profesores", verbose_name="Profesores")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural ="Materias"
        ordering = ['-created']

    def __str_(self):
        return self.name

class Grado(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    seccion = models.CharField(max_length=10, verbose_name="Seccion")
    materias = models.ManyToManyField(Materia,related_name="get_materias", verbose_name="Materias")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name = "Grado"
        verbose_name_plural = "Grados"
        ordering = ['-created']

    def __str_(self):
        return self.name  

class Estudiante(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    email = models.CharField(max_length=100, verbose_name="Email")
    grado = models.ForeignKey(Grado, verbose_name="Grado", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['-created']

    def __str_(self):
        return self.name

class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    materia = models.ForeignKey(Grado, verbose_name="Materia", on_delete=models.CASCADE)
    nota = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"

    def __str_(self):
        return self.nota


