# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ThreadSerializer , ForumSerializer
from .models import Forum , Thread


class ThreadViewSet(viewsets.ModelViewSet):

    queryset = Thread.object.all()
    serializer_class = ThreadSerializer


class ForumViewSet(viewsets.ModelViewSet):

    queryset = Forum.object.all()
    serializer_class = ForumSerializer
