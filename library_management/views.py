from django.shortcuts import render
from books.models import BookRecord

def home(request):
    books = BookRecord.objects.all()  # Fetch books for homepage
    return render(request, 'home.html', {'books': books, 'user': request.user})

