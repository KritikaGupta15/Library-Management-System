from django import forms
from .models import BookRecord, BorrowRecord

class BookForm(forms.ModelForm):
    class Meta:
        model = BookRecord  # Ensure this matches your actual model name
        fields = ['book_name', 'author', 'publisher', 'published_date', 'category', 'available_copies']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['book', 'due_date']