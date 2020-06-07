from django.test import TestCase
from django.urls import reverse
from ..models import Forum


class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        Forum.objects.create(name='Farmzone', description='Topic.')
        self.url = reverse('new_topic', kwargs={'pk': 1})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(
            login_url=login_url, url=self.url))
