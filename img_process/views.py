from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
import cv2
import numpy as np
from django.conf import settings

def index(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
        max_id = Document.objects.latest('id').id
        obj = Document.objects.get(id = max_id)
        input_path = obj.photo.url
        output_path =settings.MEDIA_URL + 'output/output.png'
        img_process(input_path, output_path)
    return render(request, 'img_process/index.html', {
        'form': form,
        'obj': obj,
    })

def img_process(input_path, output_path):
    print(input_path)
    print(output_path)
    inp = cv2.imread(input_path)
    print(inp)
    out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, out)



# Create your views here.
