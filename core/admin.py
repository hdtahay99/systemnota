from django.contrib import admin
from .models import Profesor, MateriaAdmin, GradoAdmin, Estudiante, Nota, Grado, Materia

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Estudiante)
admin.site.register(Nota)

