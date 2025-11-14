from django.urls import path
from .views import hello_world, about, Blogs, edit_blog, add_blog, subscribe_view

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('about/', about, name='about'),
    path('blogs/', Blogs, name='blogs'),
    path('edit/<int:blog_id>/', edit_blog, name='edit_blog'),
    path('add/', add_blog, name='add_blog'),
    path('subscribe/', subscribe_view, name='subscribe_view')
]