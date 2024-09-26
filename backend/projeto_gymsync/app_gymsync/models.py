from django.db import models

# Create your models here.
from django.db import models

class Treino(models.Model):
    nome = models.CharField(max_length=100)  # Nome do treino
    numero_series = models.IntegerField()    # Número de séries
    agrupamento_muscular = models.CharField(max_length=100)  # Grupo muscular trabalhado

    def __str__(self):
        return self.nome

