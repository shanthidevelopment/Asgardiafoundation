from django.urls import path
from .import views

urlpatterns = [
    path('asgardia/', views.index),
]
