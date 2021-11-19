from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Author(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    address=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Blog(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='thumbnails')
    heading1=models.CharField(max_length=255, null=True)
    blog_desc1=models.TextField()
    image1=models.ImageField(upload_to='blog_images')
    heading2=models.CharField(max_length=255, null=True, blank=True)
    blog_desc2=models.TextField(null=True,blank=True)
    image2=models.ImageField(upload_to='blog_images',null=True,blank=True)
    heading3=models.CharField(max_length=255, null=True, blank=True)
    blog_desc3=models.TextField(null=True,blank=True)
    image3=models.ImageField(upload_to='blog_images',null=True,blank=True)
    heading4=models.CharField(max_length=255, null=True, blank=True)
    blog_desc4=models.TextField(null=True,blank=True)
    image4=models.ImageField(upload_to='blog_images',null=True,blank=True)
    heading5=models.CharField(max_length=255, null=True, blank=True)
    blog_desc5=models.TextField(null=True,blank=True)
    image5=models.ImageField(upload_to='blog_images',null=True,blank=True)

    def __str__(self):
        return self.title