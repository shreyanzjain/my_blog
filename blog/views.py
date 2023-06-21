from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.models import User

# posts = [
#     {
#         'title': 'Post 1',
#         'author': 'Shreyans',
#         'date_posted': 'Aug 27, 2021',
#         'content': 'This is post 1'
#     },
#     {
#         'title': 'Post 2',
#         'author': 'Pinky',
#         'date_posted': 'Aug 28, 2021',
#         'content': 'This is post 2'
#     }
# ]
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class UserPostListView(DetailView):
    model = User
    template_name='blog/user_post.html'

@login_required()
def about(request):
    return render(request, 'blog/about.html')