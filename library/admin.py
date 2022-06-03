from django.contrib import admin
from .models import Books, Movies, Music

admin.site.register(Books)
admin.site.register(Movies)
admin.site.register(Music)