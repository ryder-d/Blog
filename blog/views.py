from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def index(request):
    # template directory for render command is defined by dirs in settings.py
    return render(request, 'index.html')

# TODO explore function based alternative
# https://www.bedjango.com/blog/class-based-views-vs-function-based-views/
class BlogListView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_post_list.html'

class BlogPost(DetailView):
    model = Post
    template_name = 'blog_post.html'