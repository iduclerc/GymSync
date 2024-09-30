from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Treino ,Exercicios

from django.contrib import messages
from .models import Usuario


def forum(request):
    treinos = Treino.objects.all()
    return render(request,'forum.html', {'treinos': treinos})

       

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


def add_exercicio(request, treino_id=None):
    treinos = Treino.objects.all() 
    treino_selecionado = get_object_or_404(Treino, id=treino_id) if treino_id else None

    if request.method == 'POST':
        nome = request.POST.get('nome')
        repeticoes = request.POST.get('repeticoes')
        carga = request.POST.get('carga')
        treino_id = request.POST.get('treino_id')  

        # Verifica se o treino foi selecionado corretamente
        treino = get_object_or_404(Treino, id=treino_id)

        # Cria um novo exercício associado ao treino
        exercicio = Exercicios(treino=treino, nome=nome, repeticoes=repeticoes, carga=carga)
        exercicio.save()

        return redirect('forum')

    return render(request, 'add_exercicio.html', {'treinos': treinos, 'treino_selecionado': treino_selecionado})


def servicos(request):
    treinos = Treino.objects.all()
    return render(request, 'servicos.html', {'treinos': treinos})
