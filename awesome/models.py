from django.db import models
from django.utils import timezone
from markdown import markdown
from bs4 import BeautifulSoup


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	assoc = models.ForeignKey('Application', null=True, blank=True, default = None)
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

	def plain_text(self):
		return ''.join(BeautifulSoup(self.html(), "html.parser").findAll(text=True))

	def __str__(self):
		return self.title


class Tag(models.Model):
	TAG_TYPE_CHOICES = (
		('0', 'Category'),
		('1', 'Descriptive'),
		('2', 'Platform'),
	)
	name = models.CharField(max_length=100)
	type = models.CharField(max_length=1, choices=TAG_TYPE_CHOICES)
	desc = models.TextField()

	def __str__(self):
		return self.name


class Application(models.Model):
	APP_TYPE_CHOICES = (
		('0', 'Game'),
		('1', 'Software'),
	)
	app_type = models.CharField(max_length=1, choices=APP_TYPE_CHOICES)
	published_date = models.DateTimeField(
		blank=True, null=True)
	# Category
	name = models.CharField(max_length=200)
	tags = models.ManyToManyField(Tag)
	steam_appid = models.IntegerField()
	is_free = models.NullBooleanField()
	header_img = models.CharField(max_length=200)
	# header_img_upload = models.ImageField(upload_to='app_header_img', blank=True, null=True)
	website = models.CharField(max_length=200)
	desc = models.TextField()

	def __str__(self):
		return self.name
