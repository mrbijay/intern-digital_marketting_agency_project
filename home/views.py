from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string, get_template
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

@login_required(login_url='login')
def contact_us(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail(
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            html_message=message
        )
    return render(request, 'contact_us.html')


    


    
    
    
    

    
    
