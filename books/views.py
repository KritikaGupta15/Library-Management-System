from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BookRecord
from django.db.models import Q
from .forms import BookForm, BorrowForm

# View for listing books
def book_collection(request):
    books = BookRecord.objects.all()
    return render(request, 'books/book_collection.html', {'books': books})

def book_list(request):
    books = BookRecord.objects.all()  # Get all books from the database
    return render(request, 'books/book_list.html', {'books': books})

# View for adding a book (Admin Only)



# View for editing a book
def edit_book(request, book_id):
    book = get_object_or_404(BookRecord, book_id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)  # Initialize form with data and instance
        if form.is_valid():
            form.save()  # Save the changes
            return redirect('home')  # Redirect to book list
    else:
        form = BookForm(instance=book)  # Initialize form with the book instance
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})  # Pass form to template


# View for deleting a book
def delete_book(request, book_id):
    book = get_object_or_404(BookRecord, book_id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('home')
    return render(request, 'books/confirm_delete.html', {'book': book})

@login_required
def book_collection(request):
    books = BookRecord.objects.all()
    return render(request, 'books/base.html', {'books': books})

def manage_books(request):
    if request.user.is_authenticated and request.user.role == "admin":
        books = BookRecord.objects.all()
        return render(request, 'books/manage_books.html', {'books': books})
    else:
        return render(request, 'error.html', {'message': "You do not have permission to view this page."})
def add_book_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')  # ✅ Redirect after adding book
        else:
            form = BookForm()
        return render(request, 'books/add_book.html', {'form': form})
    else:
        return redirect('home')


def borrow_book(request, book_id):
    book = get_object_or_404(BookRecord, book_id=book_id)

    if request.method == "POST":
        form = BorrowForm(request.POST)  # Or process data directly from request.POST
        if form.is_valid():  # Or your validation logic
            borrow_record = form.save(commit=False) # If using a form
            borrow_record.user = request.user
            borrow_record.book = book
            borrow_record.save()

            # Decrease available copies
            book.available_copies -= 1
            book.save()  # Save the updated book

            return redirect('home')  # Or wherever you want to redirect
    else:
        form = BorrowForm() # If using a form

    return render(request, 'books/borrow_book.html', {'form': form, 'book': book})




def search_results(request):
    query = request.GET.get('q')
    if query:
        results = BookRecord.objects.filter(  # ⚠️  Use BookRecord
            Q(book_name__icontains=query) | Q(author__icontains=query)  # ⚠️  Use your actual field names
        ).distinct()
    else:
        results = BookRecord.objects.all()  # Or BookRecord.objects.none()
    return render(request, 'books/search_results.html', {'results': results, 'query': query})
