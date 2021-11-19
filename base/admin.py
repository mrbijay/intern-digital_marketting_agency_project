from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Header)
class NavbarAdmin(admin.ModelAdmin):
    list_display=('title','order','href','is_active',)
    list_editable = ('order',)
admin.site.register(Navbar,NavbarAdmin)

class FooterAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Footer,FooterAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','img')
admin.site.register(Service,ServiceAdmin)
