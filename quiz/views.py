from django.shortcuts import render,HttpResponse
from . import views
# Create your views here.

def home(request):
    return HttpResponse('Hello')