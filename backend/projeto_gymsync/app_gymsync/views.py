from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Treino

def forum(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        numero_series = request.POST.get('numero_series')
        agrupamento_muscular = request.POST.get('agrupamento_muscular')

        # Criar o objeto Treino e salvar no banco de dados
        treino = Treino(nome=nome, numero_series=numero_series, agrupamento_muscular=agrupamento_muscular)
        treino.save()
                                                                                                                    
        # Redirecionar para uma página de sucesso (ou outra página que você preferir)
        return redirect('lista_treinos.html')

    return render(request, 'forum.html')

def criar_treino(request):
    pass

def lista_treinos(request):

    treinos = Treino.objects.all()
    return render(request, 'lista_treinos.html', {'treinos': treinos})
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
