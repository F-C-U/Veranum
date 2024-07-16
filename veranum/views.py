from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *



def index(request):
    return render(request, "veranum/index.html")


def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_reservas")
    else:
        form = ReservaForm()
    return render(request, "veranum/crear_reserva.html", {"form": form})


def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "veranum/lista_reservas.html", {"reservas": reservas})


def buscar_habitaciones(request):
    tipo = request.GET.get("tipo")
    habitaciones = Habitacion.objects.filter(tipo=tipo, disponible=True)
    return render(
        request, "veranum/buscar_habitaciones.html", {"habitaciones": habitaciones}
    )


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegistroForm()
    return render(request, "veranum/registro.html", {"form": form})
