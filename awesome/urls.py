from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.thread_list, name='home_page'),
	url(r'^thread/$', views.thread_list, name='thread_list'),
	url(r'^app/$', views.app_list, name='app_list'),
	url(r'^thread/(?P<pk>[0-9]+)/$', views.thread_detail, name='thread_detail'),
	url(r'^app/(?P<pk>[0-9]+)/$', views.app_detail, name='app_detail'),
	url(r'^tag/$', views.tag_list, name='tag_list'),
	url(r'^tag/(?P<pk>[0-9]+)/$', views.tag_id, name='tag_id'),
	url(r'^tag/query/$', views.tag_query, name='tag_query'),
]
