from django.urls import path

from django.contrib import admin
from . import views





urlpatterns = [
    path('', views.home, name='Website-Home'),
    path('about/', views.about, name='Website-About'),
]