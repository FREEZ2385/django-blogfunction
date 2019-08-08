from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Blog

# Create your views here.

def index(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}
    return render(request, 'blogmain/index.html', context)

def write(request):
    return render(request, 'blogmain/write.html')

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
<<<<<<< HEAD
=======
        else:
            return HttpResponse("failed")
>>>>>>> 5704cc1cf095cba56d8d78fa3791d388cf0f300c
    return redirect('/')

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
