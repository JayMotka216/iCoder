from django.shortcuts import render, HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages

def home(request):
    fetureposts = Post.objects.filter(fetured=True)
    features = {'fetured':fetureposts}
    return render(request, 'home/home.html', features)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.error(request, 'Please fill the Form correctly!')
        else:
            contact = Contact(name=name, mail=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has ben sent Successful!")
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET.get('query')
    if len(query) > 50:
        allpost=[]
    else:
        allposttitle = Post.objects.filter(title__icontains=query)
        allpostcontent = Post.objects.filter(content__icontains=query)
        allpostauthor = Post.objects.filter(author__icontains=query)
        allpost = allposttitle.union(allpostcontent).union(allpostauthor)
    params = {'allpost':allpost, 'query':query}
    return render(request, 'home/search.html', params)
# Create your views here.
