from django import forms
from .models import Exercicios

class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicios  # O modelo associado ao formulário
        fields = ['nome', 'repeticoes', 'carga']  # Campos que serão exibidos no formulário
        
