from django.db import models
# Create your models here.

class Escola(models.Model):
    ESTADO = (
        ("---", "---"),
        ("SP","São Paulo"),

    )
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    estado = models.CharField(choices=ESTADO, max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    senha = models.CharField(max_length=255)
