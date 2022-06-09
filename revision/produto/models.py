from django.db import models
class Produto (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    validade = models.CharField(max_length=100)

def __str__(self):
    return self.nome