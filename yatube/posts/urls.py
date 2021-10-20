from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index),
    path('posts/group_list.html', views.group_posts, name='group_list'),
    path('index.html', views.index, name='index'),
]