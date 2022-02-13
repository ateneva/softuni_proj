from django.urls import path, include
from employees import views

urlpatterns = [
    path('', views.home_page, name='demo-home'),
]