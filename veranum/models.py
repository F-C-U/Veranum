from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pasajero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField()
    fecha_modificacion = models.DateField()
    fecha_eliminacion = models.DateField()
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_por_dia = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo}"


class ServicioExtra(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    servicios_extras = models.ManyToManyField(ServicioExtra, blank=True)
    precio_total = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.precio_total:
            self.calcular_precio_total()
        super().save(*args, **kwargs)

    def calcular_precio_total(self):
        dias = (self.fecha_fin - self.fecha_inicio).days
        precio_habitacion = self.habitacion.precio_por_dia * dias
        precio_servicios = sum(
            servicio.precio for servicio in self.servicios_extras.all()
        )
        self.precio_total = precio_habitacion + precio_servicios

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.habitacion} del {self.fecha_inicio} al {self.fecha_fin}"
    
    
