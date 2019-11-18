from django.shortcuts import render, HttpResponse
from .models import Grado, Pensum
from django.contrib import messages
from .forms import GradoForm


# Create your views here.

def home(request):
	pubs = Grado.objects.all()
	return render(request,'core/listar_grado.html', {'pubs': pubs})

def agregar(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(name=formulario.cleaned_data['name'], seccion= formulario.cleaned_data['seccion'])
            for materia_id in request.POST.getlist('materias'):
                pensum = Pensum(materia_id=materia_id, grado_id = grado.id)
                pensum.save()
            messages.add_message(request, messages.SUCCESS, 'Grado guardado')
    else:
        formulario = GradoForm()
    return render(request, 'core/grado_editar.html', {'formulario': formulario})