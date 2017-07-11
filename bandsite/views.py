from django.http import HttpResponse
from django.shortcuts import render

from .models import Photo, Video, Music


# Create your views here.
def index(request):
    return render(request, 'bandsite/home.html')

def about(request):
    return render(request, 'bandsite/aboutus.html')

def contact(request):
    return render(request, 'bandsite/contact.html')

def demo(request):
    return render(request, 'bandsite/demos.html')
