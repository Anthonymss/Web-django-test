from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('registro/', views.registro, name='registro'),
    path('exportar-pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
]
