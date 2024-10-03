from django.contrib import admin
from django.urls import path
from app_gymsync import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Página principal (forum)
    path('', views.forum, name='forum'),
    
    # Criar treino
    path('criar_treino/', views.criar_treino, name='criar_treino'),
    
    # Listar treinos
    path('lista_treino/', views.lista_treinos, name='lista_treinos'),
    
    # Excluir treino
    path('excluir_treino/<int:treino_id>/', views.excluir_treino, name='excluir_treino'),
    
    # Cadastro de usuário
    path('cadastro/', views.cadastro, name='cadastro'),
    
    # Adicionar exercício associado a um treino específico
    path('treino/<int:treino_id>/add_exercicio/', views.add_exercicio, name='add_exercicio'),
    
    # Página de serviços
    path('servicos/', views.servicos, name='servicos'),  # Nova rota para a página de serviços
    
    path('criar_rotina/', views.criar_rotina, name='criar_rotina'),
    
    path('rotina/<int:rotina_id>/adicionar_treinos/', views.adicionar_treinos, name='adicionar_treinos'),

    path('treino/<int:treino_id>/editar/', views.editar_treino, name='editar_treino')

]
