from django.db import models
from django.utils import timezone
from markdown import markdown
from bs4 import BeautifulSoup

# Create your models here.


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def add(self):
		self.published_date = timezone.now()
		self.save()

	def html(self):
		return markdown(self.text)

	def plainText(self):
		return ''.join(BeautifulSoup(self.html()).findAll(text=True))

	def __str__(self):
		return self.title
