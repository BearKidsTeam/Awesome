# from django.shortcuts import render
# from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import *


# Create your views here.

def thread_list(request):
	threads = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Recommands', 'url': reverse('thread_list')}]
	return render(request, 'awesome/thread_list.html', {'threads': threads, 'page': page})


def thread_detail(request, pk):
	thread = get_object_or_404(Post, pk=pk)
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Recommands', 'url': reverse('thread_list')},
			{'title': 'Detail', 'url': '#'}]
	return render(request, 'awesome/thread_detail.html', {'thread': thread, 'page': page})


def app_list(request):
	apps = Application.objects.filter().order_by('name')
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Applications', 'url': reverse('app_list')}]
	return render(request, 'awesome/app_list.html', {'apps': apps, 'page': page})


def app_detail(request, pk):
	app = get_object_or_404(Application, pk=pk)
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Applications', 'url': reverse('app_list')},
			{'title': 'Detail', 'url': '#'}]
	return render(request, 'awesome/app_detail.html', {'app': app, 'page': page})


def tag_id(request, pk):
	tag = get_object_or_404(Tag, pk=pk)
	app = Application.objects.filter(tags__pk=pk)
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Tags', 'url': reverse('tag_list')},
			{'title': 'Apps', 'url': reverse('tag_id', kwargs={'pk': pk})}]
	return render(request, 'awesome/tag_id.html', {'tag': tag, 'apps': app, 'page': page})


def tag_list(request):
	tags = Tag.objects.filter().order_by('name')
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Tags', 'url': reverse('tag_list')}]
	return render(request, 'awesome/tag_list.html', {'tags': tags, 'page': page})
