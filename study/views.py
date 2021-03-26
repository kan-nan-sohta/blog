from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

def index(request):
    params = {
        'path': settings.STATIC_URL
    }
    return render(request, 'study/index.html', params)
    
# Create your views here.
