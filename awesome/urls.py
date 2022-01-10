from django.urls import path

from . import views

urlpatterns = [
    path('', views.thread_list, name='home_page'),
    path('thread/', views.thread_list, name='thread_list'),
    path('app/', views.app_list, name='app_list'),
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('app/<int:pk>/', views.app_detail, name='app_detail'),
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/<int:pk>/', views.tag_id, name='tag_id'),
    path('tag/query/', views.tag_query, name='tag_query'),
]