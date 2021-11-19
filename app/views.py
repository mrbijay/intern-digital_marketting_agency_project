from django.shortcuts import render

from base.models import Footer, Header, Navbar, Service

# Create your views here.

def home(request):
    data=Navbar.objects.filter(is_active=True).order_by('order')
    header=Header.objects.all()
    footer=Footer.objects.all()
    return render(request, 'home.html',{'data':data,'header':header,'footer':footer})

def contact(request):
    data=Navbar.objects.filter(is_active=True).order_by('order')
    header=Header.objects.all()
    footer=Footer.objects.all()
    return render(request, 'contact.html',{'data':data,'header':header,'footer':footer})

def service(request):
    data=Navbar.objects.filter(is_active=True).order_by('order')
    header=Header.objects.all()
    footer=Footer.objects.all()
    service=Service.objects.all()
    return render(request, 'service.html',{'data':data,'header':header,'footer':footer,'service':service})

