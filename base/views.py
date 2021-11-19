from django.shortcuts import render

from base.models import Footer, Header, Navbar

# Create your views here.

def base(request):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    return render(request, 'home.html',{'data':data,'header':header,'footer':footer})