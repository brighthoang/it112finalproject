import re
from django.shortcuts import render
from .models import Books, Movies, Music

def index(request):
    return render(request, 'library/index.html')

def books(request):
    books_list = Books.objects.all()
    return render(request, 'library/books.html', {'books_list': books_list})


def movies(request):
    movies_list = Movies.objects.all()
    return render(request, 'library/movies.html', {'movies_list': movies_list})


def music(request):
    music_list = Music.objects.all()
    return render(request, 'library/music.html', {'music_list': music_list})