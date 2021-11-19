from django.contrib import admin

# Register your models here.

from blog.models import Author, Category ,Blog


# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Blog)
