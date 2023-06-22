from django.urls import path
from django.contrib.auth.decorators import login_required
from blog import views

urlpatterns = [
    path('', login_required(views.PostListView.as_view()), name='blog-home'),
    path('post/<int:pk>/', login_required(views.PostDetailView.as_view()), name='blog-post-detail'),
    path('post/new/', login_required(views.PostCreateView.as_view()), name='blog-post-create'),
    path('post/<int:pk>/update/', login_required(views.PostUpdateView.as_view()), name='blog-post-update'),
    path('post/<int:pk>/delete/', login_required(views.PostDeleteView.as_view()), name='blog-post-delete'),
    path('user/<str:username>/', login_required(views.UserPostListView.as_view()), name='blog-user-posts'),
    path('about', views.about, name='blog-about'),
]