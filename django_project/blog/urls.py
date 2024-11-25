from django.urls import path
from . import views

urlpatterns = [
    # route, function, name
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about")
]