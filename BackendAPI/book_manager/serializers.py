# admin_api/serializers.py

from rest_framework import serializers
from .models import Book, Borrow


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "author", "publisher", "category", "available"]


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ["user", "book", "borrowed_date", "return_date"]
