from django.test import TestCase
from .models import Books, Movies, Music
from django.contrib.auth.models import User


class BooksTest(TestCase):
    def setUp(self):
        self.all = Books(book_title = 'Diary of a Wimpy Kid: The Last Straw', author = "Jeff Kinney", 
        ISBN = "978-0-8109-8892-7", publishyear = 2009)

    def test_typestring(self):
        self.assertEqual(str(self.all), "Diary of a Wimpy Kid: The Last Straw")

    def test_tablename(self):
        self.assertEqual(str(Books._meta.db_table), 'books')


class MoviesTest(TestCase):
    def setUp(self):
        self.all = Movies(movie_title = 'Ratatouille', director = "Brad Bird", 
        genre = "Comedy/Family", releaseyear = 2007)

    def test_typestring(self):
        self.assertEqual(str(self.all), "Ratatouille")

    def test_tablename(self):
        self.assertEqual(str(Movies._meta.db_table), 'movies')


class MusicTest(TestCase):
    def setUp(self):
        self.all = Music(song_title = 'Blue & Grey', artist = "BTS", 
        genre = "KPOP", releaseyear = 2020)

    def test_typestring(self):
        self.assertEqual(str(self.all), "Blue & Grey")

    def test_tablename(self):
        self.assertEqual(str(Music._meta.db_table), 'music')
