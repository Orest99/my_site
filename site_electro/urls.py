from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home_1', views.home1, name='home_1'),
    path('home_2', views.home2, name='home_2'),
    path('home_3', views.home3, name='home_3'),
    path('home_4', views.home4, name='home_4'),
]