import re
from django.shortcuts import render, get_object_or_404
from .models import Books, Movies, Music
from django.urls import reverse_lazy

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


def booksDetail(request, id):
    books=get_object_or_404(Books, pk=id)
    return render(request, 'library/booksdetail.html', {'books': books})


def moviesDetail(request, id):
    movies=get_object_or_404(Movies, pk=id)
    return render(request, 'library/moviesdetail.html', {'movies': movies})


def musicDetail(request, id):
    music=get_object_or_404(Music, pk=id)
    return render(request, 'library/musicdetail.html', {'music': music})
