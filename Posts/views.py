from django.shortcuts import render, redirect
from .models import Blog, subscribe
from django.http import HttpResponseNotFound
from .forms import BlogForm
from django.contrib import messages

# Create your views here.
def hello_world(request):
    context = {'message': "Hello from the blogs platform!"}
    return render(request, 'index.html', context )

def home(request):
    blogs = Blog.objects.order_by('-created_at')

    latest_blog = blogs.first()         # single item
    recent_blogs = blogs[1:4]           # next 3 posts

    context = {
        'latest_blog': latest_blog,
        'recent_blogs': recent_blogs
    }
    return render(request, 'index.html', context)


def about(request):
    context = {'message': "This is the about page of the blogs platform."}
    return render(request, 'about.html', context )

# listing blogs
def Blogs(request):
    blogs = Blog.objects.all()
    context = { 'blogs': blogs}
    return render(request, 'blogs.html', context)

# edit blog
def edit_blog(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return HttpResponseNotFound("Blog not found")  # Redirect if blog not found

    if request.method == 'POST':
        blog.title = request.POST.get('title', blog.title)
        blog.content = request.POST.get('content', blog.content)
        blog.published = 'published' in request.POST
        if 'image' in request.FILES:
            blog.image = request.FILES['image']
        blog.save()
        return redirect('blogs')     

    context = {'blog': blog}
    return render(request, 'edit_blog.html', context)

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blogs')
    else:
        form = BlogForm()
    
    context = {'form': form}
    return render(request, 'add_blog.html', context)

# subscribe view
def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        if subscribe.objects.filter(email=email).exists():
            messages.info(request, "You are already subscribed.")
        else:
            subscriber = subscribe(email=email)
            subscriber.save()
            messages.success(request, "Subscription successful!")
            return redirect('subscribe_view')
    return render(request, 'subscribe.html')