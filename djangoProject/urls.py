# djangoProject/urls.py

from django.contrib import admin
from django.urls import path, include  # Ensure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # This line includes your accounts app URLs
]
