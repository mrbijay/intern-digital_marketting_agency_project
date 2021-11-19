from django.shortcuts import render
from base.models import Footer, Header, Navbar, Service
from blog.models import Blog, Category

# Create your views here.

def blog(request):
    data=Navbar.objects.filter(is_active=True).order_by('order')
    header=Header.objects.all()
    footer=Footer.objects.all()
    service=Service.objects.all()
    cat=Category.objects.all()
    blog=Blog.objects.all().order_by('-id')
    return render(request, 'blog.html',{'data':data,'header':header,'footer':footer,'service':service, 'cat':cat,'blog':blog})

def single_blog(request,id,slug):
    data=Navbar.objects.filter(is_active=True).order_by('order')
    header=Header.objects.all()
    footer=Footer.objects.all()
    service=Service.objects.all()
    cat=Category.objects.all()
    blog=Blog.objects.get(id=id)
    return render(request, 'blog_single.html',{'data':data,'header':header,'footer':footer,'service':service, 'cat':cat,'blog':blog})

def search(request):
    q=request.GET['q']
    data=Navbar.objects.filter(is_active=True).order_by('order')
    header=Header.objects.all()
    footer=Footer.objects.all()
    cat=Category.objects.all()
    blog=Blog.objects.filter(slug__icontains=q).order_by('-id')
    return render(request, 'search.html',{'data':data,'header':header,'footer':footer,'blog':blog,'cat':cat})
