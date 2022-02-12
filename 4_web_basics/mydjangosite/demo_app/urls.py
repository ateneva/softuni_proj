# it's neater if every app has its own urls.py

from django.urls import path
from demo_app import views

# App
urlpatterns = [
    path('', views.home_page),
]
