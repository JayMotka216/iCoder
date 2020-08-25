from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('Home')

def blog(request):
    return HttpResponse('Blog')
# Create your views here.
