from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extra

def blogHome(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request, 'blog/blog.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    comments = BlogComment.objects.filter(post = post, parent=None)
    replies = BlogComment.objects.filter(post = post).exclude(parent=None)
    rep = {}
    for reply in replies:
        if reply.parent.sno not in rep.keys():
            rep[reply.parent.sno]=[reply]
        else:
            rep[reply.parent.sno].append(reply)
    params = {'post':post, 'comments':comments,'user':request.user, 'replies':rep}
    return render(request, 'blog/blogPost.html', params)
# Create your views here.

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        print(user)
        postId = request.POST.get('postId')
        post = Post.objects.filter(sno=postId).first()
        parentsno = request.POST.get('parentId')
        if parentsno == '':
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Commented Posted Successfully!")
        else:
            parent = BlogComment.objects.get(sno=parentsno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Reply Posted Successfully!")
        if user == 'AnonymousUser':
            messages.error(request, "Please Log In to post a comment!")
            return redirect(f'blog/{post.slug}')
    return redirect(f'/blog/{post.slug}')