# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.destinos_turisticos, name='destinos_turisticos'),
    path('crear_destinos/', views.crear_destinos, name='crear_destinos'),
    path('administrar_destinos/', views.administrar_destinos, name='administrar_destinos'),
    path('modificar_destino/<str:nombre_ciudad>/', views.modificar_destino, name='modificar_destino'),
    path('eliminar_destino/<str:nombre_ciudad>/', views.eliminar_destino, name='eliminar_destino'),
    path('destino/<int:destino_id>/', views.detalle_destino, name='detalle_destino'),
]
