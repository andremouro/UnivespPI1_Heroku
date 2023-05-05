from django.contrib import admin
from django.urls import path
from student import views



urlpatterns = [
    path('admin/', admin.site.urls), #definição do caminho para a página do administrador
    path('', views.HomeView.as_view()), #definição do caminho para a página principal, que irá carregar a classe HomeView (definida em views.py)
    path('descr', views.DescriptiveView.as_view()), #definição do caminho para a página com a estatística descritiva dos alunos, que irá carregar a classe DescriptiveView
    path('habits', views.HabitsView.as_view()), #definição do caminho para a página com a modelagem de dados dos alunos, que irá carregar a classe ModellingView
    path('model', views.ModellingView.as_view()),
    path('form', views.upload, name='upload'),
    path('home',views.home,name='home')

]
