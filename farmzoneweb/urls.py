from django.urls import path

from . import views

app_name = 'farmzoneweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    # #path('admin')
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('forum.html', views.forum, name='forum'),
    path('listings.html', views.listings, name='marketplace'),
    path('listings-single.html', views.listing_single, name='ad-page'),
    path('login.html', views.login, name='Login'),
    path('postitem.html', views.post_item, name='post-item'),
    path('profile.html', views.profile, name='profile'),
    path('register.html', views.register, name='register'),

]
