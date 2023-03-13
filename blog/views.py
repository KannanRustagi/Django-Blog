from django.shortcuts import render
from django.http import HttpResponse

posts=[{
    'author':'Corey',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date':'august 23 2003'
},
{
    'author':'jane doe',
    'title': 'Blog Post 2',
    'content': 'second post content',
    'date':'august 28 2003'
}
]

def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

