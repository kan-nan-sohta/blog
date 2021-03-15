from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
from .models import Greeting

def index(request):
    blogs = Blog.objects.order_by('-id')
    context = {
        'blogs': blogs
    }
    return render(request, 'hello/index.html', context)

def detail(request, blog_id):
    blog_text = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog_text': blog_text
    }
    return render(request, 'hello/detail.html', context)

# from .models import Greeting

# Create your views here.
# def index(request):
#     params = {
#         'title': 'Hello/Index',
#         'msg': 'This is sample page',
#         'goto': 'next',
#     }
#     # return HttpResponse('Hello from Python!')
#     return render(request, "hello/index.html", params)

# def next(request):
#     params = {
#         'title': 'Hello/Next',
#         'msg': 'This is another page',
#         'goto': 'index',
#     }
#     return render(request, 'hello/index.html', params)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "hello/db.html", {"greetings": greetings})
