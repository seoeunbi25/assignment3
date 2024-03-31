from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

def create(request):
    if request.method=='POST':
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.content = request.POST['content']
    
        new_blog.save()

        return redirect('home')
    return render(request,'new.html')

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})
