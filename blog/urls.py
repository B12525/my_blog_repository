from django.conf.urls import url
from django.view.generic import ListView,DetailView
from .models import Posts

urlpatterns = [
url('',ListView.as_view(queryset=Posts.objects.all().order_by('-date')[:20]),
,template_name='blog/posts_temp.html'),
url('(?P<pk>\d+)',DetailView(model=Post),template_name='blog/one_post_temp.html'),
]
