from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('languages/', views.LanguageListView.as_view(), name='languages'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]