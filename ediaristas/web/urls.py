# Importa pacote do django para facilitar na configuração de caminhos no diretório
from django.urls import path

# Importa métodos definidos no arquivo views.py
from .views import cadastrar_diarista, listar_diaristas, editar_diarista, remover_diarista

# Array para determinar quais as rotas da aplicação
urlpatterns = [
    # Indica que o caminho 'cadastrar_diarista' utilizará o método cadastrar_diarista
    path('cadastrar_diarista', cadastrar_diarista, name='cadastrar_diarista'),

    # Rota para método listar_diaristas
    path('listar_diaristas', listar_diaristas, name='listar_diaristas'),

    # Rota para método editar_diarista -> precisa do parâmetro diarista_id do tipo inteiro
    path('editar_diarista/<int:diarista_id>', editar_diarista, name='editar_diarista'),

    # Rota para método remover_diarista
    path('remover_diarista/<int:diarista_id>', remover_diarista, name='remover_diarista'),
]