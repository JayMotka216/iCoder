from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('Home')

def contact(request):
    return HttpResponse('Contact')

def about(request):
    return HttpResponse('About Us')
# Create your views here.
