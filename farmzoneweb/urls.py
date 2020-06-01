from django.urls import path
from django.conf.urls import url , include

from . import views

app_name = 'farmzoneweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    # #path('admin')
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('forum.html', views.forum, name='forum'),
    path('ads/listings.html', views.listings, name='marketplace'),
    path('ads/listings-single.html', views.listing_single, name='ad-page'),
    path('accounts/login.html', views.login, name='Login'),
    path('ads/postitem.html', views.post_item, name='post-item'),
    path('accounts/profile.html', views.profile, name='profile'),
    path('accounts/register.html', views.register, name='register'),

]
