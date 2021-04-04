from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'index.html')


def search_city(request):
    return render(request, 'search_city.html')


def searched_city(request):
    return render(request, 'search_filters.html')


def searched_filters(request):
    return render(request, 'results.html')


def create(request):
    return redirect('search/new/filters')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def test(request):
    return render(request, "test.html")
