from rest_framework import generics
from .models import Book, Borrow
from .serializers import BookSerializer, BorrowSerializer

# Create your views here.

class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class FilterBooksView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        publisher = self.request.query_params.get('publisher')
        category = self.request.query_params.get('category')
        if publisher:
            queryset = queryset.filter(publisher=publisher)
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class BorrowBookView(generics.CreateAPIView):
    serializer_class = BorrowSerializer
    queryset = Borrow.objects.all()
    
    def perform_create(self, serializer):
        # Mark the book as borrowed (unavailable)
        book = serializer.validated_data['book']
        book.available = False
        book.save()
        serializer.save()