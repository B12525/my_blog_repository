from django.urls import path
from django.views.generic import ListView,DetailView
from .models import Posts

urlpatterns = [
path('',ListView.as_view(queryset=Posts.objects.all().order_by('-date')[:20]
,template_name='blog/posts_temp.html')),
path('post/<int:pk>',DetailView.as_view(model=Posts,template_name='blog/one_post_temp.html')),
]
