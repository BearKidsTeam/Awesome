from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Post

# Create your views here.

def thread_list(request):
	threads = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	page = [{'title': 'Awesome', 'url': '#'}, {'title': 'Recommand List', 'url': reverse('thread_list')}]
	return render(request, 'awesome/thread_list.html', {'threads': threads, 'page':page})

def thread_detail(request, pk):
	thread = get_object_or_404(Post, pk=pk) 
	page = [{'title': 'Awesome', 'url': '#'}, {'title': 'Recommand List', 'url': reverse('thread_list')}, {'title': 'Detail', 'url': '#'}]
	return render(request, 'awesome/thread_detail.html', {'thread': thread, 'page':page})
