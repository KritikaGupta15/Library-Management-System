from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import SignupForm, LoginForm


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'user/signup_login.html', {'signup_form': form})



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser:  # ✅ Ensure superuser login works  # 🔥 Redirect admins to dashboard
                    return redirect('home')  # ✅ Redirect regular users properly
            else:
                form.add_error(None, "Invalid username or password")  # 🚨 Show error message
    else:
        form = LoginForm()

    return render(request, 'user/signup_login.html', {'login_form': form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def is_admin(user):
    return user.role == "admin"

@login_required
@user_passes_test(is_admin)
def manage_books(request):
    return render(request, 'books/manage_books.html')