from django.db import models
class Clientes (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
def __str__(self):
    return self.nome