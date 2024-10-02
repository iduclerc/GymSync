from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password


DAYS_OF_WEEK = [
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
]

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


class Usuario(models.Model):
    email = models.EmailField(unique=True) #unique=True criar 1 conta por email
    senha = models.CharField(max_length=128)  # Para armazenar a senha hash

    def save(self, *args, **kwargs):
        # Gera o hash da senha antes de salvar
        self.senha = make_password(self.senha)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

class Rotina(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class RotinaDia(models.Model):
    rotina = models.ForeignKey(Rotina, on_delete=models.CASCADE, related_name='dias')
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    dia_semana = models.CharField(choices=DAYS_OF_WEEK, max_length=3)
    horario = models.TimeField()

    class Meta:
        unique_together = ('rotina', 'dia_semana', 'horario')

    def __str__(self):
        return f'{self.dia_semana} - {self.horario}'
