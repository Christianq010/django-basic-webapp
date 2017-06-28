from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [ 
        url(r'^$', ListView.as_view(
                        # list all objects (posts) and list 25 of them by the newest
                        queryset=Post.objects.all().order_by("-date")[:25],
                        template_name="blog/blog.html")),
        # creating a url for individual blogs
        # <pk> is the primary key, d+ for python to know its > 1
        url(r'^(?P<pk>\d+)$', DetailView.as_view(
                        model = Post,
                        template_name="blog/post.html")),
            ]