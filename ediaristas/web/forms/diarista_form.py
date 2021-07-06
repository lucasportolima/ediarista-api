# Importa pacote forms do djando para configurar a classe DiaristaForm
from django import forms

# Importa model de diarista para usar como base para criar o formulário
from ..models import Diarista

# Importa arquivo cep_service para utilizar API do ViaCEP
from ..services import cep_service

# Importa pacote json para tratar as respostas da API
import json

''' 
Classe que herda do pacote forms para configurar o formulário -> forms.Modelform -> "Modelform": form gerado a
partir de um model
'''
class DiaristaForm(forms.ModelForm):
    # Especificação de máscaras nos campos:
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "000.000.000-00"}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "00000-000"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "(00) 00000-0000"}))

    # Forma de tornar o campo opcional na hora de preencher o formulário -> deve-se alterar no model tb ou preencher
    # o campo de forma automática na hora de salvar no bando de dados -> sobrescreve o método save

    # codigo_ibge = forms.IntegerField(required=False)

    # Classe para definir meta configurações
    class Meta:
        # Indica qual o model que será usado como base para criar o formulário
        model = Diarista

        # Forma de indicar que todos os campos devem ser renderizados no formulário
        # fields = '__all__'

        # Indica que todos os campos devem ser renderizados no formulário, exceto o do codigo_ibge
        exclude = ('codigo_ibge', )

    # Métodos para retirar máscaras dos campos
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']

        # Retorna o cpf sem os caracteres da máscara
        return cpf.replace(".", "").replace("-", "")

    def clean_cep(self):
        cep = self.cleaned_data['cep']

        # Define variável para armazenar cep sem a máscara para poder enviar para a API ViaCEP
        cep_formatado = cep.replace("-", "")

        # Define variável para armazenar resposta da API obtida pelo arquivo cep_service
        response = cep_service.buscar_cidade_cep(cep_formatado)

        # Tratamento das respostas obtidas pela API(ver site)
        if response.status_code == 400:
            # Retorna erro de validação no formulário
            raise forms.ValidationError("CEP inválido")

        # Se não for 400, coloca o conteúdo da resposta na variável cidade_api
        cidade_api = json.loads(response.content)

        # Caso o cep não exista, a resposta será um erro: true, então verifica se existe a palavra erro na resposta
        if 'erro' in cidade_api:
            raise forms.ValidationError("CEP não encontrado")

        # Retorna o cep sem os caracteres da máscara
        return cep_formatado

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']

        # Retorna o telefone sem os caracteres da máscara
        return telefone.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")

    # Sobrescreve o método save para repassar o código do IBGE obtido pela API diretamente
    def save(self, commit=True):
        # Primeiramente, deve-se pegar a instância da diarista que está sendo cadastrada:
        instance = super(DiaristaForm, self).save(commit=False)
        # O "commit=False" indica que não deve-se colocar no banco de dados ainda, pois será feita alguma alteração

        # Pega a resposta da API:
        response = cep_service.buscar_cidade_cep(self.cleaned_data.get('cep'))
        # "self.cleaned_data.get('cep')" -> pega o cep da diarista já limpo(cleaned), ou seja, já tratado e sem máscara

        # Pega o conteúdo da resposta da API(código do ibge, bairro, etc):
        cidade_api = json.loads(response.content)

        # Atribui o código do ibge obtido da API na instância da diarista que está sendo tratada
        instance.codigo_ibge = cidade_api['ibge']

        # Salva a instância da diarista
        instance.save()

        # Retorna a instância da diarista
        return instance