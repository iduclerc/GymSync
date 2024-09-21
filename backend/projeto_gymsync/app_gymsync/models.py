from django.db import models

# Create your models here.
from django.db import models

class Treino(models.Model):
    nome = models.CharField(max_length=100)  # Nome do treino
    numero_series = models.IntegerField()    # Número de séries
    agrupamento_muscular = models.CharField(max_length=100)  # Grupo muscular trabalhado

    def __str__(self):
        return self.nome
    
class Exercicios(models.Model):
    treino = models.ForeignKey(Treino, related_name='exercicios', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    repeticoes = models.IntegerField()
    carga = models.FloatField()
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='exercicios')

    def __str__(self):
        return f"{self.nome} - {self.repeticoes} reps"

