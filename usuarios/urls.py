from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.entrar, name='login'),
    path('logout/', views.sair, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar/', views.editar_perfil, name='editar_perfil'),

]
