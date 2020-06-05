from django.conf.urls import include , url

from . import views


app_name = "chat_url"
urlpatterns = [

url(r"(?P<product_id>[\d]+)/$",views.save_chats , name = 'save_chats' ),
url(r"chat_view/(?P<product_id>[\d]+)/$",views.chat_view , name = 'chat_view' ),

]
