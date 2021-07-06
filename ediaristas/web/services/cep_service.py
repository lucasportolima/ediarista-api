# Importa pacote requests(deve ser instalado) para fazer requisições http
import requests

# Define método para fazer requisição e buscar a cidade pelo cep
def buscar_cidade_cep(cep):
    # Define variável para receber a resposta da requisição
    response = requests.get(
        f"https://viacep.com.br/ws/{cep}/json/"
    )

    # Retorna a resposta da API
    return response