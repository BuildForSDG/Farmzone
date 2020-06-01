# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ThreadSerializer , ForumSerializer
from .models import Forum , Thread
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render , redirect
from django.http import HttpResponse

class ThreadViewSet(viewsets.ModelViewSet):

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class ForumViewSet(viewsets.ModelViewSet):

    queryset = Forum.objects.all()
    serializer_class = ForumSerializer




##########################################################################################
                      # THREAD PART
############################################################################################
#thread message saving
# @api_view['POST']
def save_thread(request):
    if request.method == "POST":
        try:
            user_id = session.request['user_id']
            thread_message = request.POST['thread_message']
            thread_fields = [user_id , thread_message]
            if thread_message != "":
                save_data =Thread(user_id =user_id , thread_message = thread_message)
                save_data.save()
                return HttpResponse("Saved successfully")
            else:
                return HttpResponse("Blank return the forum main page")

        except Exception as e:
            return HttpResponse(f" Please login  {e}")
        else:
            pass

        return render(request , 'forum.html')
    else:
        return render(request , "forum.html")


def delete_thread(request , threadid):
    id = threadid
    #check if its the user
    try:
        user = request.session['user_id']
        userid =Thread.objects.get(thread_id = id).user_id_id
        if userid != user:
            return HttpResponse("Alert Not allowed")
        #
        else:
            pass
        try:
            # filter all the messages with the thread id and also thread itself
            del_thread =Thread.objects.get(thread_id = id).delete()
            forum_del = Forum.objects.filter(thread_id_id = id).delete()
        except Exception as e:
            return HttpResponse("Not deleted an error occured")
    except Exception as e:
        return HttpResponse("Allert page Not allowed to delete")



# can allow editing if possible
def edit_thread(request , threadid):
    id = threadid

    try:
        # ?check if loggedin
        userid = request.session['user_id']
        #check the message writer
        user = Thread.objects.get(thread_id = threadid).user_id_id
        if user != userid:
            return HttpResponse("Alert page to allowed to edit")
        else:
            pass
        try:

            # get the thread
            edit_thread =Thread.objects.get(thread_id = id)
        except Exception as e:
            return HttpResponse("Not deleted an error occured")

        else:
            if request.method == "POST":
                new_thread_message = request.POST['thread_message']
                edit_thread.thread_message = new_thread_message
                edit_thread.save()

            else:
                return render(request , 'forum.html')
    except Exception as e:
        return HttpResponse("Return Login page")


#this is the function to return all threads from the page
def all_threads(request):
    # rerturn all thread to be seen by all people
    try:
        # print("inside")
        request.session['user_id']
        # print("here")

    except Exception as e:
        # login page
        return HttpResponse("Return Login page")
    else:
        all_threads = Thread.objects.all().order_by("thread_post_time")
        return HttpResponse("Page to display all the threasd")





##########################################################################################
                      # FORUM PAGE PART
############################################################################################
# forum message endpoint for saving
# @api_view["POST"]
def save_forum(request , thread):
    try:
        user_id = request.session['user_id']
        if request.method== "POST":

            forum_post = requet.POST['forum_post']
            thread_id = thread

            # forum_fields = [user_id , forum_post , thread_id]
            if forum_post != "":
                forum_save = Forum(user_id = user_id , forum_post = forum_post ,thread_id=thread_id)
                try:
                    forum_save.save()
                    return HttpResponse("Default page afetr  a message for a htread is made")
                except Exception as e:
                    return HttpResponse("rerturn the forum page with the thread id")
        else:
            return render(request , 'forum.html')
    except Exception as e:
        return HttpResponse("Return Login page")



#function to show all replies to a thread
#this is the function to return all replies from the thread in a chat mmaner like
def all_forums(request , threadid):
    try:
        # checking if a user is logged in
        request.session['user_id']
        id = threadid


    except Exception as e:
        #return loggedin page
        return HttpResponse("Return Login page")
    else:
        all_forums = Forum.objects.filter(thread_id_id = id).order_by("forum_post_time")
        thread = Thread.objects.get(thread_id = id)
        return HttpResponse("Page to display all the messages from a particular thread")




#funcr-tion to delete the message

def delete_forum_msg(request , msg_id):
    id = msg_id
    try:
        #check if user in loggedin
        userid = request.session['user_id'].user_id_id

        #get the message
        msg_user_id = Forum.objects.get(forum_id = id)
        #compaire with userid from session
        if msg_user_id == userid:
            try:
                # get the message with the id
                forum_del = Forum.objects.get(forum_id = id).delete()
            except Exception as e:
                return HttpResponse("Not deleted an error occured")
        else:
            return HttpResponse('Page to allert you cant delete')
    except Exception as e:
        #go back to login
        return HttpResponse("Return Login page")
