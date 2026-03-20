from django.urls import path
from . import views

urlpatterns = [
    path('anunciar/', views.anunciar, name='anunciar'),
    path('anunciar/produto/', views.anunciar_produto, name='anunciar_produto'),
    path('anunciar/servico/', views.anunciar_servico, name='anunciar_servico'),
    path('meus-anuncios/', views.meus_anuncios, name='meus_anuncios'),
    path('editar-produto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('excluir-produto/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('editar-servico/<int:id>/', views.editar_servico, name='editar_servico'),
    path('excluir-servico/<int:id>/', views.excluir_servico, name='excluir_servico'),
    path('produto/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    path('servico/<int:id>/', views.detalhe_servico, name='detalhe_servico'),
    path('relatorio/', views.gerar_relatorio, name='gerar_relatorio'),
]
