from django.shortcuts import render

# Create your views here.

def thread_list(request):
	return render(request, 'awesome/thread_list.html', {})
