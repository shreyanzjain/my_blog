from django.shortcuts import render

posts = [
    {
        'title': 'Post 1',
        'author': 'Shreyans',
        'date_posted': 'Aug 27, 2021',
        'content': 'This is post 1'
    },
    {
        'title': 'Post 2',
        'author': 'Pinky',
        'date_posted': 'Aug 28, 2021',
        'content': 'This is post 2'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')