from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    
    path('alunos', views.aluno_list, name='aluno_list'),
    path('aluno/<int:pk>/', views.aluno_detail, name='aluno_detail'),
    path('aluno/new', views.aluno_new, name='aluno_new'),
    path('aluno/<int:pk>/edit/', views.aluno_edit, name='aluno_edit'),
    path('aluno/<pk>/remove/', views.aluno_remove, name='aluno_remove'),

    path('cursos', views.curso_list, name='curso_list'),
    path('curso/<int:pk>/', views.curso_detail, name='curso_detail'),
    path('curso/new', views.curso_new, name='curso_new'),
    path('curso/<int:pk>/edit/', views.curso_edit, name='curso_edit'),
    path('curso/<pk>/remove/', views.curso_remove, name='curso_remove'),

    path('turmas', views.turma_list, name='turma_list'),
    path('turma/<int:pk>/', views.turma_detail, name='turma_detail'),
    path('turma/new', views.turma_new, name='turma_new'),
    path('turma/<int:pk>/edit/', views.turma_edit, name='turma_edit'),
    path('turma/<pk>/remove/', views.turma_remove, name='turma_remove'),

    path('turnos', views.turno_list, name='turno_list'),
    path('turno/<int:pk>/', views.turno_detail, name='turno_detail'),
    path('turno/new', views.turno_new, name='turno_new'),
    path('turno/<int:pk>/edit/', views.turno_edit, name='turno_edit'),
    path('turno/<pk>/remove/', views.turno_remove, name='turno_remove'),

    path('servidors', views.servidor_list, name='servidor_list'),
    path('servidor/<int:pk>/', views.servidor_detail, name='servidor_detail'),
    path('servidor/new', views.servidor_new, name='servidor_new'),
    path('servidor/<int:pk>/edit/', views.servidor_edit, name='servidor_edit'),
    path('servidor/<pk>/remove/', views.servidor_remove, name='servidor_remove'),

    path('refeicaos', views.refeicao_list, name='refeicao_list'),
    path('refeicao/<int:pk>/', views.refeicao_detail, name='refeicao_detail'),
    path('refeicao/new', views.refeicao_new, name='refeicao_new'),
    path('refeicao/<int:pk>/edit/', views.refeicao_edit, name='refeicao_edit'),
    path('refeicao/<pk>/remove/', views.refeicao_remove, name='refeicao_remove'),

    path('tipoRefeicaos', views.tipoRefeicao_list, name='tipoRefeicao_list'),
    path('tipoRefeicao/<int:pk>/', views.tipoRefeicao_detail, name='tipoRefeicao_detail'),
    path('tipoRefeicao/new', views.tipoRefeicao_new, name='tipoRefeicao_new'),
    path('tipoRefeicao/<int:pk>/edit/', views.tipoRefeicao_edit, name='tipoRefeicao_edit'),
    path('tipoRefeicao/<pk>/remove/', views.tipoRefeicao_remove, name='tipoRefeicao_remove'),

    path('reservas', views.reserva_list, name='reserva_list'),
    path('reserva/<int:pk>/', views.reserva_detail, name='reserva_detail'),
    path('reserva/new', views.reserva_new, name='reserva_new'),
    path('reserva/<int:pk>/edit/', views.reserva_edit, name='reserva_edit'),
    path('reserva/<pk>/remove/', views.reserva_remove, name='reserva_remove'),

]