# from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Count
from .models import *


# Utils func.

# match the items CONTAIN all the gaven ids
def get_multi_match(model_class, m2m_field, ids):
	query = model_class.objects.all()
	for _id in ids:
		query = query.filter(**{m2m_field: _id})
	return query


# match all items which's ids EXACTLY match the gaven ids list
def get_exact_match(model_class, m2m_field, ids):
	query = model_class.objects.annotate(count=Count(m2m_field)).filter(count=len(ids))
	for _id in ids:
		query = query.filter(**{m2m_field: _id})
	return query


# Views here.

def thread_list(request):
	threads = Post.objects.filter(published_date__lte=timezone.now(), assoc__isnull=True).order_by('-published_date')
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Recommends', 'url': reverse('thread_list')}]
	return render(request, 'awesome/thread_list.html', {'threads': threads, 'page': page})


def thread_detail(request, pk):
	thread = get_object_or_404(Post, pk=pk)
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Recommends', 'url': reverse('thread_list')},
			{'title': 'Detail', 'url': '#'}]
	return render(request, 'awesome/thread_detail.html', {'thread': thread, 'page': page})


def app_list(request):
	apps = Application.objects.filter().order_by('name')
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Applications', 'url': reverse('app_list')}]
	return render(request, 'awesome/app_list.html', {'apps': apps, 'page': page})


def app_detail(request, pk):
	app = get_object_or_404(Application, pk=pk)
	reviews = Post.objects.filter(assoc__pk=pk).order_by('-published_date')
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Applications', 'url': reverse('app_list')},
			{'title': 'Detail', 'url': '#'}]
	return render(request, 'awesome/app_detail.html', {'app': app, 'page': page, 'reviews': reviews})


def tag_id(request, pk):
	tag = get_object_or_404(Tag, pk=pk)
	apps = Application.objects.filter(tags__pk=pk)
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Tags', 'url': reverse('tag_list')},
			{'title': 'Apps', 'url': reverse('tag_id', kwargs={'pk': pk})}]
	return render(request, 'awesome/tag_id.html', {'tag': tag, 'apps': apps, 'page': page})


def tag_list(request):
	tags = Tag.objects.filter().order_by('name')
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Tags', 'url': reverse('tag_list')}]
	return render(request, 'awesome/tag_list.html', {'tags': tags, 'page': page})


def tag_query(request):
	search_tags = request.GET.getlist('tag')
	tags = Tag.objects.filter(pk__in=search_tags).order_by('name')
	apps = get_multi_match(Application, 'tags__pk', search_tags)  # FIXME: 'search_tags' should be a list type 'tags'
	page = [{'title': 'Awesome', 'url': reverse('home_page')}, {'title': 'Tag Filter', 'url': reverse('tag_query')}]
	return render(request, 'awesome/tag_query.html', {'tags': tags, 'apps': apps, 'page': page})
