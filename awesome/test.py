from django.contrib.auth.models import User
from django.test import TestCase
from .models import *


# tests go here
class ThreadCreateTestCase(TestCase):
	def setUp(self):
		self.u1 = User.objects.create(username='user1')

	def tearDown(self):
		self.u1.delete()

	def test_thread_create(self):
		Post.objects.create(author=self.u1, title='Sample title', text='Sample Test')
		print(Post.objects.all())
