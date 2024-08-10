from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.api_urls')),  # Use /api/ as a prefix for API routes
]
