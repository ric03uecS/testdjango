import datetime

from django.test import TestCase
from myapp.models import Post

class BlogPostTestCase(TestCase):
    fixtures = ['fixtures/fixture',]
    def setUp(self):
        Post.objects.create(id=1, 
            title='Starting a Django 1.6 Project the Right Way', 
            date=datetime.datetime.now(),
            category='Django')
        Post.objects.create(id=2, 
            title='Python\'s Hardest Problem', 
            date=datetime.datetime.now(),
            category='Python')

    def test_posts_have_category(self):
        """Animals that can speak are correctly identified"""
        first_post = Post.objects.get(id=1)
        second_post = Post.objects.get(id=2)
        third_post = Post.objects.get(id=3)
        fourth_post = Post.objects.get(id=4)
        self.assertEqual(first_post.category, 'Django')
        self.assertEqual(second_post.category, 'Python')
        self.assertEqual(third_post.category, 'imagine')
        self.assertEqual(fourth_post.category, 'beatles')
