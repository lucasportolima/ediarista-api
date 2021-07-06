from django.db import models

# Classe "Diarista" -> nome da tabela
# Essa classe herda de models.Model -> é um model do Django
class Diarista(models.Model):
    # Definição dos dados da tabela

    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    # CharField -> armazena dados do tipo char -> na tabela, esses tipos são convertidos para os usados no banco, por exemplo, o CharField será o varchar para o banco sql.
    # null=False e blank=False -> ão permite valor null nem em branco

    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    # unique=True -> não pode existir cpf repetido

    email = models.EmailField()
    # EmailField já verifica se o formato digitado é de um email

    telefone = models.CharField(max_length=11, null=False, blank=False)

    logradouro = models.CharField(max_length=60, null=False, blank=False)

    numero = models.IntegerField(null=False, blank=False)

    bairro = models.CharField(max_length=30, null=False, blank=False)

    complemento = models.CharField(max_length=100, null=False, blank=True)
    # blank=True, pois o complemento pode não existir

    cep = models.CharField(max_length=8, null=False, blank=False)

    estado = models.CharField(max_length=2, null=False, blank=False)
    # Armazenar apenas a sigla do estado

    codigo_ibge = models.IntegerField(null=False, blank=False)
    # Para identificar a cidade, não apenas o cep(específico) ou o estado(geral) -> para a busca retornar diaristas da mesma cidade

    foto_usuario = models.ImageField(null=False)
    # Armazenar a foto do usuário -> o tipo ImageField só pode ser usado ao instalar o pacote Pillow