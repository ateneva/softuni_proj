# it's neater to export all your app views to APP urls.py

from django.urls import path
from mydjangosite.mydjangosite.demo_app.views import home_page

# App
urlpatterns = [
    path('', home_page),
]
