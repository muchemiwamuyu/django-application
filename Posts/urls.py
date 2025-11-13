from django.urls import path
from .views import hello_world

urlPatterns = [
    path('', hello_world, name='hello_world'),
]