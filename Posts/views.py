from django.shortcuts import render
from .models import Blog

# Create your views here.
def hello_world(request):
    context = {'message': "Hello from the blogs platform!"}
    return render(request, 'index.html', context )

def about(request):
    context = {'message': "This is the about page of the blogs platform."}
    return render(request, 'about.html', context )

# listing blogs
def Blogs(request):
    blogs = Blog.objects.all()
    context = { 'blogs': blogs}
    return render(request, 'blogs.html', context)
