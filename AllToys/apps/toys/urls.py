from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('toys/', views.get_toys, name='toys'),
    path('toys/<int:id>/', views.get_toy_detail, name='toy_detail'),
]
