# from django.db import models

# Create your models here.
from backend.marketplace.models import Users

# Create your models here.
from django.db import models
import uuid

#userid from model Usser is used for forum messaging



#theead tabel

class Thread(models.Model):
    '''
    The starter for the thread
    Once it has been created  by a user,,
    Other people can comment about it.
    '''
    thread_id = models.UUIDField(primary_key = True , unique = True , default=uuid.uuid4)
    user_id = models.ForeignKey(Users , on_delete = models.CASCADE)
    thread_message = models.TextField(max_length = 1255)
    thread_post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Name for the table.
        '''
        db_table = "Thread"

    def _str__(self):
        """Thread instance."""
        return f'{self.thread_message}  by user_id {self.user_id}'


class Forum(models.Model):
    '''
    The class to create db for the forum messaging details
    with the time of post
    poster who posted
    and the messages itself
    The model will be a reply from # thread table.
    '''
    forum_id = models.UUIDField(primary_key = True , unique = True , default=uuid.uuid4)
    user_id = models.ForeignKey(Users,on_delete = models.CASCADE)#this is not indicated in the schema
    forum_post = models.TextField(max_length=1255)
    forum_post_time = models.DateTimeField(auto_now_add=True)
    thread_id = models.ForeignKey(Thread , on_delete = models.CASCADE)




    class Meta:
        '''
        Name for the table.
        '''
        db_table = "Forum"

    def __str__(self):
        """Checking forum instance."""
        return f'{self.forum_post}  by user_id {self.user_id} on thread with id {self.thread_id}'
