# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ThreadSerializer , ForumSerializer
from .models import Forum , Thread
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ThreadViewSet(viewsets.ModelViewSet):

    queryset = Thread.object.all()
    serializer_class = ThreadSerializer


class ForumViewSet(viewsets.ModelViewSet):

    queryset = Forum.object.all()
    serializer_class = ForumSerializer



#thread message saving
@api_view['POST']
def save_thread(request):
    try:
        user_id = session.request['user_id']
        thread_message = request.data.get('thread_message' , None)
        thread_fields = [user_id , thread_message]
        if not None in thread_fields and not "" in thread_fields:
            save_data =Thread(user_id =user_id , thread_message = thread_message)
            save_data.save()
            return_data=
            {
            "error":0,
            "message":"Successful saved"
            }
        else:
            return_data=
            {
            "error":1,
            "message":"Erro Blank"
            }


    except Exception as e:

        return_data=
        {
        "error":2,
        "message":f"error as {e}"
        }
    else:
        pass

    return Response(return_data)



# forum message endpoint for saving
@api_view["POST"]
def save_forum(request , thread):
    try:
        user_id = request.session['user_id']
        forum_post = request.data.get(forum_post , None)
        thread_id = thread

        forum_fields = [user_id , forum_post , thread_id]
        if None not in forum_fields and "" not in forum_fields:
            forum_save = Forum(user_id = user_id , forum_post = forum_post ,thread_id=thread_id)
            try:
                forum_save.save()
                return_data =
                {
                "error":0,
                "message":"Successful"
                }
            except Exception as e:

                return_data =
                {
                "error":1,
                "message":f"Error occured as {e}"
                }
    except Exception as e:
        return_data =
        {
        "error":2,
        "message":f"Error occured as {e}"
        }
    else:
        pass
    return Response(return_data)





# views methods
