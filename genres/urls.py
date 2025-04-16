from django.shortcuts import render
from django.urls import path
from .views import genre_view, genre_by_id_view

urlpatterns = [
    path('genres', genre_view, name='genre_view'),
    path('genres/<int:pk>', genre_by_id_view, name='genre_by_id_view')
]