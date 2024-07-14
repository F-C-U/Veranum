from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, "index.html")

def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_reservas")
    else:
        form = ReservaForm()
    return render(request, "crear_reserva.html", {"form": form})


def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "lista_reservas.html", {"reservas": reservas})


def buscar_habitaciones(request):
    tipo = request.GET.get("tipo")
    habitaciones = Habitacion.objects.filter(tipo=tipo, disponible=True)
    return render(request, "buscar_habitaciones.html", {"habitaciones": habitaciones})
