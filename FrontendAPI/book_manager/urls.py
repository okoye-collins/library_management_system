from django.urls import path
from .views import  ListBooksView, BookDetailView, FilterBooksView, BorrowBookView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name='list-books'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/filter/', FilterBooksView.as_view(), name='filter-books'),
    path('books/borrow/', BorrowBookView.as_view(), name='borrow-book'),
]