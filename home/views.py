from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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

def handleSignUp(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        cpass = request.POST['cpass']
        if len(uname)>10:
            messages.error(request, 'Username should be less than 10 characters!')
            return redirect('/')
        if cpass != pass1:
            messages.error(request, "Please Enter same password!")
            return redirect('/')
        myuser = User.objects.create_user(uname, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "You have successfully signed up!")
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

def handleLogIn(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pas = request.POST['pass']
        user = authenticate(username=uname, password=pas)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully loged in!")
            return redirect('/')
        else:
            messages.error(request, "Invalide Credentials, Please try again!")
            return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

def handleLogOut(request):
    logout(request)
    messages.success(request, "You have successfully loged out!")
    return redirect('/')
# Create your views here.
