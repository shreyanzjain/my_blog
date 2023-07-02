from typing import Any, Optional
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post, Comments
from django.contrib.auth.models import User
from blog.forms import EditComment

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post

class UserPostListView(ListView):
    model = Post
    template_name='blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostCreateView(CreateView):
    model = Post
    fields =['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form_update.html'
    fields = ['title', 'content']

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
    
class CommentCreateView(CreateView):
    model = Comments
    template_name = 'blog/comment_form.html'
    form_class = EditComment
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
    
class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comments
    success_url = '/'
    def test_func(self) -> bool:
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False

@login_required()
def about(request):
    return render(request, 'blog/about.html')