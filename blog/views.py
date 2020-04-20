from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
# demic data
posts = [
    {
        'author': 'Anik',
        'title': 'Python for Beginners',
        'Content': 'Who are u?',
    },
    {
        'author': 'Parvej',
        'title': 'Introduction To laravel',
        'Content': 'Who are u?',
    }
]


# end Demic Data
# function base view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogs/home.html', context)


def about(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogs/about.html', context)


# Class Base View
class PostListView(ListView):
    model = Post
    template_name = 'blogs/home.html'  # <app>/<model>_<viewtype>html
    context_object_name = 'posts'
    ordering = ['-data_posted']


class PostDetailListView(DetailView):
    model = Post
    template_name = 'blogs/post_view.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blogs/post_form.html'
    def  form_valid(self, form):
        form.instance.author = self.request.user
        return  super().form_valid(form)
