from rest_framework import serializers

from .models import  Chat



class ChatSerializer(serializers.ModelSerilizer):

    class Meta:
        '''serializing the data'''
        model = Chat
        fields = '__all__'
