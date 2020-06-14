from django.urls import path
from django.conf.urls import url , include

from . import views

app_name = 'farmzoneweb'

urlpatterns = [
    path('aboutus.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('faqs.html', views.faqs, name='faqs'),
]
