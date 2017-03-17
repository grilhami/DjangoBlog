from django.test import TestCase
from django.utils import timezone
from .models import Post
import datetime

class PostViewTest(TestCase):

    def test_home(self):
        
        response = self.client.get('/')
        self.assertContains(response, 20, 200)

    def test_feed(self):
        
        response = self.client.get('/posts/')
        self.assertContains(response, 20, 200)


class PostModelTest(TestCase):

    def create_post(self, title="test", content="test content"):
        
        return Post.objects.create(title=title, content=content)

    def test_post_creation(self):

        new_post = self.create_post()
        self.assertEqual(isinstance(new_post, Post))
        self.assertEqual(new_post.user.id, 1)
        self.assertEqual(new_post.__str__, new.title)
        self.asserEqual(new_post.title, "test")

