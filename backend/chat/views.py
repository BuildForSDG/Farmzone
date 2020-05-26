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


#id for the product ads will be gotten from the url
@api_view["POST"]
def save_chats(request , product_id):
    try:
        message = request.data.get(message , None)
        # a session will be set once login with user_id
        user_id = request.session["user_id"]
        ads_id = product_id
        category_id = ProductsAds.objects.get(ads_id = ads_id).category_id
        chats_fields = [message , ads_id , user_id]
        if not None in chats_fields and not "" in chats_fields:
            chat_save = Chat(user_id = user_id , message=message ,ads_id=ads_id ,category_id = category_id)
            try:
                chat_save.save()
            except Exception as e:
                return_data =
                {
                "error":0,
                "message":f"Error occures as {e}"
                }
        else:
            return_data =
            {
            "error":1,
            "message":"Fill the spaces"
            }

    except Exception as e:
        return_data =
        {
        "error":2,
        "message":f"Error occures as {e}"
        }
    else:
        return_data =
        {
        "error":3,
        "message":f"Successful!"
        }

    return Response(return_data)



# get chats for each id

#will revisit to know what to use ..if all chats for a product will be displayed etc
@api_view["GET"]
def chat_view(request , product_id):
    # get the chats for that products
    query = Chat.objects.filter(ads_id = product_id).order_by("message_post_time")
    return query
