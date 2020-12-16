from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
# Create your views here.
from newsapi import NewsApiClient


def Home(request):
    return render(request, 'blog/Home.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('home')
            else:
                print('User not found')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def all_news(request):
    newsapi = NewsApiClient(api_key='80a893cc368d4e39a2ed0123757b9131')
    all = newsapi.get_everything(sources='the-hindu')
    l = all['articles']
    p = Paginator(l, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'blog/all_news.html', context={"mylist": page_obj})


def logout_user(request):
    logout(request)
    return render(request, 'blog/Home.html')
