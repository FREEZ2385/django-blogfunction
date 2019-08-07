from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}
    return render(request, 'blogmain/index.html', context)
