from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.thread_list, name='home_page'),
	url(r'^thread/list/$', views.thread_list, name='thread_list'),
	url(r'^app/list/$', views.app_list, name='app_list'),
	url(r'^thread/(?P<pk>[0-9]+)/$', views.thread_detail, name='thread_detail'),
]
