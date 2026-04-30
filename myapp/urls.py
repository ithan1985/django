from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('dashboard/', views.dashboard, name='dashboard'),
]