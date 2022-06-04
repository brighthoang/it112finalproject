from django import forms
from .models import Books, Movies, Music

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'