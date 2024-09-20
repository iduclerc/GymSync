from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Treino

def criar_treino(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        numero_series = request.POST.get('numero_series')
        agrupamento_muscular = request.POST.get('agrupamento_muscular')

        # Criar o objeto Treino e salvar no banco de dados
        treino = Treino(nome=nome, numero_series=numero_series, agrupamento_muscular=agrupamento_muscular)
        treino.save()

        # Redirecionar para uma página de sucesso (ou outra página que você preferir)
        return redirect('lista_treinos')

    return render(request, 'criar_treino.html')
def lista_treinos(request):
    treinos = Treino.objects.all()
    return render(request, 'lista_treinos.html', {'treinos': treinos})


