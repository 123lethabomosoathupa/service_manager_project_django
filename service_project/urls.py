from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('service_manager.urls')),
    path('', RedirectView.as_view(url='/services/', permanent=True)),  # Redirect root
]
