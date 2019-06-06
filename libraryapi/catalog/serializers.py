from rest_framework import serializers
from .models import Book, Author, Language, Genre

class BookSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Book
        fields = ('title', 'author', 'summary', 'isbn', 'genre', 'language')

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth')

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('name',)

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)