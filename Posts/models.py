from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return   self.title
    
    @classmethod
    def publish(cls):
        return cls.objects.filter(published=True)

class editorModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    blogs = models.ManyToManyField(Blog, related_name='editors')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class subscribe(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
