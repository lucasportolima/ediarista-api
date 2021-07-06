from django.shortcuts import render, redirect

# Importa arquivo para ser usado para auxiliar na renderização do formulário
from .forms import diarista_form

# Importa model de Diarista
from .models import Diarista

# Método para cadastrar uma diarista
# Recebe a request como parâmetro
def cadastrar_diarista(request):
    # Verifica se o tipo/método da requisição é post, pois, se for, significa que está sendo feito um cadastro.
    if request.method == 'POST':
        """
        Cria uma instância de diarista_form com os dados enviados pelo formulário:
        POST para os campos de texto
        FILES para a foto
        """
        form_diarista = diarista_form.DiaristaForm(request.POST, request.FILES)

        # Verifica se os dados enviados para form_diarista são válidos
        if form_diarista.is_valid():
            # Se os dados forem válidos, salva no banco de dados
            form_diarista.save()

            # Retorna redirecionamento para a rota "listar_diaristas" caso o cadastro dê certo -> deve-se utilizar o
            # mesmo nome definido em "name" ao configurar a rota em "web/urls.py"
            return redirect('listar_diaristas')

    # Se o método não for post, exibe o formulário para preencher
    else:
        # Instancia a classe DiaristaForm para utilizar o form baseado no model Diarista
        form_diarista = diarista_form.DiaristaForm()

    # Retorna a renderização do arquivo form_diarista.html e repassa a request e a instância
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista, 'tipo_form': 'Cadastrar'})

# Método para listar as diaristas
def listar_diaristas(request):
    # Variável que recebe todas as diaristas do banco
    diaristas = Diarista.objects.all()

    # Retorna renderização do arquivo e envia os dados das diaristas
    return render(request, 'lista_diaristas.html', {'diaristas': diaristas})

# Método para editar dados de uma diarista -> recebe como parâmetro a request e o id da diarista que deseja-se editar
def editar_diarista(request, diarista_id):
    # Variável que recebe os dados da diarista com o id correspondente
    diarista = Diarista.objects.get(id=diarista_id)

    # Verifica se o tipo/método da requisição é post, pois, se for, significa que está sendo feito um cadastro.
    if request.method == 'POST':

        # Instância do formulário com base no model com os dados dessa diarista preenchendo os campos
        form_diarista = diarista_form.DiaristaForm(request.POST or None, request.FILES, instance=diarista)

        # Após alterar os campos do formulário instanciado, verifica se esse formulário é válido
        if form_diarista.is_valid():
            # Se for válido, salva no banco de dados
            form_diarista.save()

            # Redireciona se tudo der certo
            return redirect('listar_diaristas')

    # Se o método não for post, exibe o formulário com base nos dados da diarista
    else:
        # Instância do formulário com os campos preenchidos com os dados da diarista encontrada pelo id
        form_diarista = diarista_form.DiaristaForm(instance=diarista)

    # Renderiza o formulário com os dados da diarista com id indicado
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista, 'tipo_form': 'Editar'})

# Método para remover uma diarista
def remover_diarista(request, diarista_id):
    # Variável que recebe os dados da diarista com o id correspondente
    diarista = Diarista.objects.get(id=diarista_id)

    # Remove diarista
    diarista.delete()

    # Redireciona para listagem
    return redirect('listar_diaristas')