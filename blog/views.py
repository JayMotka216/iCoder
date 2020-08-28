from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages

def blogHome(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request, 'blog/blog.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    comments = BlogComment.objects.filter(post = post)
    params = {'post':post, 'comments':comments,'user':request.user}
    return render(request, 'blog/blogPost.html', params)
# Create your views here.

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        print(user)
        postId = request.POST.get('postId')
        post = Post.objects.filter(sno=postId).first()
        if user is 'AnonymousUser':
            messages.error(request, "Please Log In to post a comment!")
            return redirect(f'blog/{post.slug}')
        else:
            print(post)
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Commented Posted Successfully!")
    return redirect(f'/blog/{post.slug}')