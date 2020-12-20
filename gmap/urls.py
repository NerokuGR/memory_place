from django.urls import path
from gmap import views

urlpatterns = [
    path('', views.gmap, name='map'),
]
