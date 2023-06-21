from typing import Optional
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
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

class PostCreateView(CreateView):
    model = Post
    fields =['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form_update.html'
    fields =['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required()
def about(request):
    return render(request, 'blog/about.html')