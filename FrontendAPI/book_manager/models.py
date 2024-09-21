from django.db import models
from user.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.user} borrowed {self.book}"
