from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'newpost/news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_publication'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'newpost/post.html'
    context_object_name = 'post'

