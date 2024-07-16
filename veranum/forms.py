from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            "pasajero",
            "habitacion",
            "fecha_inicio",
            "fecha_fin",
            "servicios_extras",
        ]

    def clean(self):
        cleaned_data = super().clean()
        habitacion = cleaned_data.get("habitacion")
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")

        if Reserva.objects.filter(
            habitacion=habitacion,
            fecha_fin__gte=fecha_inicio,
            fecha_inicio__lte=fecha_fin,
        ).exists():
            raise forms.ValidationError(
                "La habitación no está disponible en el periodo seleccionado."
            )

        return cleaned_data


class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "nombre",
            "apellido",
            "telefono",
            "fecha_nacimiento",
            "password1",
            "password2",
        ]
