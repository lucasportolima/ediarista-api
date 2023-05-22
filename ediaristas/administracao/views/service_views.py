from django.shortcuts import render, redirect
from ..forms.service_forms import ServiceForm
from ..models import Service
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_servico(request):
    if request.method == 'POST':
        form_service = ServiceForm(request.POST)
        if form_service.is_valid():
            form_service.save()
            return redirect('listar_servicos')
    else:
        form_service = ServiceForm()
    return render(request, 'servicos/form_servico.html', {'form_service': form_service})

@login_required
def listar_servicos(request):
    services = Service.objects.all()
    return render(request, 'servicos/lista_servicos.html', {'services': services})

@login_required
def editar_servico(request, id):
    service = Service.objects.get(id=id)
    form_service = ServiceForm(request.POST or None, instance=service)
    if form_service.is_valid():
            form_service.save()
            return redirect('listar_servicos')
    return render(request, 'servicos/form_servico.html', {'form_service': form_service})

