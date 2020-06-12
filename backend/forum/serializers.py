from rest_framework import serializers
from .models import Thread , Forum


class ThreadSerializer(serializers.ModelSerializer):
    '''Serialize the data'''
    model = Thread
    fields = '__all__'


class ForumSerializer(serializers.ModelSerializer):
    '''Serialize forum data'''
    model = Forum
    fields = '__all__'
