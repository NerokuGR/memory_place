from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main_app/home_page.html', data)


def about(request):
    return render(request, 'main_app/about.html')
