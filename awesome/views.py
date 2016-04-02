from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def thread_list(request):
	threads = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'awesome/thread_list.html', {'threads': threads})
