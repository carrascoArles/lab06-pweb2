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

def administrar_destinos(request):
    destinos = DestinosTuristicos.objects.all()
    context ={
      'destinos': destinos,
    }
    return render(request, 'administrar_destinos.html', context)

def modificar_destino(request, nombre_ciudad):
    destino = get_object_or_404(DestinosTuristicos, nombreCiudad=nombre_ciudad)
    form = destinoForm(request.POST, request.FILES, instance=destino)

    
    context = {
        'form': form
    }
    return render(request, 'modificar_destino.html', context)

def eliminar_destino(request, nombre_ciudad):
    destino = get_object_or_404(DestinosTuristicos, nombreCiudad=nombre_ciudad)
    if request.method == 'POST':
        destino.delete()
        return redirect('administrar_destinos')
    context = {
        'destino': destino,
    }
    
    return render(request, 'eliminar_destino.html', context)