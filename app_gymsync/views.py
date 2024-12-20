from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Treino ,Exercicios
from django.contrib.auth.hashers import check_password

from django.contrib import messages
from .models import Usuario
from .models import EditarTreino 
from .models import Rotina, RotinaDia
from django.http import HttpResponse
from datetime import time
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def forum(request):
    treinos = Treino.objects.all()
    return render(request,'forum.html', {'treinos': treinos})

       

def criar_treino(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        numero_series = request.POST.get('numero_series')
        agrupamento_muscular = request.POST.get('agrupamento_muscular')

        if not nome or not numero_series or not agrupamento_muscular:
            return render(request, 'criar_treino.html', {
                'error': 'Preencha todos os campos corretamente'
            })

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

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('senha')  # Certifique-se de que o campo de senha no formulário é "senha"
        
        try:
            # Busca o usuário pelo email
            usuario = Usuario.objects.get(email=email)
            
            # Verifica se a senha está correta
            if check_password(password, usuario.senha):
                # Se a senha estiver correta, faça login
                request.session['usuario_id'] = usuario.id  # Armazenando ID do usuário na sessão
                return redirect('home')  # Redireciona para a página inicial
            else:
                messages.error(request, 'Email ou senha inválidos.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Email ou senha inválidos.')

    return render(request, 'login.html')


def add_exercicio(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)  # Obtém o treino pelo ID
    filtro_selecionado = request.POST.get('filtro', '')

    # Filtra os exercícios de acordo com o agrupamento muscular selecionado
    if filtro_selecionado:
        exercicios = Exercicios.objects.filter(treino=treino, nome__icontains=filtro_selecionado)
    else:
        exercicios = Exercicios.objects.filter(treino=treino)

    if request.method == 'POST' and 'exercicio_nome' in request.POST:
        nome = request.POST.get('exercicio_nome')
        repeticoes = request.POST.get('repeticoes')
        carga = request.POST.get('carga')
        avaliacao = request.POST.get('rating')  # Captura a avaliação
        # Criar e salvar o exercício
        Exercicios.objects.create(
            nome=nome,
            treino=treino,
            repeticoes=repeticoes,
            carga=carga,
            avaliacao = avaliacao
        )
        return redirect('forum')  # Ajuste para redirecionar conforme necessário

    # Renderiza a página com o treino selecionado e os exercícios filtrados
    treinos = Treino.objects.all()
    return render(request, 'add_exercicio.html', {'treinos': treinos, 'treino': treino, 'exercicios': exercicios, 'filtro_selecionado': filtro_selecionado})


def servicos(request):
    treinos = Treino.objects.all()
    return render(request, 'servicos.html', {'treinos': treinos})

from .models import Treino  # Certifique-se de importar o modelo correto

def criar_rotina(request):
    treinos = Treino.objects.all()  # Busca todos os treinos do banco de dados
    rotina = None  # Inicializa a variável rotina como None

    if request.method == 'POST':
        nome_rotina = request.POST.get('nome')
        treino_id = request.POST.get('treino')  # Obtém o treino selecionado no formulário
        dia_semana = request.POST.get('dia_semana')  # Obtém o dia da semana do formulário
        horario = request.POST.get('horario')  # Obtém o horário do formulário

        if nome_rotina and treino_id and dia_semana and horario:
            # Cria uma nova instância da rotina
            rotina_principal, created = Rotina.objects.get_or_create(nome=nome_rotina)
            treino = Treino.objects.get(id=treino_id)  # Busca o treino pelo id
            # Cria um novo registro de RotinaDia
            rotina = RotinaDia.objects.create(
                rotina=rotina_principal,
                treino=treino,
                dia_semana=dia_semana,
                horario=horario
            )
            rotina.save()

    return render(request, 'criar_rotina.html', {'rotina': rotina, 'treinos': treinos})




def adicionar_treinos(request, rotina_id):
    rotina = Rotina.objects.get(id=rotina_id)
    treinos = Treino.objects.all()
    
    if request.method == 'POST':
        treino_id = request.POST.get('treino')
        dia_semana = request.POST.get('dia_semana')
        horario_str = request.POST.get('horario')

        # Validando entrada de horário
        try:
            horario = time.fromisoformat(horario_str)
        except ValueError:
            return HttpResponse("Formato de horário inválido.")

        treino = Treino.objects.get(id=treino_id)
        RotinaDia.objects.create(rotina=rotina, treino=treino, dia_semana=dia_semana, horario=horario)
        
        
        return redirect('adicionar_treinos', rotina_id=rotina.id)

    return render(request, 'adicionar_treinos.html', {'rotina': rotina, 'treinos': treinos})

def editar_treino(request, treino_id):
    # Obter o treino com base no ID fornecido
    treino = get_object_or_404(Treino, pk=treino_id)

    if request.method == 'POST':
        # Obter os valores dos campos enviados no formulário
        nome = request.POST.get('nome')
        numero_series = request.POST.get('numero_series')
        agrupamento_muscular = request.POST.get('agrupamento_muscular')

        # Atualizar os valores do treino
        treino.nome = nome
        treino.numero_series = numero_series
        treino.agrupamento_muscular = agrupamento_muscular

        # Salvar as mudanças no banco de dados
        treino.save()

        # Redirecionar para a página de detalhes do treino após salvar
        return redirect('forum')

    # Renderizar o formulário de edição, preenchendo com os valores atuais do treino
    return render(request, 'editar_treino.html', {'treino': treino})

def detalhes_treino(request, treino_id):
    # Busca o treino específico pelo ID
    treino = get_object_or_404(Treino, id=treino_id)
    exercicios = Exercicios.objects.filter(treino=treino)  # Exercícios relacionados ao treino

    return render(request, 'detalhes_treino.html', {'treino': treino, 'exercicios': exercicios})



def lista_exercicios(request):
    exercicios = Exercicios.objects.all()
    return render(request, 'lista_exercicio.html', {'exercicios': exercicios})


def exportar_treino_view(request):
    treinos = Treino.objects.all()
    return render(request, 'exportar_treino.html', {'treinos': treinos})

def exportar_treino_pdf(request):
    treino_id = request.GET.get('treino_id')
    treino = get_object_or_404(Treino, id=treino_id)
    exercicios = Exercicios.objects.filter(treino=treino)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="treino_{treino_id}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    largura, altura = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, altura - 50, f"Treino: {treino.nome}")

    p.setFont("Helvetica", 12)
    y = altura - 100
    for exercicio in exercicios:
        p.drawString(50, y, f"Exercício: {exercicio.nome}")
        p.drawString(200, y, f"Repetições: {exercicio.repeticoes}")
        p.drawString(350, y, f"Carga: {exercicio.carga}")
        y -= 30
        if y < 50:
            p.showPage()
            y = altura - 50

    p.showPage()
    p.save()
    return response

def calcular_imc_view(request):
    treinos = ''
    imc = None
    classificacao = ''
    
    if request.method == 'POST':
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))

        if altura > 0:  # Evitar divisão por zero
            imc = round(peso / (altura ** 2), 2)

            # Classificação do IMC e recomendação de treino
            if imc < 18.5:
                classificacao = 'Abaixo do peso'
                treinos = 'Hipertrofia'
            elif 18.5 <= imc < 24.9:
                classificacao = 'Peso normal'
                treinos = 'Manutenção'
            elif 25 <= imc < 29.9:
                classificacao = 'Sobrepeso'
                treinos = 'Perda de peso'
            else:
                classificacao = 'Obesidade'
                treinos = 'Cardio'

    return render(request, 'calcular_imc.html', {
        'imc': imc,
        'classificacao': classificacao,
        'treinos': treinos
    })