from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string, get_template
from django.contrib.auth.decorators import login_required
from .models import ContactForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

@login_required(login_url='login')
def contact_us(request):
    if request.method =="POST":
        contact=ContactForm()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        messages.success(request , 'Successfully submitted your form. Thank You !')
        return redirect('contact_us')

    return render(request, 'contact_us.html')


    


    
    
    
    

    
    
