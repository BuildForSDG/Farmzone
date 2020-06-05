from django.conf.urls import url , include

from . import views
app_name = "forum_url"



urlpatterns =[

#thread urls
    url("^$" , views.all_threads , name = "all_threads"),
    url("add/$" , views.save_thread , name = "save_thread"),
    url(r"delete/(?P<threadid>[\d]+)/$" , views.delete_thread , name = "delete_thread"),
    url(r"edit/(?P<threadid>[\d]+)/$" , views.edit_thread , name = "edit_thread"),

    #forum urls
    url(r"(?P<threadid>[\d]+)/$" , views.all_forums , name = "all_forums"),
    url(r"(?P<thread>[\d]+)/reply/$" , views.save_forum , name = "save_forum"),
    url(r"(?P<msg_id>[\d+])/delete/$" , views.delete_forum_msg , name = "delete_forum_msg"),

]
