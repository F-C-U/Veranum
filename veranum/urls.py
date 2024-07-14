from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crear-reserva/", views.crear_reserva, name="crear_reserva"),
    path("reservas/", views.lista_reservas, name="lista_reservas"),
    path("buscar-habitaciones/", views.buscar_habitaciones, name="buscar_habitaciones"),
]
