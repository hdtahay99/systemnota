from django import forms
from .models import Materia, Grado


class GradoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Grado
        fields = ('name', 'seccion', 'materias')

    def __init__ (self, *args, **kwargs):
        super(GradoForm, self).__init__(*args, **kwargs)
        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].help_text = "Ingrese las materias"
        self.fields["materias"].queryset = Materia.objects.all()