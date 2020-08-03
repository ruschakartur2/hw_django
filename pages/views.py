from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
