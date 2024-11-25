from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

## Handle traffic from homepage of our blog
def home(request):
    
    return render(request, 'blog/home.html')
    
    # return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')