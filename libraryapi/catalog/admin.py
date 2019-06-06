from django.contrib import admin
from .models import Author, Book, Language, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)