# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import ChatSerializer
from .models import Chat


class ChatViewSet(viewsets.ModelViewSet):
    '''creating view functions'''
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
