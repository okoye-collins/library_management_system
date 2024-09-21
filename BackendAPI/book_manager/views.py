# admin_api/views.py

from rest_framework import generics
from .models import Book, User, Borrow
from .serializers import BookSerializer, BorrowSerializer

class AddBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RemoveBookView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

# class ListUsersView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class ListBorrowedBooksView(generics.ListAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

class ListUnavailableBooksView(generics.ListAPIView):
    queryset = Book.objects.filter(available=False)
    serializer_class = BookSerializer
