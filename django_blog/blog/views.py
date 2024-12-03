from django.shortcuts import render

from .models import Post

def home(request):
    posts = Post.objects.all()  # Retrieve all blog posts
    return render(request, 'blog/home.html', {'posts': posts})  # Pass posts to the template
