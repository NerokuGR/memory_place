from django.urls import path
from gmap import views

urlpatterns = [
    path('map/', views.gmap, name='map'),
]
