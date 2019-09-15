from django.shortcuts import render

from django.http import HttpResponse

from django.db import models

from .models import Genre, Movie

# Create your views here.
def index(request):
    all_movies = Movie.objects.all()
    return render(request, 'views/index.html', {'title': 'Home Page', 'catalog' : all_movies})

def about(request):
    return render(request, 'views/about.html', {'title': 'About Me'})

def read_test(request):
    all = Genre.objects.all()
    print(all)
    names = ''
    for g in all:
        names += g.name

    return HttpResponse(names)