from django.urls import path
from django.contrib.auth.decorators import login_required
from blog import views

urlpatterns = [
    path('', login_required(views.PostListView.as_view()), name='blog-home'),
    path('post/<int:pk>/', login_required(views.PostDetailView.as_view()), name='blog-post-detail'),
    path('<pk>/posts/', login_required(views.UserPostListView.as_view()), name='blog-user-posts'),
    path('about', views.about, name='blog-about'),
]