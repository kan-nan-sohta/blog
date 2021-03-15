from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    params = {
        'path': os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    }
    return render(request, 'study/index.html', params)
    
# Create your views here.
