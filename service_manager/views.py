from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from .models import Service

# 🔑 User Registration
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('service_list')
    else:
        form = UserCreationForm()
    return render(request, 'service_manager/register.html', {'form': form})

# 🔑 User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('service_list')
    else:
        form = AuthenticationForm()
    return render(request, 'service_manager/login.html', {'form': form})

# 🔑 User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# Services (Protected)
@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_manager/service_list.html', {'services': services})

@login_required
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_manager/service_detail.html', {'service': service})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service_manager/service_form.html', {'form': form})

@login_required
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

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service_manager/service_confirm_delete.html', {'service': service})
