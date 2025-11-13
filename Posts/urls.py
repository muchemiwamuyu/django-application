from django.urls import path
from .views import hello_world, about, Blogs

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('about/', about, name='about'),
    path('blogs/', Blogs, name='blogs'),
]