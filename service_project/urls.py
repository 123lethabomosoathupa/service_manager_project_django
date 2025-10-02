from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from service_manager import views as service_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Root → redirect to service list
    path('', lambda request: redirect('service_list'), name='home'),

    # App URLs
    path('services/', include('service_manager.urls')),

    # Auth
    path('login/', service_views.user_login, name='login'),
    path('register/', service_views.user_register, name='register'),
    path('logout/', service_views.user_logout, name='logout'),
]
