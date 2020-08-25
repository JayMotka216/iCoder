from django.shortcuts import render, HttpResponse

def blogHome(request):
    return HttpResponse('Blog Home')

def blogPost(request, slug):
    return HttpResponse(f'Blog Post{slug}')
# Create your views here.
