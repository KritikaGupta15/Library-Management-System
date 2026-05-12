from django.urls import path
from .views import book_collection, add_book_view, edit_book, delete_book, manage_books, borrow_book
from . import views
urlpatterns = [
    path('', book_collection, name='book_collection'),
    path('add/', add_book_view, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
    path('manage/', manage_books, name='manage_books'),
    path('books/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('books/', views.book_list, name='book_list'),
    path('search/', views.search_results, name='search_results'),
]








