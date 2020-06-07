from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Forum


class HomeTests(TestCase):
    def setUp(self):
        self.forum = Forum.objects.create(
            name='Django', description='Farmers.')
        url = reverse('home')
        self.response = self.client.get(url)
