from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('Confites', 'Confites'),
        ('Alimentos', 'Alimentos'),
        ('Otros', 'Otros'),
    ]

    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    creado_at = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
