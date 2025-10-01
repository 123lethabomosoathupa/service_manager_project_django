from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServiceForm
from .models import Service

# List all services
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_manager/service_list.html', {'services': services})

# View a single service
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_manager/service_detail.html', {'service': service})

# Create a new service (with image upload)
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)  # 👈 request.FILES handles file uploads
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service_manager/service_form.html', {'form': form})

# Edit an existing service
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_manager/service_form.html', {'form': form})

# Delete a service
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service_manager/service_confirm_delete.html', {'service': service})