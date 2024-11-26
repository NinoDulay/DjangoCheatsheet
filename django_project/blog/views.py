from django.shortcuts import render

from django.http import HttpResponse


# Sample dynamic data
posts = [
    {
        "author": "NinoDulay",
        "title": "Blog Post 1",
        "content": "First content ever!",
        "date_posted": "August 20, 2020"
    },
    {
        "author": "NinoDulay",
        "title": "Blog Post 2",
        "content": "Second content ever!",
        "date_posted": "August 20, 2021"
    }
]

# Create your views here.

## Handle traffic from homepage of our blog
def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)

    #return render(request, 'blog/home.html')    
    # return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})