# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import ChatSerializer
from .models import Chat
from marketplace.models import Users , Category , ProductsAds
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ChatViewSet(viewsets.ModelViewSet):
    '''creating view functions'''
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

##########################################################################################
                          ADS CHAT VIEW
##########################################################################################
#id for the product ads will be gotten from the url
# @api_view["POST"]
def save_chats(request , product_id):
    try:
        request.session["user_id"]
        try:
            if request.method == "POST":

                message = request.POST['message']
                # a session will be set once login with user_id
                user_id = request.session["user_id"]
                #product id will be appended to the url
                ads_id = product_id
                category_id = ProductsAds.objects.get(ads_id = ads_id).category_id
                chats_fields = [message , ads_id , user_id]
                if message != "":
                    chat_save = Chat(user_id = user_id , message=message ,ads_id=ads_id ,category_id = category_id)
                    try:
                        chat_save.save()
                        return HttpResponse(:Successful send ads msgs)
                    except Exception as e:
                        return HttpResponse("An Error Occured while saving the messages")
                else:
                    return HttpResponse("Same page with ads")


            else:
                return("Same Page with ads")
        except Exception as e:
            return HttpResponse("Same Page with Ads Chat")

    except Exception as e:
        return HttpResponse("Redirect Login Page")



# get chats for each id

#will revisit to know what to use ..if all chats for a product will be displayed etc
# @api_view["GET"]

#anybody can viw
def chat_view(request , product_id):
    # get the chats for that products
    query = Chat.objects.filter(ads_id = product_id).order_by("message_post_time")
    return HttpResponse("Page with chats for a particular preduct")
