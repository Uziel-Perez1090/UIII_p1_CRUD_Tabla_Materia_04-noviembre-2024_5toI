from django.shortcuts import render
from .models import materia

def inicio_vista(request):
    lasmaterias=materia.objects.all()
# Create your views here.
    return render(request,'gestionarMaterias.html')