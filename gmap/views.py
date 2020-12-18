from django.shortcuts import render


def gmap(request):
    data = {
        'title': 'map',
    }
    return render(request, 'gmap/Google_map.html', data)
