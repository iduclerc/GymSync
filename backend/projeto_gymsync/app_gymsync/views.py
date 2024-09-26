from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Treino
from .forms import ExercicioForm
from django.contrib import messages
from .models import Usuario


def forum(request):
    return render(request,'forum.html')

       

def criar_treino(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        numero_series = request.POST.get('numero_series')
        agrupamento_muscular = request.POST.get('agrupamento_muscular')

        # Criar o objeto Treino e salvar no banco de dados
        treino = Treino(nome=nome, numero_series=numero_series, agrupamento_muscular=agrupamento_muscular)
        treino.save()
                                                                                                                    
        # Redirecionar para uma página de sucesso (ou outra página que você preferir)
        return redirect('forum') #tem que retornar a pagina para adicionar os exercios

    return render(request, 'criar_treino.html')

def add_exercicio(request,treino_id):
    treino = get_object_or_404(Treino,id=treino_id)
    
    if request.method == 'POST':
        form = ExercicioForm(request.POST)
        if form.is_valid():
            exercicio = form.save(commit=False)
            exercicio.treino = treino
            exercicio.save()
            return redirect('forum.html')
    else:
        form = ExercicioForm()

    return render(request, 'adicionar_exercicio.html', {'form': form, 'treino': treino})

def excluir_treino(request,treino_id):
    
    treino = get_object_or_404(Treino, id=treino_id)
    
    if request.method == 'POST':
        treino.delete()  # Exclui o treino
        messages.success(request, f'Treino "{treino.nome}" excluído com sucesso!')
        return redirect('forum')  # Redireciona para a página com a lista de treinos
    
    return render(request, 'confirmar_exclusao.html', {'treino': treino})

def lista_treinos(request):

    treinos = Treino.objects.all()
    return render(request, 'lista_treinos.html', {'treinos': treinos})
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

<<<<<<< HEAD
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
=======

def cadastro(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        # Verifica se o email já existe
        if Usuario.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {'error': 'Email já está em uso.'})

        # Cria o novo usuário
        Usuario.objects.create(
            email=email,
            senha=senha  # A senha será automaticamente hasheada no modelo
        )

        # Redireciona para a página inicial ou qualquer outra após o cadastro
        return redirect('forum')

    return render(request, 'cadastro.html')

>>>>>>> f59912150e6cb189381a0938ee5b17d2c90c74eb
