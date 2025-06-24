from django.db import models
from cloudinary.models import CloudinaryField
from decimal import Decimal

class Trabajo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = CloudinaryField('Imagen principal', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class ImagenTrabajoExtra(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name='imagenes')
    imagen = CloudinaryField("Imagen adicional", blank=True, null=True)

    def __str__(self):
        return f"Imagen extra de {self.trabajo.titulo}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = CloudinaryField('imagen', blank=True, null=True)
    descuento = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def precio_con_descuento(self):
        if self.descuento > 0:
            porcentaje = Decimal(self.descuento) / Decimal(100)
            return self.price * (Decimal(1) - porcentaje)
        return self.price


class ImagenExtra(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='imagenes')
    imagen = CloudinaryField("Imagen adicional", blank=True, null=True)

    def __str__(self):
        return f"Imagen extra de {self.product.title}"


class Visita(models.Model):
    fecha = models.DateField(auto_now_add=True)
    url = models.CharField(max_length=255)
    ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.url}"
