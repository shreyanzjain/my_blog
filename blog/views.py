from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

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
@login_required()
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

@login_required()
def about(request):
    return render(request, 'blog/about.html')