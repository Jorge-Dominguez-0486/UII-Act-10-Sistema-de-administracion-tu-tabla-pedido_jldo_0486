
# app_pedido/urls.py

from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('pedido/<int:pedido_id>/', views.view_pedido, name='view_pedido'), 
    path('add/', views.add, name='add'),
    path('edit/<int:pedido_id>/', views.edit, name='edit'), 
    path('delete/<int:pedido_id>/', views.delete, name='delete'), # Usa pedido_id
]