from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def thread_list(request):
	threads = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'awesome/thread_list.html', {'threads': threads})

def thread_detail(request, pk):
	thread = get_object_or_404(Post, pk=pk)
	return render(request, 'awesome/thread_detail.html', {'thread': thread})
