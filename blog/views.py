from django.shortcuts import render, HttpResponse

def blogHome(request):
    return render(request, 'blog/blog.html')

def blogPost(request, slug):
    params = {'slug':slug}
    return render(request, 'blog/blogPost.html', params)
# Create your views here.
