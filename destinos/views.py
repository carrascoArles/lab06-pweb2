from PIL import Image
from django.shortcuts import render, redirect
from .models import DestinosTuristicos
from .forms import destinoForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

def destinos_turisticos(request):
    destinos = DestinosTuristicos.objects.all()
    context ={
      'destinos': destinos,
    }
    return render(request, 'destinos_turisticos.html', context)

def detalle_destino(request, destino_id):
    destino = get_object_or_404(DestinosTuristicos, pk=destino_id)
    return render(request, 'detalle_destino.html', {'destino': destino})

def crear_destinos(request):

    form = destinoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = destinoForm()
    context = {
    'form': form
    }
    return render(request, 'crear_destino.html', context)