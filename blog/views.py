from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .form import BlogPost
from .models import Blog

# Create your views here.

def index(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}
    return render(request, 'blogmain/index.html', context)

def write(request):
        if request.method == "POST":
            form = BlogPost(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.blog_time = timezone.now()
                post.save()
                return redirect('/')
        else:
            form = BlogPost()
            return render(request, 'blogmain/new.html', {'form': form})

'''
def writeprocess(request):
    blog = Blog()
    if request.method == "POST":
            blog.blog_title = request.POST["title"]
            blog.blog_subtitle = request.POST["subtitle"]
            blog.blog_contents = request.POST["content"]
            blog.blog_time = timezone.now()
            try:
                blog.save()
            except Exception as e:
                return HttpResponse("failed")
    return redirect('/')
'''
def writeprocess(request):
    if request.method == "POST":
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog_time = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = BlogPost()
        return render(request, "new.html", {'form': form})

def delete(request, num):
    try:
        Blog.objects.filter(blog_num = num).delete()
    except Exception as e:
        return HttpResponse("Failed")
    return redirect('/')

def detail(request, num):
    blog = Blog.objects.filter(blog_num = num)
    context = {'blogs':blog}
    return render(request, 'blogmain/details.html', context)
