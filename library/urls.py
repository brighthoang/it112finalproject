from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name="books"),
    path('movies/', views.movies, name="movies"),
    path('music/', views.music, name="music"),
    path('booksdetail/<int:id>', views.booksDetail, name="booksdetail"),
    path('moviesdetail/<int:id>', views.moviesDetail, name="moviesdetail"),
    path('musicdetail/<int:id>', views.musicDetail, name="musicdetail"),
] 