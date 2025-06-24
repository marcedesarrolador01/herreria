from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.services, name='services'),
    path('contacto/', views.contac, name='contact'),
    path('trabajos/', views.trabajos_lista, name='trabajos_lista'),
    path('productos/', views.product_list, name='product_list'),
    path('prueba-correo/', views.prueba_email, name='prueba_correo'),
]



