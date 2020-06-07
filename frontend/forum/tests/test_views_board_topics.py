from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Forum


class ForumTopicsTests(TestCase):
    def setUp(self):
        Forum.objects.create(name='Django', description='Farmers.')

    def test_forum_topics_view_success_status_code(self):
        url = reverse('forum_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_forum_topics_view_not_found_status_code(self):
        url = reverse('forum_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_forum_topics_view_contains_navigation_links(self):
        forum_topics_url = reverse('forum_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(forum_topics_url)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
