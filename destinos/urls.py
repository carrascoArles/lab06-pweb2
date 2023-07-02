# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.destinos_turisticos, name='destinos_turisticos'),
    path('crear_destinos/', views.crear_destinos, name='crear_destinos'),
    path('destino/<int:destino_id>/', views.detalle_destino, name='detalle_destino'),
]
