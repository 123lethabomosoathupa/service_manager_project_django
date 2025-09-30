from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm

# List view
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_manager/service_list.html', {'services': services})

# Detail view
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_manager/service_detail.html', {'service': service})

# Create new service
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service_manager/service_form.html', {'form': form})

# Edit service
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_manager/service_form.html', {'form': form})

# Delete service
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service_manager/service_detail.html', {'service': service})