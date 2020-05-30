from django.db import models
import uuid

# Create your models here.

from backend.marketplace.models import Users , Category , ProductsAds

#chat table for commenting about a product
class Chat(models.Model):
    '''
    The implimentation for the caht table in which a user can comment
    about the product.
    '''
    chat_id = models.UUIDField(default = uuid.uuid4 , primary_key = True , unique = True)
    user_id = models.ForeignKey(Users , on_delete = models.CASCADE)
    message = models.TextField(max_length = 1255)
    message_post_time = models.DateTimeField(auto_now_add = True)
    # username .....my thougth is we have user_id we can the get the username using it
    #i aslo think we can get the time---- in full format instead of getting time and date separetely
    #it will be broken apart from there
    #i have added ads-id since am seeing its purposes for showing which commodity was
    # being commented about
    ads_id = models.ForeignKey(ProductsAds , on_delete = models.CASCADE)
    category_id = models.ForeignKey(Category , on_delete = models.CASCADE)



    class Meta():
        '''
        Name for the table.
        '''
        db_table = "Chat"

# <<<<<<< HEAD
    # def __str__():
    #     """Chat instance."""
# =======

    def __str__(self):
        """Check data."""

        return f'{self.message} by {self.user_id}'
