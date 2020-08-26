from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')

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
# Create your views here.
