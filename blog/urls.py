from django.urls import path
from . import views


urlpatterns = [
    path('allblog/', views.blog , name='allblog'),
    path('blog/<str:slug>/<int:id>',views.single_blog,name='blog'),
    path('search/', views.search, name='search'),

]