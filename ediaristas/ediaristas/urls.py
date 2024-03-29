"""ediaristas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Importa settings e static para utilizar na indicação do diretório de imagens
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

# Importa método include para incluir o arquivo urls da aplicação web
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Indica que as rotas do arquivo urls da aplicação web serão utilizadas com 'web/' antes da rota
    path('administracao/', include('administracao.urls')),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
