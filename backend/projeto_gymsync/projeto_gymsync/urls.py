"""
URL configuration for projeto_gymsync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_gymsync import views # possivel erro de algo
from . import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.forum, name='forum'),
    path('criar_treino/',views.criar_treino,name='criar_treino'),
    #path('forum/criar_treino/',views.criar_treino,name='lista_treino'),
    #path('forum/criar_treino.html/add_exercicio.html',views.add_exercicio,name='add_exercicio'),
    path('lista_treino/', views.lista_treinos, name='lista_treinos'),
    #path('forum/lista_treino/',views.excluir_treino, name="excluir_treino"),
    path('forum/<int:treino_id>/add_exercicio/',views.add_exercicio,name='add_exercicio'),
    path('excluir_treino/<int:treino_id>/', views.excluir_treino, name='excluir_treino'),
    path('cadastro/', views.cadastro, name='cadastro'),
     path('treino/<int:treino_id>/add_exercicio/', views.add_exercicio, name='add_exercicio'),
    
    # Página de serviços
    path('servicos/', views.servicos, name='servicos'),  # Nova rota para a página de serviços
    
    path('criar_rotina/', views.criar_rotina, name='criar_rotina'),
    
    path('rotina/<int:rotina_id>/adicionar_treinos/', views.adicionar_treinos, name='adicionar_treinos'),
    path('treino/<int:treino_id>/editar/', views.editar_treino, name='editar_treino'),
    
    path('login/', views.login_view, name='login'),
 ]
