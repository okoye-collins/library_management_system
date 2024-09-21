
from django.urls import path
from .views import AddBookView, RemoveBookView, ListBorrowedBooksView, ListUnavailableBooksView

urlpatterns = [
    path('add-book/', AddBookView.as_view(), name='add-book'),
    path('remove-book/<int:id>/', RemoveBookView.as_view(), name='remove-book'),
    path('borrowed-books/', ListBorrowedBooksView.as_view(), name='list-borrowed-books'),
    path('unavailable-books/', ListUnavailableBooksView.as_view(), name='list-unavailable-books'),
]
