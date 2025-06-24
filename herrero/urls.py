from django.contrib import admin
from django.urls import path, include
from app.views import analytics_dashboard 
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/estadisticas/', analytics_dashboard, name='analytics_dashboard'),
    path('', include('app.urls')),  # si tenés esto, mantenelo
]


