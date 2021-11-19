from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Header(models.Model):
    title=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='Logo/')

    def __str__(self):
        return self.title

class Navbar(models.Model):
    title=models.CharField(max_length=255)
    href=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    order=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Footer(models.Model):
    name=models.CharField(max_length=100,default=None, null=True, blank=True)
    f_logo=models.ForeignKey(Header,on_delete=models.CASCADE)
    f_title1=models.CharField(max_length=255,null=True,blank=True)
    f_title2=models.CharField(max_length=255,null=True,blank=True)
    f_title3=models.CharField(max_length=255,null=True,blank=True)
    f_title4=models.CharField(max_length=255,null=True,blank=True)
    f_title5=models.CharField(max_length=255,null=True,blank=True)
    nav_menu=models.ForeignKey(Navbar,on_delete=models.CASCADE)
    t1=models.CharField(max_length=255,null=True,blank=True)
    t2=models.CharField(max_length=255,null=True,blank=True)
    t3=models.CharField(max_length=255,null=True,blank=True)
    t4=models.CharField(max_length=255,null=True,blank=True)
    t5=models.CharField(max_length=255,null=True,blank=True)
    a1=models.CharField(max_length=255,null=True,blank=True)
    a2=models.CharField(max_length=255,null=True,blank=True)
    a3=models.CharField(max_length=255,null=True,blank=True)
    a4=models.CharField(max_length=255,null=True,blank=True)
    a5=models.CharField(max_length=255,null=True,blank=True)



class Service(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField(upload_to='service_img/')
    desc=models.TextField()
    href=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


    




