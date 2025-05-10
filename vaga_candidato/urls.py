from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_candidatos, name='lista_candidatos'),
    path('candidato/<int:candidato_id>/',
         views.candidato_detalhe, name='candidato_detalhe'),
    path('vaga/<int:vaga_id>/', views.vaga_detalhe, name='vaga_detalhe'),
    path('candidato/novo/', views.candidato_formulario, name='novo_candidato'),
    path('vaga/nova/', views.vaga_formulario, name='nova_vaga'),
]
