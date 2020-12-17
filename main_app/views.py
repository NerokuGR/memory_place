from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# отображение страницы логина
def login(request):
    data = {
        'title': 'Sign in',
    }
    return render(request, 'main_app/login.html', data)


# декоратор для логина
# отображение стартовой странцы
@login_required
def index(request):
    data = {
        'title': 'Home',
    }
    return render(request, 'main_app/home_page.html', data)


# отображение странцы о нас
def about(request):
    data = {
        'title': 'about',
    }
    return render(request, 'main_app/about.html', data)
