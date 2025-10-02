# service_manager/admin.py
from django.contrib import admin
from .models import Service   # ✅ only Service

admin.site.register(Service)
