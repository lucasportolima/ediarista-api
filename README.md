# Multi-stack_backend-Django
Backend com Django do projeto desenvolvido durante o workshop Multi-stack da Treina Web

## Alguns passos do projeto:

### 1. Iniciando projeto na IDE Pycharm:
  <a name='pacotes'></a>
  - Após criar o projeto com uma Virtual Enviroment(`venv`), deve-se instalar o `Django` em `File->Settings->Project: 
    name -> Python Interpreter -> Install(símbolo de +)`, então basta procurar por `Django`, marcar `Specify 
    Version` e clicar em `Install Packages`
  - Serão instaladas automaticamente algumas dependências do Django ao instalá-lo.
  - Após isso, deve-se abrir o terminal na própria IDE e verificar se a venv está ativa, o que é indicado, no Windows, 
    por (venv) antes do diretório. Caso não esteja, pode-se reiniciar o terminal e/ou ir para `Settings` novamente e 
    verificar se o `Python Interpreter` está corretamente especificado. 
  - Por fim, cria-se o projeto Django no terminal da IDE com o comando:
```
django-admin startproject nome_do_projeto
```
Nesse projeto:
```
django-admin startproject ediaristas
```

<a name='aplicacao'></a>

### 2. Iniciando uma aplicação:
- Primeiramente, deve-se verificar se está na pasta principal -> onde está o arquivo `manage.py`.
- Em seguida, deve-se executar o comando:
```
python manage.py startapp nome_da_aplicação
```
Nesse projeto:
```
python manage.py startapp web
```
- Ao criar a aplicação, será criada a pasta da aplicação com alguns [arquivos de configuração](#web/arquivos)
    
### 3. Executando projeto:
- Deve-se estar na pasta principal `ediaristas`
- Executa-se o projeto com o comando:
```
python manage.py runserver
```

### 4. Criando tabela
- Algumas observações iniciais: 
    - Será utilizado o sqlite que vem com o `venv` e não um banco instalado, como o mysql, postgres ou mongodb.
      
    <a name='migrations'></a>

    - Ao executar o projeto nas primeiras vezes, aparecerá um erro de migrations não executadas. Dentre elas, há 
      algumas principais que já vem com o Django, ou seja, não precisamos alterá-las, pelo menos inicialmente. Além 
      disso, essas migrations podem interferir na execução correta do programa, como a `admin`.
    - Porém, como o objetivo é criar a tabela para os dados das diaristas, segue-se direto para isso:
- Primeiro, é preciso executar no diretório do projeto, nesse caso na pasta `ediaristas`, o comando:
```
python manage.py makemigrations
```
OBS: Caso um model tenha sido modificado, esse comando deve ser executado novamente para verificar as migrations

Inicialmente, não haverá mudanças detectadas, pois a aplicação ainda não foi [registrada](#registro_app), é preciso 
dar o "poder" ao projeto para gerenciar a aplicação.

- Após registrar a aplicação, ainda será preciso instalar o pacote `Pillow` para utilizar o `ImageField` em `models.
  py` para a foto do usuário. Essa instalação é feita da mesma forma que a instalação do [Django](#pacotes).
- Por fim, após instalar o Pillow, pode-se executar novamente o comando acima para criar a migration baseada na 
  class Diarista definida em `models.py`. Essa migration pode ser encontrada na pasta migration na pasta da 
  aplicação com o nome dado após executar o comando, nesse caso será o arquivo `web/migrations/0001_initial.py`
  
OBS: Pode-se acessar o [DBeaver](#dbeaver) para visualizar a estrutura do banco configurado no `sqlite`

- Com a migration criada, pode-se executá-la para criar a tabela no banco de dados com o comando:
```
python manage.py migrate
```
Esse comando executará também as outras [migrations](#migrations) configuradas pelo Django

<a name='registro_app'></a>

### 5. Registrando uma aplicação
- Para indicar que o projeto deve gerenciar uma aplicação, ou seja, registrar uma aplicação, deve-se abrir o arquivo 
  `settings.py` na pasta do projeto, nesse caso `ediaristas/settings.py`, e incluir o nome da aplicação na array 
  `INSTALLED_APPS`, nesse caso:
```
'web',
```  

### 6. Configurando views e formulário
- Após configurar o arquivo python para criar o [formulário](#form_diarista) de diaristas, deve-se configurar o 
  arquivo `web/views.py` para renderizar o formulário -> é o arquivo que configuramos para receber uma requisição e 
  enviar uma resposta
- Configurar o arquivo `web/templates/form_diarista.html`
- Criar um arquivo `urls.py` no pasta web para indicar qual a rota para exibir o formulário.
- Indicar no arquivo `ediaristas/urls.py`(arquivo de urls do projeto) que as rotas da aplicação web serão utilizadas
  (arquivo de urls da pasta web)
- Configurar arquivo `ediaristas/settings.py` para definir onde as imagens enviadas no cadastro serão armazenadas:
Colocar após `STATIC_URL`
```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
Deve-se importar o `os`:
```
import os
from pathlib import Path
```
- Configurar arquivo `ediaristas/urls.py` para indicar qual o caminho para obter as fotos armazenada. Como, neste 
  caso, os arquivos serão armazenados no computador e não em um servidor, deve-se indicar um caminho estático(static):
Concatena com o array de `urlpatterns`
```
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```  
Deve-se importar o static e o settings:
```
from django.conf import settings
from django.conf.urls.static import static
```

### 7. Outros passos:
1. Criar função de listar diaristas em `web/views.py` e configurar rota para essa função em `urls.py`.
2. Adicionar redirecionamento(no `views.py`) para rota `/listar_diaristas` após cadastrar uma diarista.
3. Criar arquivo base para partes em comum nas templates -> `base.html`
4. Estilizar `base.html` com bootstrap:
```
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
```
5. Estilizar arquivo `lista_diaristas.html`:
```
<table class='table'>
```
6. Adicionar uma navbar:
```
<nav class="navbar navbar-expand-md navbar-dark bg-dark md-4">
        <a href="#" class="navbar-brand">Ediaristas - TreinaWeb</a>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a href="{% url 'listar_diaristas' %}" class="nav-link">Home</a>
                </li>
            </ul>
        </div>
</nav>
```
7. Estilizar formulário do arquivo `form_diarista.html` com o [pacote](#pacotes) `django-crispy-forms`
Essa estilização é feita dessa forma porque o formulário é gerado automaticamente a partir de um model, então não há 
   como incluir css diretamente no arquivo. 

8. Ativar o pacote crispy no arquivo `ediaristas/settings.py` em `INSTALLED_APPS` ao adicionar antes de `web`:
```
'crispy_forms',
```
9. Definir qual será o template pack que será utilizado. Isso é feito ao adicionar entre `INSTALLED_APPS` e 
    `MIDDLEWARES`:
```
CRISPY_TEMPLATE_PACK = 'nome_do_template_pack'
```    
Nesse caso:
```
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
10. Carregar pacote crispy no `form_diarista.html`.

11. Criar botão de cadastrar em `lista_diaristas.html`:
```
<a href="{% url 'cadastrar_diarista' %}" class="btn btn-primary">Cadastrar</a>
```

12. Criar método de editar dados de uma diarista e configurar uma rota para esse método.

13. Criar método para remover uma diarista e configurar uma rota.

14. Adicionar máscaras nos inputs com o plugin `JQuery Mask CDN` -> colocar script em `base.html`:
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.16/jquery.mask.min.js" 
integrity="sha512-pHVGpX7F/27yZ0ISY+VVjyULApbDlD0/X0rgGbTqCE7WFW5MezNTWG/dnhtbBuICzsd0WQPgpE4REBLv+UqChw==" 
crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```
O JQuery Mask precisa do JQuery, então é preciso instalá-lo também:
```
<script src="https://code.jquery.com/jquery-3.6.0.min.js" 
integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
```

15. Ativar o `JQuery Mask CDN` com o script(no base.html tb):
```
<script>
        $(function(){
            $.applyDataMask();
        });
</script>
```
Deve-se especificar os campos com máscara no arquivo `diarista_form.py`.

16. Retirar máscaras ao submeter os dados no arquivo `diarista_form.py`, pois elas contam como caracteres e foi 
    definido um limite anteriormente.
    
17. Adicionar máscaras na exibição do cep ao listar as diaristas com o [pacote](#pacotes) `easy-mask`. Deve-se 
    adicioná-lo ao array de `INSTALLED_APPS` de `ediaristas/settings.py`:
```
'easy_mask',
```    
Após isso, basta carregar o pacote em `lista_diaristas`.

18. Implementar o serviço [ViaCEP](https://viacep.com.br/) para obter o código do IBGE ao cadastrar uma diarista. 
    Para isso, deve-se criar um [arquivo](#viacep) para se comunicar com esse serviço e com a aplicação web -> 
    `cep_service.py`.
    
19. Remover o campo `Código ibge` do formulário em `diarista_form.py`, pois será usada a API para o preencher antes de 
    salvar a diarista.

20. Utilizar o arquivo `cep_service.py` em `diarista_form.py` para tratar e utilizar a resposta da API para validar 
    o cep.
    
21. Armazenar o valor do código do IBGE retornado pela API se o CEP for válido. Para isso, deve-se sobrescrever o 
    método `save`, método utilizado para guardar os dados no banco, em `diarista_form`.
    
22. Iniciar a API -> nova [aplicação](#aplicacao)

## Pastas e arquivos:
O `Django` trabalha com o esquema: um projeto para várias aplicações, em que cada aplicação é responsável por 
resolver um problema

- `ediaristas`: pasta do projeto criada dentro da pasta principal com o mesmo nome(ediaristas)
    - `settings.py` -> configurações globais, ou seja, para todas as aplicações
    - `urls.py` -> definição de urls globais para o projeto
    
- `web`:
  <a name='web/arquivos'></a>
  - `admin.py` -> define algumas configurações do módulo administrativo do Django e pode ser utilizado para 
    realizar operações de CRUD, já vem com o sistema todo pronto para gerenciamento de tabelas
  - `apps.py` -> definir algumas configurações da aplicação
  - `models.py` -> define quais tabelas serão utilizadas
  - `tests.py` -> mais relacionado a testes unitários
  - `views.py` -> tratamento das requisições. É o meio de campo entre as aplicações e/ou entre as camadas da 
    aplicação. Define o que é exibido e quando é exibido.
    
  - `templates`: armazenar os arquivos html para a aplicação.
    - `form_diarista.html`: cadastro e edição de uma diarista
    - `lista_diaristas.html`: listar diaristas registradas no banco de dados
  - `forms`: armazenar arquivos que configurarão como os formulários se comportarão -> o Django possui uma 
    ferramenta que facilita a criação de formulários a partir de um model de forma automática
    <a name='form_diarista'></a>
    - `form_diaristas.py`: configurará como o formulário de diaristas irá se comportar -> criará a partir do model 
      de diarista
  - `services`: armazenar arquivos para se comunicar com serviços externos(APIs, web services)
    - `cep_service.py`: conectar com o serviço [ViaCEP](https://viacep.com.br/) e receber a resposta com os dados e 
      passar para a aplicação web.

Aula 4 - 00:25:00
