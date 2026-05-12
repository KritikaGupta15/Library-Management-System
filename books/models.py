from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class BookRecord(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    available_copies = models.IntegerField(default=1)

    class Meta:
        db_table = "books_bookrecord"  # Explicitly set the correct table name

class BorrowRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # User borrowing the book
    book = models.ForeignKey(BookRecord, on_delete=models.CASCADE)  # Book being borrowed
    borrowed_date = models.DateField(auto_now_add=True)  # Date borrowed
    due_date = models.DateField()  # Return deadline
    returned = models.BooleanField(default=False)
