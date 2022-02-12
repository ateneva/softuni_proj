from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# function-based views

def home_page(request):
    return HttpResponse('It works')

# class-based views