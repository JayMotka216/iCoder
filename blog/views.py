from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment

def blogHome(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request, 'blog/blog.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    comments = BlogComment.objects.filter(post = post)
    params = {'post':post, 'comments':comments}
    return render(request, 'blog/blogPost.html', params)
# Create your views here.

def postComment(request):

    return redirect('/')