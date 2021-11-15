from . import views
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us , name='contact_us'),
    path('blog/', views.blog , name='blog'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)