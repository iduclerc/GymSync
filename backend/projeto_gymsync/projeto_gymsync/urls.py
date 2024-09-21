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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', views.forum, name='forum'),
    path('forum/criar_treino',views.criar_treino,name='criar_treino'),
    #path('forum/criar_treino/',views.criar_treino,name='lista_treino'),
    path('forum/criar_treino.html/add_exercicio.html',views.add_exercicio,name='add_exercicio'),
    path('forum/lista_treino.html', views.lista_treinos, name='lista_treinos'),
    path('forum/lista_treino.html',views.excluir_treino, name="excluir_treino"),
    path('forum/add_exercicio.html/<int:treino_id>',views.add_exercicio,name="add_exercicio")
 ]
